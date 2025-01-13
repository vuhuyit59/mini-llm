import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from backend import responses
from backend.constant import DEFAULT_PAGE_SIZE
from backend.core import get_session
from backend.models import AiVideoRequestModel
from backend.queries import ai_video_request as ai_video_qr
from backend.serializers.ai_video_request import \
    AiVideoRequestSerializer, AiVideoRequestDetailSerializer
from backend.services.rabbit.producer.request_create_ai_video_producer import \
    RequestCreateAiVideoProducer
from backend.services.rabbit.rabbit_service import RabbitMQService

logger = logging.getLogger(__name__)

router = APIRouter()

__all__ = ['router']


@router.get("/list",
            response_model=responses.SuccessPagingResponseModel[
                List[AiVideoRequestSerializer]])
async def get_ai_video_request_list_api(
        session: AsyncSession = Depends(get_session),
        page: int = 1,
        page_size: int = DEFAULT_PAGE_SIZE,
        *,
        user_id: str,
):
    total, ai_video_requests = await ai_video_qr.get_list(
        session=session,
        page_size=page_size,
        page=page,
        user_id=user_id,
    )
    return responses.response_page_success(
        data=[AiVideoRequestDetailSerializer.from_orm(
            prompt_request).dict()
              for
              prompt_request in ai_video_requests],
        total=total,
        page=page, page_size=page_size)


@router.get("/{request_id}",
            response_model=responses.SuccessResponseModel[
                AiVideoRequestDetailSerializer])
async def get_ai_video_request_detail_api(
        session: AsyncSession = Depends(get_session),
        *,
        request_id: str,
        user_id: str,
):
    ai_video_request_obj: AiVideoRequestModel or None = await ai_video_qr.get_detail(
        session=session,
        user_id=user_id,
        request_id=request_id
    )
    if not ai_video_request_obj:
        return responses.response_failed(
            error=['Prompt request not found'],
            status_code=404,
            code=404
        )
    return responses.response_success(
        data=AiVideoRequestDetailSerializer.from_orm(
            ai_video_request_obj).dict()
    )


@router.post("",
             response_model=responses.SuccessResponseModel[
                 AiVideoRequestDetailSerializer])
async def create_ai_video_request_api(
        session: AsyncSession = Depends(get_session),
        *,
        request_data: AiVideoRequestSerializer
):
    try:
        func_name = create_ai_video_request_api.__name__
        print(f'{func_name}: get request data [{request_data}]')
        if not request_data.input_sample or request_data.input_sample is None:
            return responses.response_failed(
                error=['Invalid input sample'],
                status_code=500,
                code=500
            )
        ai_video_request: AiVideoRequestModel = await ai_video_qr.create(
            session=session, value=request_data)
        if not ai_video_request:
            return responses.response_failed(
                message='Create failed',
                code=500, status_code=500
            )
        data_to_send = dict(
            user_id=ai_video_request.user_id,
            request_id=ai_video_request.id
        )
        rabbit_client = RequestCreateAiVideoProducer.get_instance()
        RabbitMQService.basic_publish(
            self=rabbit_client,
            body=data_to_send,
            routing_key=RequestCreateAiVideoProducer.get_produce_endpoint(),
        )
        return responses.response_success(
            data=AiVideoRequestDetailSerializer.from_orm(
                ai_video_request).dict()
        )
    except Exception as e:
        print("api failed", e)
        return responses.response_failed(
            message='Some thing went wrong',
            code=500, status_code=500
        )
