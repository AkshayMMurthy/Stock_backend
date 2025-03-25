import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
