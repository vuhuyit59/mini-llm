from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from backend.core.settings import settings

engine = create_async_engine(settings.DATABASE_URI, future=True,
                             echo=settings.DATABASE_ECHO)
async_session: AsyncSession = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
BaseModel = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.commit()
