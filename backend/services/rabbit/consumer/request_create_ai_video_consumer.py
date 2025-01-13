import json
import logging

from backend.core import settings
from backend.core.database import get_session, async_session
from backend.queries.ai_video_request import get_detail
from backend.services.ai_video import create_ai_video

from backend.services.rabbit.rabbit_connection_holder import \
    RabbitMQConnectionHolder
from backend.utils import run_async_from_sync

logger = logging.getLogger(__name__)


class RequestCreateAiVideoConsumer(RabbitMQConnectionHolder):
    __instance = None

    @staticmethod
    def get_produce_endpoint():
        return settings.REQUEST_CREATE_AI_VIDEO_QUEUE_NAME

    @staticmethod
    def get_instance():
        if RequestCreateAiVideoConsumer.__instance is None:
            RequestCreateAiVideoConsumer()
        instance = RequestCreateAiVideoConsumer.__instance
        if instance.channel.is_closed or instance.channel.connection.is_closed:
            RabbitMQConnectionHolder.connect(instance)
            instance.channel = instance.connection.channel()
            RequestCreateAiVideoConsumer.__instance = instance
            return RequestCreateAiVideoConsumer.__instance
        else:
            return RequestCreateAiVideoConsumer.__instance

    def handler_reply_msg(self, ch, method, properties, body):
        self.response = json.loads(body.decode("utf-8"))
        run_async_from_sync(self.handle_create_ai_video, **self.response)

    async def handle_create_ai_video(self, **kwargs):
        async with async_session() as session:
            obj = await get_detail(session=session,
                                   user_id=kwargs.get("user_id"),
                                   request_id=kwargs.get("request_id"))
            await create_ai_video(obj, session)



    def __init__(self):
        if RequestCreateAiVideoConsumer.__instance is None:
            logger.info("RequestCreateAiVideoConsumer init")
            RabbitMQConnectionHolder.__init__(self)
            self.response = None
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.get_produce_endpoint())
            self.channel.basic_consume(
                queue=self.get_produce_endpoint(),
                on_message_callback=self.handler_reply_msg,
                auto_ack=True)
            self.channel.start_consuming()
            RequestCreateAiVideoConsumer.__instance = self
