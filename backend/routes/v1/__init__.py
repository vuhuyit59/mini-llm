from fastapi import APIRouter
from .ai_video_request import router as ai_video_request_router

router = APIRouter()

router.include_router(
    ai_video_request_router, prefix='/ai_video_request',
    tags=['ai_video_request']
)
