from typing import Callable, Any, Tuple
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import HTTPException

from models import AbstractModel
from core.config import settings


class AbstractDataBase:
    engine = create_async_engine(settings.DATABASE_URL, echo=True) 
    session = async_sessionmaker(engine)

    @classmethod
    async def run_metadata_method(cls, method: str) -> None:
        if not hasattr(AbstractModel.metadata, method):
            raise HTTPException(status_code=500, detail=f"Method '{method}' not found.")

        async with cls.engine.connect() as connection:
            await connection.run_sync(
                getattr(AbstractModel.metadata, method)
            )
    
    @classmethod
    async def run_in_session(
        cls, func: Callable[[AsyncSession, Any], Any], *args, **kwargs
    ) -> Any:
        async with cls.session() as session:
            if asyncio.iscoroutinefunction(func):     
                returning = await func(session, *args, **kwargs)
            else:
                returning = func(session, *args, **kwargs) 

            return returning
    
    @classmethod
    async def run_in_session_with_commit(
        cls, func: Callable[[AsyncSession, Any], Any], *args, **kwargs
    ) -> Any:
        async def inner(session: AsyncSession, *args, **kwargs) -> None:
            async with session.begin():
                returning = await func(session, *args, **kwargs)
            
            return returning
        
        return await cls.run_in_session(inner, *args, **kwargs) 
            
    @classmethod
    async def create_all_tables(cls) -> None:
        await cls.run_metadata_method("create_all")

    @classmethod
    async def drop_all_tables(cls) -> None:
        await cls.run_metadata_method("drop_all")
