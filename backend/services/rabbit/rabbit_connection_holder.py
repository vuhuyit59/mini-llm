import logging
import uuid

import pika
from backend.core import settings

credentials = pika.PlainCredentials(
    username=settings.RABBITMQ_USER, password=settings.RABBITMQ_PASS
)

logger = logging.getLogger(__name__)


class RabbitMQConnectionHolder(object):
    def __init__(self):
        self.corr_id = str(uuid.uuid4())
        RabbitMQConnectionHolder.connect(instance=self)
        self.response = None
        RabbitMQConnectionHolder.__instance = self

    @staticmethod
    def connect(instance):
        instance.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST_NAME,
                port=settings.RABBITMQ_PORT,
                # virtual_host=settings.RABBITMQ_V_HOST,
                credentials=credentials,
                heartbeat=5,
                # blocked_connection_timeout=300,
                connection_attempts=3,
            )
        )
