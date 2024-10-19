from db.crud import update_user, get_user
from services.spotify_auth import refresh_access_token
import requests
from enum import Enum

class TimeRange(Enum):
    SHORT_TERM = 'short_term'
    MEDIUM_TERM = 'medium_term'

def get_user_top_tracks(user_id, time_range=TimeRange.SHORT_TERM):
    user = get_user(user_id)
    result = []
    
    if user and user.access_token is None:
        return

    status_code, data = request_top_tracks(user.access_token, time_range) # type: ignore
    
    if status_code == 401:
        try: 
            user.access_token = refresh_access_token(user.id) # type: ignore
            user = update_user(user.id, user.access_token) # type: ignore
            status_code, data = request_top_tracks(user.access_token, time_range) # type: ignore
        except Exception as e:
            print(e)
            return
    
    if status_code != 200:
        print(data, status_code)
        return
    
    for track in data.get('items'):
        result.append({'name': track.get('name'), 'artist': track.get('artists')[0].get('name') })
    
    return result

def request_top_tracks(access_token, time_range):
    response = requests.get(f'https://api.spotify.com/v1/me/top/tracks?limit=10&time_range={time_range}', headers={
                'Authorization': f'Bearer {access_token}'
            })
    return response.status_code, response.json()

def request_get_user_profile(access_token):
    response = requests.get('https://api.spotify.com/v1/me', headers={
            'Authorization': f'Bearer {access_token}'  # type: ignore
            })
    return response.status_code, response.json()

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