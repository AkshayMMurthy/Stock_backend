import os
#We are fetching the api key stored in the environment variable file .env
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY") 

if GOOGLE_API_KEY is None:
    raise ValueError("GOOGLE_API_KEY is not set in environment variables")
