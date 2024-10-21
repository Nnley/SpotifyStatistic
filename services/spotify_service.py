import requests
import enum

from db.crud import UserManager, UserRepository, UserTokenManager, UserTrackManager
from db.types import TopTracksType, IUser

from services.spotify_auth import SpotifyAuth, NotAuthorizedError
from typing import Optional, List, cast


class TimeRange(enum.Enum):
    short_term = 'short_term'
    medium_term = 'medium_term'
    long_term = 'long_term'


class SpotifyAPI:
    def __init__(self):
        self.base_url = 'https://api.spotify.com/v1'
    
    def fetch_top_tracks(self, access_token: str, time_range: TimeRange) -> tuple[int, dict]:
        url = f'{self.base_url}/me/top/tracks?limit=10&time_range={time_range}'
        response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})
        return response.status_code, response.json()

    def fetch_user_profile(self, access_token: str) -> tuple[int, dict]:
        url = f'{self.base_url}/me'
        response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})
        return response.status_code, response.json()


class SpotifyService():
    def __init__(self):
        self.spotify_api = SpotifyAPI()

    def get_user_top_tracks(self, user_id: int, time_range: TimeRange) -> Optional[List[TopTracksType]]:
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError(f"User {user.id} is not authorized")

        status_code, data = self.spotify_api.fetch_top_tracks(user.access_token, time_range)
        
        if status_code == 401:
            user = self.refresh_user_tokens(user)
            status_code, data = self.spotify_api.fetch_top_tracks(cast(str, user.access_token), time_range)

        if status_code != 200:
            raise Exception(f'Request top tracks error with status code: {status_code}')

        return self.parse_top_tracks(data)

    def get_user_profile(self, user_id):
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError(f"User {user.id} is not authorized")
        
        status_code, data = self.spotify_api.fetch_user_profile(user.access_token)
        
        if status_code == 401:
            user = self.refresh_user_tokens(user)
            status_code, data = self.spotify_api.fetch_user_profile(cast(str, user.access_token))
        
        if status_code != 200:
            raise Exception(f'Request user profile error with status code: {status_code}')
        
        return data
    
    def refresh_user_tokens(self, user: IUser) -> IUser:
        try:    
            spotify_auth = SpotifyAuth()
            user.refresh_token, user.access_token = spotify_auth.refresh_access_token(cast(str, user.refresh_token))
            UserTokenManager.set_access_token(user.id, user.access_token)
            UserTokenManager.set_refresh_token(user.id, user.refresh_token)
            return user
        except Exception as e:
            raise Exception(f"Failed to refresh access token: {e}")

    def parse_top_tracks(self, data):
        result = []
        for track in data.get('items', []):
            result.append({'name': track.get('name'), 'artist': track.get('artists')[0].get('name')})
        return result