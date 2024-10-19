from flask import Flask, request, redirect, session
import os
import uuid

from db.crud import get_user, update_user
from services.spotify_auth import generate_auth_link, get_access_token

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
    
    user = get_user(user_id)
    if user is None:
        return 'User not found', 404
    
    try:
        access_token, refresh_token = get_access_token(code)
        update_user(user_id, access_token, refresh_token)
    except Exception as e:
        return f'Failed to get access token: {e}', 500

    return redirect('https://t.me/SpotifyStatisticBot?start=success')

@app.route('/auth/<user_id>')
def handle_auth(user_id):
    session['user_id'] = user_id

    state = str(uuid.uuid4())
    session['state'] = state
    
    return redirect(generate_auth_link(state))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)