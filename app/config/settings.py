from dotenv import load_dotenv
import os

load_dotenv()

# Allowed origins for CORS (configurable via .env as comma-separated list)
ALLOWED_ORIGINS_STR = os.getenv("ALLOWED_ORIGINS", "http://localhost:4321,https://chrisandsonsllc.com,https://chris.gorombo.com")
ALLOWED_ORIGINS = [origin.strip() for origin in ALLOWED_ORIGINS_STR.split(",")]
