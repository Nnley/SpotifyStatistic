import os
import urllib.parse
import requests
import json
import base64

from config import load_environment_variables
load_environment_variables()


class NotAuthorizedError(Exception):
    pass


class SpotifyAuth:
    def __init__(self):
        self.client_id =os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("REDIRECT_URI")
        self.scope = 'user-read-private user-top-read'
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.auth_url = 'https://accounts.spotify.com/authorize'

    def generate_auth_link(self, state: str) -> str:
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'state': state
        }
        
        return f"{self.auth_url}?{urllib.parse.urlencode(params)}"

    def get_access_refresh_tokens(self, code: str) -> tuple[str, str]:
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'client_secret': self.client_secret
        }

        response = requests.post(self.token_url, data=payload)

        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info.get("access_token")
            refresh_token = token_info.get("refresh_token")

            return access_token, refresh_token
        else:
            raise Exception('Get tokens error: ' + response.json() + '\nRespose status code:' + response.status_code)

    def refresh_access_token(self, refresh_token: str) -> str | tuple[str, str]:
        client_creds = f"{self.client_id}:{self.client_secret}"
        encoded_creds = base64.b64encode(client_creds.encode()).decode()

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {encoded_creds}'
        }

        response = requests.post(self.token_url, headers=headers, data=payload)

        if response.status_code == 200:
            token_info = response.json()
            new_refresh_token = token_info.get("refresh_token", refresh_token)
            new_access_token = token_info.get("access_token")

            return new_access_token, new_refresh_token
        else:
            error_message = json.dumps(response.json())
            raise Exception('Refresh token error: ' + error_message + '\nResponse status code: ' + str(response.status_code))