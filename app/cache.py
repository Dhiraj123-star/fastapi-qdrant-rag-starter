import redis
from app.config import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

def get_cache(key:str):
    return redis_client.get(key)

def set_cache(key:str, value:str, ttl:int=300):
    redis_client.setex(key,ttl,value)
