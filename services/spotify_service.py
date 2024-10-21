import requests
import enum

from db.crud import UserManager, UserRepository, UserTokenManager, UserTrackManager, UserNotFoundError
from db.types import TopTracksType

from services.spotify_auth import SpotifyAuth, NotAuthorizedError
from typing import Optional, List


class TimeRange(enum.Enum):
    short_term = 'short_term'
    medium_term = 'medium_term'
    long_term = 'long_term'


class SpotifyService():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_user_top_tracks(user_id: int, time_range: TimeRange) -> Optional[List[TopTracksType]]:
        instance = SpotifyService()
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError("User is not authorized")

        status_code, data = instance._request_top_tracks(user.access_token, time_range)
        
        if status_code == 401:
            try: 
                spotify_auth = SpotifyAuth()
                user.access_token = spotify_auth.refresh_access_token(user.refresh_token)
                user = update_user(user.id, user.access_token)
                status_code, data = SpotifyService._request_top_tracks(user.access_token, time_range)
            except Exception as e:
                print(e)
                return
        
        if status_code != 200:
            print(data, status_code)
            return
        
        result = []
        for track in data.get('items'):
            result.append({'name': track.get('name'), 'artist': track.get('artists')[0].get('name') })
        
        return result

    def _request_top_tracks(self, access_token, time_range):
        response = requests.get(f'https://api.spotify.com/v1/me/top/tracks?limit=10&time_range={time_range}', headers={
                    'Authorization': f'Bearer {access_token}'
                })
        return response.status_code, response.json()

    def _request_get_user_profile(self, access_token):
        response = requests.get('https://api.spotify.com/v1/me', headers={
                'Authorization': f'Bearer {access_token}'  # type: ignore
                })
        return response.status_code, response.json()

    @staticmethod
    def get_user_profile(user_id):
        user = get_user(user_id)
        
        if user and user.access_token is None:
            return
        
        status_code, data = request_get_user_profile(user.access_token) # type: ignore
        
        if status_code == 401:
            try: 
                user.access_token = refresh_access_token(user.id) # type: ignore
                user = update_user(user.id, user.access_token) # type: ignore
                status_code, data = request_get_user_profile(user.access_token) # type: ignore
            except Exception as e:
                print(e)
                return
        
        if status_code != 200:
            print(data, status_code)
            return
        
        return data