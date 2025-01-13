from sqlalchemy import Select, select, desc, ChunkedIteratorResult, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from backend.constant import DEFAULT_PAGE_SIZE
from backend.models import AiVideoRequestModel
from backend.serializers import AiVideoRequestSerializer


async def get_list(session: AsyncSession, user_id: str, page: int = 1,
                   page_size: int = DEFAULT_PAGE_SIZE) -> (
        int, [AiVideoRequestModel]):
    query: Select = select(AiVideoRequestModel).filter(
        AiVideoRequestModel.user_id == user_id,
    ).order_by(desc(AiVideoRequestModel.updated_at))
    query_count: Select = select(
        func.count(AiVideoRequestModel.id),
    ).filter(
        AiVideoRequestModel.user_id == user_id,
    )
    execution_count: ChunkedIteratorResult = await session.execute(query_count)
    execution: ChunkedIteratorResult = await session.execute(
        query.offset((page - 1) * page_size).limit(page_size)
    )
    return execution_count.scalar_one(), execution.scalars().all()


async def get_detail(session: AsyncSession,
                     user_id: str,
                     request_id: str) -> AiVideoRequestModel or None:
    query: Select = select(AiVideoRequestModel).filter(
        AiVideoRequestModel.user_id == user_id,
        AiVideoRequestModel.id == request_id,
    )
    try:
        execution: ChunkedIteratorResult = await session.execute(query)
        ai_video_request = execution.scalar_one()
        return ai_video_request
    except Exception:
        return None


async def create(
        session: AsyncSession,
        value: AiVideoRequestSerializer
) -> AiVideoRequestModel:
    new_record: AiVideoRequestModel = AiVideoRequestModel(
        **value.dict())
    session.add(new_record)
    await session.flush()
    return new_record

