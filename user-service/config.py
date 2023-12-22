import os
from dotenv import load_dotenv

dot_env_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dot_env_path):
    load_dotenv(dot_env_path)

class Config:
