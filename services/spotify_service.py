import aiohttp
import enum

from db.crud import UserManager, UserRepository, UserTokenManager, UserTrackManager
from db.types import TopTracksType, IUser, IUserProfile, TopArtistsType
from services.types import Track

from services.spotify_auth import SpotifyAuth, NotAuthorizedError
from typing import Optional, List, cast
from datetime import datetime


class TimeRange(enum.Enum):
    SHORT_TERM = 'short_term'
    MEDIUM_TERM = 'medium_term'
    LONG_TERM = 'long_term'


class SpotifyAPI:
    def __init__(self):
        self.base_url = 'https://api.spotify.com/v1'

    async def fetch_top_tracks(self, access_token: str, time_range: TimeRange) -> tuple[int, dict]:
        url = f'{self.base_url}/me/top/tracks?limit=10&time_range={time_range.value}'
        headers = {'Authorization': f'Bearer {access_token}'}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                return response.status, await response.json()

    async def fetch_top_artists(self, access_token: str, time_range: TimeRange) -> tuple[int, dict]:
        url = f'{self.base_url}/me/top/artists?limit=10&time_range={time_range.value}'
        headers = {'Authorization': f'Bearer {access_token}'}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                return response.status, await response.json()

    async def fetch_user_profile(self, access_token: str) -> tuple[int, dict]:
        url = f'{self.base_url}/me'
        headers = {'Authorization': f'Bearer {access_token}'}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                return response.status, await response.json()
    
    async def fetch_currently_playing(self, access_token: str) -> tuple[int, dict]:
        url = f'{self.base_url}/me/player/queue'
        headers = {'Authorization': f'Bearer {access_token}'}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                return response.status, await response.json()


