from dataclasses import dataclass
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Optional, Type, Union

import aiohttp
import xmltodict

from .constants import BASE_URL
from .abc import ABCBuilder
from .builders import (
    StatsJsonBuilder,
    CreatureJsonBuilder
)

if TYPE_CHECKING:
    from .models import (
        Stats,
        Creature
    )


@dataclass
class Builders():
    stats: ABCBuilder
    creature: ABCBuilder


class SporeClient():
    def __init__(self) -> None:
        self._base_url = BASE_URL
        self._decoder: Callable[[str], dict[str, Any]] = xmltodict.parse

        self._builders = Builders(
            stats=StatsJsonBuilder(),
            creature=CreatureJsonBuilder()
        )

    async def create(self, session: Optional[aiohttp.ClientSession]) -> None:
        self._session = session

    async def __aenter__(
        self,
        session: Optional[aiohttp.ClientSession] = None
    ) -> "SporeClient":
        if session is None:
            session = aiohttp.ClientSession()

        await self.create(session)
        return self

    async def get_stats(self) -> "Stats":
        return self._builders.stats.build(
            await self.request(f"{self._base_url}/rest/stats")
        )

    async def get_creature(self, creature_id: Union[int, str]) -> "Creature":
        return self._builders.creature.build(
            await self.request(f"{self._base_url}/rest/creature/{creature_id}")
        )

    async def request(self, url: str) -> dict[str, Any]:
        if self._session is None:
            raise ValueError("The session does not exist")

        async with self._session.get(url) as responce:
            responce.raise_for_status()
            return self._decoder(await responce.text())

    async def close(self) -> None:
        if self._session is None:
            raise ValueError("The session does not exist")

        await self._session.close()

    async def __aexit__(
        self,
        _exception_type: Type[BaseException],
        _exception: BaseException,
        _traceback: TracebackType
    ) -> None:
        await self.close()
