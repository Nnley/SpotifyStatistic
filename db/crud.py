from db.database import Session
from db.models import User
from db.types import IUser, TopTracksType

from typing import Optional, List


class UserNotFoundError(Exception):
    pass


class UserRepository:
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[IUser ]:
        with Session() as session:
            user = session.query(User).filter_by(id=user_id).first()
            return user 

    @staticmethod
    def get_user_or_raise(user_id: int) -> IUser:
        user = UserRepository.get_user_by_id(user_id)
        if user is None:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        return user

    @staticmethod
    def add_user(user: IUser) -> None:
        with Session() as session:
            session.add(user)
            session.commit()

    @staticmethod
    def update_user(user: IUser) -> None:
        with Session() as session:
            session.merge(user)
            session.commit()


class UserManager:
    @staticmethod
    def get_or_create_user(user_id: int) -> IUser:
        user_repository = UserRepository()
        user = user_repository.get_user_by_id(user_id) 
        if user is None:
            user = User(id=user_id)
            user_repository.add_user(user)
        return user


class UserTokenManager:
    @staticmethod
    def get_access_token(user_id: int) -> Optional[str]:
        user = UserRepository.get_user_or_raise(user_id)
        if user.access_token:
            return user.access_token
        return None

    @staticmethod
    def get_refresh_token(user_id: int) -> Optional[str]:
        user = UserRepository.get_user_or_raise(user_id)
        if user.refresh_token:
            return user.refresh_token
        return None
    
    @staticmethod
    def set_access_token(user_id: int, access_token: str) -> IUser:
        user = UserRepository.get_user_or_raise(user_id)
        user.access_token = access_token
        UserRepository.update_user(user)
        return user
    
    @staticmethod
    def set_refresh_token(user_id: int, refresh_token: str) -> IUser:
        user = UserRepository.get_user_or_raise(user_id)
        user.refresh_token = refresh_token
        UserRepository.update_user(user)
        return user
    

class UserTrackManager:
    @staticmethod
    def get_top_tracks_month(user_id: int) -> Optional[List[TopTracksType]]:
        user = UserRepository.get_user_or_raise(user_id)
        if user.top_tracks_month:
            return user.top_tracks_month
        else:
            return None
    
    @staticmethod
    def get_top_tracks_half_year(user_id: int) -> Optional[List[TopTracksType]]:
        user = UserRepository.get_user_or_raise(user_id)
        if user.top_tracks_half_year:
            return user.top_tracks_half_year
        else:
            return None

    @staticmethod    
    def get_top_tracks_year(user_id: int) -> Optional[List[TopTracksType]]:
        user = UserRepository.get_user_or_raise(user_id)
        if user.top_tracks_year:
            return user.top_tracks_year
        else:
            return None

    @staticmethod    
    def set_top_tracks_month(user_id: int, top_tracks_month: List[TopTracksType]) -> IUser:
        user = UserRepository.get_user_or_raise(user_id)
        user.top_tracks_month = top_tracks_month
        UserRepository.update_user(user)
        return user

    @staticmethod   
    def set_top_tracks_half_year(user_id: int, top_tracks_half_year: List[TopTracksType]) -> IUser: 
        user = UserRepository.get_user_or_raise(user_id)
        user.top_tracks_half_year = top_tracks_half_year
        UserRepository.update_user(user)
        return user

    @staticmethod
    def set_top_tracks_year(user_id: int, top_tracks_year: List[TopTracksType]) -> IUser:
        user = UserRepository.get_user_or_raise(user_id)
        user.top_tracks_year = top_tracks_year
        UserRepository.update_user(user)
        return user