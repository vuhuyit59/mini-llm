from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.ai_video.create_content import create_content_file
from backend.services.ai_video.create_video import create_video
from backend.models import AiVideoRequestModel, AiVideoRequestStatusOptions


async def create_ai_video(ai_video_request: AiVideoRequestModel,
                    session: AsyncSession):
    image_file_list, voice_file_list = await create_content_file(
        ai_video_request, session)
    ai_video_request.process_percent = 60
    await session.commit()
    video_url = create_video(image_file_list, voice_file_list)
    if video_url:
        ai_video_request.process_percent = 100
        ai_video_request.output_video_url = video_url
        ai_video_request.status = AiVideoRequestStatusOptions.FINISHED
        await session.commit()
    else:
        ai_video_request.status = AiVideoRequestStatusOptions.FAILED
        await session.commit()
    return
