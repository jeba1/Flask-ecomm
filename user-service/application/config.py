import os
from dotenv import load_dotenv

dot_env_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dot_env_path):
    load_dotenv(dot_env_path)

class Config:
    SECRET_KEY= "HxJT8mUNljVqoCp5NUciZQ"
    SQLACHEMY_TRACK_MODIFICATIONS= False

class Developpement(Config):
    ENV = 'developement'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin123@localhost:5433/user_dev"
    


