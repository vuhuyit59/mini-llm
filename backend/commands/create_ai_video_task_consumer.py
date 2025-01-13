import logging
from typer import Typer
from backend.commands.helper import async_command
from backend.services.rabbit.consumer.request_create_ai_video_consumer import \
    RequestCreateAiVideoConsumer

app: Typer = Typer()
logger = logging.getLogger(__name__)


@async_command(app=app)
async def create_ai_video_task():
    print('Start create_ai_video_task')
    RequestCreateAiVideoConsumer()

if __name__ == "__main__":
    app()