from db.database import Session
from db.models import User

session = Session()

def get_or_create_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    
    if user is None:
        user = User(id=user_id)
        session.add(user)
        session.commit()
    
    return user

def get_user(user_id):
    return session.query(User).filter_by(id=user_id).first()

def update_user(user_id, access_token=None, refresh_token=None, top_tracks=None):
    user = get_user(user_id)
    if user:
        if access_token is not None:
            user.access_token = access_token
        if refresh_token is not None:
            user.refresh_token = refresh_token
        if top_tracks is not None:
            user.top_tracks = top_tracks
        session.commit()
    return user