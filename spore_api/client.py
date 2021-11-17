import re
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Optional, Type, Union

import aiohttp
import xmltodict

from .errors import SporeApiStatusError
from .constants import BASE_URL
from .enums import AssetType, ViewType
from .json_builders import (
    build_stats,
    build_creature,
    build_user,
    build_assets,
    build_sporecasts,
    build_sporecast_assets,
    build_achievements,
    build_full_asset,
    build_asset_comments,
    build_buddies
)

if TYPE_CHECKING:
    from .models import (
        Stats,
        Creature,
        User,
        Achievements,
        AssetComments,
        Assets,
        Buddies,
        SporecastAssets,
        FullAsset,
        Sporecasts
    )


class SporeClient():
    _decoder: Callable[[str], dict[str, Any]]
    _base_url: str

    def __init__(self) -> None:
        self._session = None
        self._init()

    def _init(self):
        self._base_url = BASE_URL
        self._decoder = xmltodict.parse

    async def create(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session = (
            aiohttp.ClientSession()
            if session is None else
            session
        )

    async def __aenter__(
        self,
        session: Optional[aiohttp.ClientSession] = None
    ) -> "SporeClient":
        await self.create(session)
        return self

    async def get_stats(self) -> "Stats":
        return build_stats(
            await self.get_data_from_url(f"{self._base_url}/rest/stats")
        )

    async def get_creature(
        self,
        asset_id: Union[int, str]
    ) -> "Creature":
        return build_creature(
            await self.get_data_from_url(f"{self._base_url}/rest/creature/{asset_id}")
        )

    async def get_user_info(
        self,
        username: str
    ) -> "User":
        return build_user(
            await self.get_data_from_url(f"{self._base_url}/rest/user/{username}")
        )

    async def get_user_assets(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Assets":
        return build_assets(
            await self.get_data_from_url(
                f"{self._base_url}/rest/assets/user/{username}/{start_index}/{length}"
            )
        )

    async def get_user_sporecasts(
        self,
        username: str
    ) -> "Sporecasts":
        return build_sporecasts(
            await self.get_data_from_url(f"{self._base_url}/rest/sporecasts/{username}")
        )

    async def get_sporecast_assets(
        self,
        sporecast_id: Union[int, str],
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "SporecastAssets":
        return build_sporecast_assets(
            await self.get_data_from_url(
                f"{self._base_url}/rest/assets/sporecast/{sporecast_id}/{start_index}/{length}"
            )
        )

    async def get_user_achievements(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Achievements":
        return build_achievements(
            await self.get_data_from_url(
                f"{self._base_url}/rest/achievements/{username}/{start_index}/{length}"
            )
        )

    async def get_asset_info(
        self,
        asset_id: Union[int, str]
    ) -> "FullAsset":
        return build_full_asset(
            await self.get_data_from_url(
                f"{self._base_url}/rest/asset/{asset_id}"
            )
        )

    async def get_asset_comments(
        self,
        asset_id: Union[int, str],
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "AssetComments":
        return build_asset_comments(
            await self.get_data_from_url(
                f"{self._base_url}/rest/comments/{asset_id}/{start_index}/{length}"
            )
        )

    async def get_user_buddies(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Buddies":
        return build_buddies(
            await self.get_data_from_url(
                f"{self._base_url}/rest/users/buddies/{username}/{start_index}/{length}"
            )
        )

    async def get_user_subscribers(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Buddies":
        return build_buddies(
            await self.get_data_from_url(
                f"{self._base_url}/rest/users/subscribers/{username}/{start_index}/{length}"
            )
        )

    async def assets_search(
        self,
        view_type: ViewType,
        start_index: Union[int, str],
        length: Union[int, str],
        asset_type: Optional[AssetType] = None
    ) -> "Assets":
        if asset_type is None:
            url = f"{self._base_url}/rest/assets/search/{view_type}/{start_index}/{length}"
        else:
            url = f"{self._base_url}/rest/assets/search/{view_type}/{start_index}/{length}/{asset_type}"

        return build_assets(
            await self.get_data_from_url(url)
        )

    async def get_data_from_url(self, url: str):
        text = await self.get_response_text(url)
        return await self.parse_response_text(text)

    async def parse_response_text(self, text: str):
        api_status_parse = re.search(r"<status>(\d+)</status>", text)
        if api_status_parse is not None:
            api_status = int(api_status_parse.group(1))

            if api_status != 1:
                raise SporeApiStatusError(api_status)

        raw_data = self._decoder(text)
        return raw_data

    async def get_response_text(self, url: str) -> str:
        if self._session is None:
            raise ValueError("The session does not exist")

        async with self._session.get(url) as response:
            response.raise_for_status()
            return await response.text()

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
