import random
import string

from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.dependencies import get_session
from models import URLModel


class URLService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.__session = session

    async def shorten_url(self, long_url: str) -> str:
        short_url = self.generate_short_url()
        url_model = URLModel(long_url=str(long_url), short_url=short_url)
        self.__session.add(url_model)
        await self.__session.commit()
        return short_url

    async def get_by_short_url(self, short_url: str) -> URLModel:
        result = await self.__session.execute(select(URLModel).where(URLModel.short_url == short_url))
        return result.scalars().first()

    @staticmethod
    def generate_short_url(length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


