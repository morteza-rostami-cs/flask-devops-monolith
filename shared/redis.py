import redis

from shared.settings import settings

# redis client
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    # recode redis response
    decode_responses=True,
)
