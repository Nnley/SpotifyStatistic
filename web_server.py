from flask import Flask, request, redirect, session

import os
import uuid
from datetime import datetime

from db.crud import UserRepository, AuthorizationCodeManager, UserNotFoundError
from services.spotify_auth import SpotifyAuth

from config import load_environment_variables
load_environment_variables()


app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SERCET')


@app.route('/callback')
def handle_redirect():
    if request.args.get('state') != session['state']:
        return 'State mismatch error', 400

    code = request.args.get('code')
    if not code:
        return 'No code provided', 400

    user_id = session.get('user_id')
    if user_id is None:
        return 'No user_id in session', 400
    
    user = UserRepository.get_user_by_id(user_id)
    if user is None:
        return 'User not found', 404
    
    try:
        spotify_auth = SpotifyAuth()
        user.access_token, user.refresh_token = spotify_auth.get_access_refresh_tokens(code)
        UserRepository.update_user(user)
    except Exception as e:
        return f'Failed to get access token: {e}', 500

    return redirect('https://t.me/SpotifyStatisticBot?start=success')

@app.route('/auth/<code>')
def handle_auth(code):
    try:
        user = AuthorizationCodeManager.get_user_by_code(code)
    except UserNotFoundError as e:
        return str(e), 404

    if user.authorization_code and user.authorization_code.expires_at < datetime.utcnow():
        return 'Authorization code expired', 400

    session['user_id'] = user.id

    state = str(uuid.uuid4())
    session['state'] = state
    
    return redirect('')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)