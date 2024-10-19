from dotenv import load_dotenv
from pathlib import Path
import os

def load_environment_variables():
    dotenv_path = Path('SpotifyStats/.env.local')
    load_dotenv(dotenv_path=dotenv_path)

load_environment_variables()