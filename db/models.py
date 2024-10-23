from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


# TODO: Rewrite the database, split the user table into other tables
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    
    access_token = Column(String, nullable=True) 
    refresh_token = Column(String, nullable=True)
    
    top_tracks_month = Column(JSON, nullable=True)
    top_tracks_half_year = Column(JSON, nullable=True)
    top_tracks_year = Column(JSON, nullable=True)
    
    top_artists_month = Column(JSON, nullable=True)
    top_artists_half_year = Column(JSON, nullable=True)
    top_artists_year = Column(JSON, nullable=True)
    
    display_name = Column(String, nullable=True)
    country = Column(String, nullable=True)
    language_code = Column(String, default='en')
    
    created_at = Column(DateTime, default=func.now())   
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now()) 
    
    authorization_code = relationship("AuthorizationCode", back_populates="user", uselist=False)


class AuthorizationCode(Base):
    __tablename__ = 'authorization_code'
    
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="authorization_code")