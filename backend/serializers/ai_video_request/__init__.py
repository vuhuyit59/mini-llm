from pydantic import BaseModel

from backend.models import AiVideoRequestStatusOptions
from typing import Optional

__all__ = ['AiVideoRequestDetailSerializer',
           'AiVideoRequestSerializer']


class AiVideoRequestDetailSerializer(BaseModel):
    id: str
    status: AiVideoRequestStatusOptions
    input_sample: str
    output_video_url: Optional[str]
    image_url: Optional[str]
    process_percent: int

    class Config:
        orm_mode = True


class AiVideoRequestSerializer(BaseModel):
    input_sample: str
    user_id: str

    class Config:
        orm_mode = True
