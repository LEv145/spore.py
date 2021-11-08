from dataclasses import dataclass
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Optional, Type, Union

import aiohttp
import xmltodict

from .constants import BASE_URL
from .abc import ABCBuilder
from .builders import (
    StatsBuilder,
    CreatureStatsBuilder
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
        self._session = None

        self._base_url = BASE_URL
        self._decoder: Callable[[str], dict[str, Any]] = xmltodict.parse

        self._builders = Builders(
            stats=StatsBuilder(self._decoder),
            creature=CreatureStatsBuilder(self._decoder),
        )

    async def create(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        if session is None:
            self._session = session

    async def __aenter__(
        self,
        session: Optional[aiohttp.ClientSession] = None
    ) -> "SporeClient":
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

    async def request(self, url: str) -> str:
        if self._session is None:
            raise ValueError("The session does not exist")

        async with self._session.get(url) as responce:
            responce.raise_for_status()
            return await responce.text()

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
