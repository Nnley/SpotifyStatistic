from db.crud import update_user, get_user
from services.spotify_auth import refresh_access_token
import requests

def get_user_top_tracks(user_id):
    user = get_user(user_id)
    result = []
    
    if user and user.access_token is None:
        return

    status_code, data = request_top_tracks(user.access_token) # type: ignore
    
    if status_code == 401:
        user.access_token = refresh_access_token(user.id) # type: ignore
        status_code, data = request_top_tracks(user.access_token) # type: ignore
        update_user(user.id, user.access_token) # type: ignore
    
    for track in data.get('items'):
        result.append({'name': track.get('name'), 'artist': {track.get('artists')[0].get('name')} })
    
    return result

def request_top_tracks(access_token):
    response = requests.get('https://api.spotify.com/v1/me/top/tracks?limit=10?time_range=short_term', headers={
                'Authorization': f'Bearer {access_token}'
            })
    return response.status_code, response.json()