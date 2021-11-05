from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Optional, Union
import aiohttp

import xmltodict

from constants import BASE_URL
from models import (
    Stats,
    Creature
)

if TYPE_CHECKING:
    from models import ModelType


class SporeClient():
    def __init__(self) -> None:
        self.BASE_URL = BASE_URL
        self._decoder: Callable[[str], dict[str, Any]] = xmltodict.parse

    async def create(self, session: Optional[aiohttp.ClientSession]) -> None:
        self._session = session

    async def __aenter__(self, session: Optional[aiohttp.ClientSession] = None):
        if session is None:
            session = aiohttp.ClientSession()

        await self.create(session)
        return self

    async def get_stats(self) -> Stats:
        return await self.request(f"{self.BASE_URL}/rest/stats", Stats)

    async def get_creature(self, creature_id: Union[int, str]) -> Creature:
        return await self.request(
            f"{self.BASE_URL}rest/creature/{creature_id}", Creature
        )

    async def request(self, url: str, model: type["ModelType"]) -> "ModelType":
        if self._session is None:
            raise ValueError("The session does not exist")

        async with self._session.get(url) as responce:
            responce.raise_for_status()

            return model.from_dict(  # TODO: +метод
                self._decoder(await responce.text())
            )

    async def close(self) -> None:
        if self._session is None:
            raise ValueError("The session does not exist")

        await self._session.close()

    async def __aexit__(
        self,
        _exception_type: type[BaseException],
        _exception: BaseException,
        _traceback: TracebackType
    ) -> None:
        await self.close()
