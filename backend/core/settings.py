from pydantic import BaseSettings


class SettingsClass(BaseSettings):
    API_SECRET: str = ""

    # Database
    DATABASE_URI: str = ""
    DATABASE_ECHO: bool = False

    # Rabbit
    RABBITMQ_USER: str = ""
    RABBITMQ_PASS: str = ""
    RABBITMQ_HOST_NAME: str = ""
    RABBITMQ_PORT: int = 5671
    RABBITMQ_V_HOST: str = ""

    REQUEST_CREATE_AI_VIDEO_QUEUE_NAME: str = "create_ai_video_queue"
    BYTE_SCALE_API_KEY: str = ""
    BYTE_SCALE_ACCOUNT_ID: str = ""


def get_settings():
    return SettingsClass()


settings: SettingsClass = get_settings()
