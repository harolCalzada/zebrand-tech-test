from redis import Redis
from django.conf import settings


def redis_client():
    return Redis.from_url(settings.REDIS_URL)
