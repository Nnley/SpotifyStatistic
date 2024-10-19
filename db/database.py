import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

from config import load_environment_variables
load_environment_variables()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)