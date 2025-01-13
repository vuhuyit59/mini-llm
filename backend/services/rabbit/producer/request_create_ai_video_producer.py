import json
import logging

from backend.core import settings

from backend.services.rabbit.rabbit_connection_holder import \
    RabbitMQConnectionHolder

logger = logging.getLogger(__name__)


class RequestCreateAiVideoProducer(RabbitMQConnectionHolder):
    __instance = None

    @staticmethod
    def get_produce_endpoint():
        return settings.REQUEST_CREATE_AI_VIDEO_QUEUE_NAME

    @staticmethod
    def get_instance():
        if RequestCreateAiVideoProducer.__instance is None:
            RequestCreateAiVideoProducer()
        instance = RequestCreateAiVideoProducer.__instance
        if instance.channel.is_closed or instance.channel.connection.is_closed:
            RabbitMQConnectionHolder.connect(instance)
            instance.channel = instance.connection.channel()
            RequestCreateAiVideoProducer.__instance = instance
            return RequestCreateAiVideoProducer.__instance
        else:
            return RequestCreateAiVideoProducer.__instance

    def handler_reply_msg(self, ch, method, properties, body):
        self.response = json.loads(body.decode("utf-8"))

    def __init__(self):
        if RequestCreateAiVideoProducer.__instance is None:
            logger.info("RequestCreateAiVideoProducer init")
            RabbitMQConnectionHolder.__init__(self)
            self.response = None
            self.channel = self.connection.channel()
            self.reply_queue = self.channel.queue_declare(queue="",
                                                          auto_delete=True)
            self.channel.queue_declare(queue=self.get_produce_endpoint())
            RequestCreateAiVideoProducer.__instance = self
