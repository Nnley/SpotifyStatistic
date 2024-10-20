from db.database import Session
from db.models import User
from db.types import IUser, TopTracksType

from typing import Optional, List


class UserNotFoundError(Exception):
    pass


class UserRepository:
    def get_user_by_id(self, user_id: int) -> Optional[IUser ]:
        with Session() as session:
            user = session.query(User).filter_by(id=user_id).first()
            return user 
    
    def get_user_or_raise(self, user_id: int) -> IUser:
        user = self.get_user_by_id(user_id)
        if user is None:
            raise UserNotFoundError(f"User  with ID {user_id} not found.")
        return user

    def add_user(self, user: IUser) -> None:
        with Session() as session:
            session.add(user)
            session.commit()

    def update_user(self, user: IUser) -> None:
        with Session() as session:
            session.merge(user)
            session.commit()


class UserManager:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_or_create_user(self, user_id: int) -> IUser:
        user = self.user_repository.get_user_by_id(user_id) 
        if user is None:
            user = User(id=user_id)
            self.user_repository.add_user(user)
        return user


class UserTokenManager: 
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
    
    def get_access_token(self, user_id: int) -> Optional[str]:
        user = self.user_repository.get_user_or_raise(user_id)
        if user.access_token:
            return user.access_token
        return None

    def get_refresh_token(self, user_id: int) -> Optional[str]:
        user = self.user_repository.get_user_or_raise(user_id)
        if user.refresh_token:
            return user.refresh_token
        return None
    
    def set_access_token(self, user_id: int, access_token: str) -> Optional[IUser]:
        user = self.user_repository.get_user_or_raise(user_id)
        user.access_token = access_token
        self.user_repository.update_user(user)
        return user
    
    def set_refresh_token(self, user_id: int, refresh_token: str) -> Optional[IUser]:
        user = self.user_repository.get_user_or_raise(user_id)
        user.refresh_token = refresh_token
        self.user_repository.update_user(user)
        return user
    

class UserTrackManager:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
    
    def get_top_tracks_month(self, user_id: int) -> Optional[List[TopTracksType]]:
        user = self.user_repository.get_user_or_raise(user_id)
        if user.top_tracks_month:
            return user.top_tracks_month
        else:
            return None
    
    def get_top_tracks_half_year(self, user_id: int) -> Optional[List[TopTracksType]]:
        user = self.user_repository.get_user_or_raise(user_id)
        if user.top_tracks_half_year:
            return user.top_tracks_half_year
        else:
            return None
    
    def get_top_tracks_year(self, user_id: int) -> Optional[List[TopTracksType]]:
        user = self.user_repository.get_user_or_raise(user_id)
        if user.top_tracks_year:
            return user.top_tracks_year
        else:
            return None
    
    def set_top_tracks_month(self, user_id: int, top_tracks_month: List[TopTracksType]) -> IUser:
        user = self.user_repository.get_user_or_raise(user_id)
        user.top_tracks_month = top_tracks_month
        self.user_repository.update_user(user)
        return user
    
    def set_top_tracks_half_year(self, user_id: int, top_tracks_half_year: List[TopTracksType]) -> IUser: 
        user = self.user_repository.get_user_or_raise(user_id)
        user.top_tracks_half_year = top_tracks_half_year
        self.user_repository.update_user(user)
        return user

    def set_top_tracks_year(self, user_id: int, top_tracks_year: List[TopTracksType]) -> IUser:
        user = self.user_repository.get_user_or_raise(user_id)
        user.top_tracks_year = top_tracks_year
        self.user_repository.update_user(user)
        return user