class SpotifyService():
    def __init__(self):
        self.spotify_api = SpotifyAPI()
        
    async def get_user_currently_playing(self, user_id: int) -> Optional[Track]:
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError(f"User {user.id} is not authorized")

        status_code, data = await self.spotify_api.fetch_currently_playing(cast(str, user.access_token))
        
        if status_code == 401:
            user = await self.refresh_user_access_token(user)
            status_code, data = await self.spotify_api.fetch_currently_playing(cast(str, user.access_token))
            
        if status_code != 200:
            raise Exception(f'Request currently playing error with status code: {status_code}')
            
        return data['currently_playing'] if data.get('currently_playing') else None

    async def get_user_top_tracks(self, user_id: int, time_range: TimeRange) -> Optional[List[TopTracksType]]:
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError(f"User {user.id} is not authorized")
        
        if time_range == TimeRange.SHORT_TERM:
            cached_tracks = UserTrackManager.get_top_tracks_month(user.id)
        elif time_range == TimeRange.MEDIUM_TERM:
            cached_tracks = UserTrackManager.get_top_tracks_half_year(user.id)
        elif time_range == TimeRange.LONG_TERM:
            cached_tracks = UserTrackManager.get_top_tracks_year(user.id)
        
        if cached_tracks:
            updated_at = datetime.strptime(cached_tracks[0]['updated_at'], '%Y-%m-%d')
            current_date = datetime.now()

            if updated_at.date() != current_date.date():
                return await self._update_top_tracks(user, time_range)

            return cached_tracks

        return await self._update_top_tracks(user, time_range)
    
    async def _update_top_tracks(self, user: IUser, time_range: TimeRange) -> List[TopTracksType]:
        status_code, data = await self.spotify_api.fetch_top_tracks(cast(str, user.access_token), time_range)

        if status_code == 401:
            user = await self.refresh_user_access_token(user)
            status_code, data = await self.spotify_api.fetch_top_tracks(cast(str, user.access_token), time_range)

        if status_code != 200:
            raise Exception(f'Request top tracks error with status code: {status_code}')

        top_tracks = self._parse_top_tracks(data)
        
        #TODO: change the updated_at from this object to a new one(db)
        current_time = datetime.now().date().isoformat()
        for track in top_tracks:
            track['updated_at'] = current_time
            
        if time_range == TimeRange.SHORT_TERM:
            UserTrackManager.set_top_tracks_month(user.id, top_tracks)
        elif time_range == TimeRange.MEDIUM_TERM:
            UserTrackManager.set_top_tracks_half_year(user.id, top_tracks)
        elif time_range == TimeRange.LONG_TERM:
            UserTrackManager.set_top_tracks_year(user.id, top_tracks)

        return top_tracks

    async def get_user_top_artists(self, user_id: int, time_range: TimeRange) -> Optional[List[TopArtistsType]]:
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError(f"User {user.id} is not authorized")
        
        if time_range == TimeRange.SHORT_TERM:
            cached_artists = UserTrackManager.get_top_artists_month(user.id)
        elif time_range == TimeRange.MEDIUM_TERM:
            cached_artists = UserTrackManager.get_top_artists_half_year(user.id)
        elif time_range == TimeRange.LONG_TERM:
            cached_artists = UserTrackManager.get_top_artists_year(user.id)
        
        if cached_artists:
            updated_at = datetime.strptime(cached_artists[0]['updated_at'], '%Y-%m-%d')
            current_date = datetime.now()

            if updated_at.date() != current_date.date():
                return await self._update_top_artists(user, time_range)

            return cached_artists

        return await self._update_top_artists(user, time_range)

    async def _update_top_artists(self, user: IUser, time_range: TimeRange) -> List[TopArtistsType]:
        status_code, data = await self.spotify_api.fetch_top_artists(cast(str, user.access_token), time_range)

        if status_code == 401:
            user = await self.refresh_user_access_token(user)
            status_code, data = await self.spotify_api.fetch_top_artists(cast(str, user.access_token), time_range)

        if status_code != 200:
            raise Exception(f'Request top tracks error with status code: {status_code}')

        top_artists = self._parse_top_artists(data)
        
        #TODO: change the updated_at from this object to a new one(db)
        current_time = datetime.now().date().isoformat()
        for artist in top_artists:
            artist['updated_at'] = current_time
            
        if time_range == TimeRange.SHORT_TERM:
            UserTrackManager.set_top_artists_month(user.id, top_artists)
        elif time_range == TimeRange.MEDIUM_TERM:
            UserTrackManager.set_top_artists_half_year(user.id, top_artists)
        elif time_range == TimeRange.LONG_TERM:
            UserTrackManager.set_top_artists_year(user.id, top_artists)

        return top_artists

    async def get_user_profile(self, user_id: int) -> IUserProfile:
        user = UserManager.get_or_create_user(user_id)

        if user.access_token is None or user.refresh_token is None:
            raise NotAuthorizedError(f"User {user.id} is not authorized")
        
        if user.country and user.display_name and user.updated_at and user.updated_at.date() == datetime.now().date():
            return {
                'country': user.country,
                'display_name': user.display_name
            }
        
        status_code, data = await self.spotify_api.fetch_user_profile(user.access_token)
        
        if status_code == 401:
            user = await self.refresh_user_access_token(user)
            status_code, data = await self.spotify_api.fetch_user_profile(cast(str, user.access_token))
        
        if status_code != 200:
            raise Exception(f'Request user profile error with status code: {status_code}')
        
        user.country = data.get('country')
        user.display_name = data.get('display_name')
        
        UserRepository.update_user(user)
        
        return data # type: ignore
    
    async def refresh_user_access_token(self, user: IUser) -> IUser:
        try:    
            spotify_auth = SpotifyAuth()
            access_token, refresh_token = spotify_auth.refresh_access_token(cast(str, user.refresh_token))
            
            user.access_token = access_token
            UserTokenManager.set_access_token(user.id, user.access_token)
        
            if refresh_token:
                user.refresh_token = refresh_token
                UserTokenManager.set_refresh_token(user.id, user.refresh_token)
           
            return user
        except Exception as e:
            raise Exception(f"Failed to refresh access token: {e}")

    def _parse_top_tracks(self, data) -> List[TopTracksType]:
        result = []
        for track in data.get('items', []):
            result.append({'name': track.get('name'), 'artist': track.get('artists')[0].get('name'), 'song_link': track.get('external_urls').get('spotify')})
        return result
    
    def _parse_top_artists(self, data) -> List[TopArtistsType]:
        result = []
        for track in data.get('items', []):
            result.append({'name': track.get('name'), 'artist_link': track.get('external_urls').get('spotify')})
        return result