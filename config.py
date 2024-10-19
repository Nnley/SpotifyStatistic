from dotenv import load_dotenv
from pathlib import Path

def load_environment_variables():
    dotenv_path = Path('.env.local')
    load_dotenv(dotenv_path=dotenv_path)

load_environment_variables()