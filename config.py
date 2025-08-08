from dotenv import load_dotenv
from os import getenv

load_dotenv()

BASE_URL = getenv("BASE_URL")
API_KEY = getenv("API_KEY")
MODEL_NAME = getenv("MODEL_NAME")
