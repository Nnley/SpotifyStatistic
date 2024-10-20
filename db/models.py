from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    access_token = Column(String, nullable=True) 
    refresh_token = Column(String, nullable=True)
    top_tracks_month = Column(JSON, nullable=True)
    top_tracks_half_year = Column(JSON, nullable=True)
    top_tracks_year = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=func.now())   
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now()) 