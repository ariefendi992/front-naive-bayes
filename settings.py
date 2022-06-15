import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    SECRET_KEY = str(os.getenv('secret_key'))
