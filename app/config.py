import os

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # ✅ Directly fetches from Render's environment variables

if GOOGLE_API_KEY is None:
    raise ValueError("GOOGLE_API_KEY is not set in environment variables")
