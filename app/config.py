import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL= os.getenv("QDRANT_URL")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

REDIS_HOST= os.getenv("REDIS_HOST")
REDIS_PORT= int(os.getenv("REDIS_PORT",6379))
