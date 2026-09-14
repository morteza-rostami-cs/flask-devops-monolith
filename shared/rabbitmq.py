import pika

from shared.settings import settings


def get_connection():
    """return a rabbitmq connection"""
    return pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
