from db.database import Session
from db.models import User

class UserRepository:
    def get_user_by_id(self, user_id):
        with Session() as session:
            return session.query(User).filter_by(id=user_id).first()

    def add_user(self, user):
        with Session() as session:
            session.add(user)
            session.commit()

    def update_user(self, user):
        with Session() as session:
            session.merge(user)
            session.commit()


class UserManager:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_or_create_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        
        if user is None:
            user = User(id=user_id)
            self.user_repository.add_user(user)
        
        return user


class UserTokenManager: 
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def get_access_token(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return user.access_token
        return None

    def get_refresh_token(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return user.refresh_token
        return None
    
    def set_access_token(self, user_id, access_token):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.access_token = access_token
            self.user_repository.update_user(user)
        return user
    
    def set_refresh_token(self, user_id, refresh_token):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.refresh_token = refresh_token
            self.user_repository.update_user(user)
        return user
    

class UserTrackManager:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def get_top_tracks_month(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return user.top_tracks_month
        else:
            return None
    
    def get_top_tracks_half_year(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return user.top_tracks_half_year
        else:
            return None
    
    def get_top_tracks_year(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return user.top_tracks_year
        else:
            return None
    
    def set_top_tracks_month(self, user_id, top_tracks_month):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.top_tracks_month = top_tracks_month
            self.user_repository.update_user(user)
        return user
    
    def set_top_tracks_half_year(self, user_id, top_tracks_half_year):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.top_tracks_half_year = top_tracks_half_year
            self.user_repository.update_user(user)
        return user

    def set_top_tracks_year(self, user_id, top_tracks_year):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.top_tracks_year = top_tracks_year
            self.user_repository.update_user(user)
        return user