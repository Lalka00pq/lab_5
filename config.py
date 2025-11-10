import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.environ.get("BASE_URL")
