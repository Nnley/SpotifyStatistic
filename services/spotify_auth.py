import os
import urllib.parse
import requests
from db.crud import get_user

from config import load_environment_variables
load_environment_variables()


client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = 'user-read-private user-top-read'
token_url = 'https://accounts.spotify.com/api/token'
auth_url = 'https://accounts.spotify.com/authorize'


# TODO: сделать с помощью классов, перепроектировать под SOLID
def generate_auth_link(state):
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': scope,
        'state': state
    }

    return f"{auth_url}?{urllib.parse.urlencode(params)}"

def get_access_token(code):
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_url, data=payload)

    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info.get("access_token")
        refresh_token = token_info.get("refresh_token")

        # TODO: Hash refresh_token
        return access_token, refresh_token
    else:
        print('Access token error: ', response.json())
        raise Exception(response.json())

def refresh_access_token(user_id):
    user = get_user(user_id)
    if not user or user.refresh_token is None:
        return Exception("Refresh token not found")
    
    # TODO: Hash refresh_token
    refresh_token = user.refresh_token

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(token_url, data=payload)

    if response.status_code == 200:
        token_info = response.json()
        new_access_token = token_info.get("access_token")
        
        
        return new_access_token
    else:
        print('Refresh token error: ', response.json())
        raise Exception(response.json())
    