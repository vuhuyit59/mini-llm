from enum import Enum

from sqlalchemy import Column, Text, String, Integer, DateTime, func
from backend.core import BaseModel
import uuid as uuid_pkg

__all__ = ['AiVideoRequestModel', 'AiVideoRequestStatusOptions']


class AiVideoRequestStatusOptions(str, Enum):
    PROCESSING = 'PROCESSING'
    FINISHED = 'FINISHED'
    FAILED = 'FAILED'

    @classmethod
    def list(cls) -> list[str]:
        return list(map(lambda c: c.value, cls))


def gen_uuid():
    return str(uuid_pkg.uuid4())


class AiVideoRequestModel(BaseModel):
    __tablename__ = "ai_video_request"

    id = Column(
        String(length=64),
        primary_key=True,
        nullable=False,
        default=gen_uuid,
    )
    status = Column(String(length=50), nullable=False,
                    default=AiVideoRequestStatusOptions.PROCESSING)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    input_sample = Column(Text, nullable=False)
    user_id = Column(Text, nullable=False)
    narration = Column(Text, nullable=True)
    output_video_url = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)
    process_percent = Column(Integer, nullable=False, default=0)
