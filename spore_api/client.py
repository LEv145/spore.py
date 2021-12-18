import re
from types import TracebackType
from typing import (
    TYPE_CHECKING,
    Optional,
    Type,
    Union,
)

import aiohttp

from .errors import SporeApiStatusError
from .constants import BASE_URL
from .enums import AssetType, ViewType
from .parsers import (
    parse_stats,
    parse_creature,
    parse_user,
    parse_assets,
    parse_sporecasts,
    parse_sporecast_assets,
    parse_achievements,
    parse_full_asset,
    parse_asset_comments,
    parse_buddies,
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
        Sporecasts,
    )


class SporeClient():
    def __init__(self) -> None:
        self._session = None

    async def create(
        self,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        self._session = (
            aiohttp.ClientSession()
            if session is None else
            session
        )

    async def __aenter__(
        self,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> "SporeClient":
        await self.create(session)
        return self

    async def get_stats(self) -> "Stats":
        url = f"{BASE_URL}/rest/stats"

        return parse_stats(
            await self.get_response_text(url)
        )

    async def get_creature(
        self,
        asset_id: Union[int, str],
    ) -> "Creature":
        url = f"{BASE_URL}/rest/creature/{asset_id}"

        return parse_creature(
            await self.get_response_text(url)
        )

    async def get_user_info(
        self,
        username: str,
    ) -> "User":
        url = f"{BASE_URL}/rest/user/{username}"

        return parse_user(
            await self.get_response_text(url)
        )

    async def get_user_assets(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str],
    ) -> "Assets":
        url = f"{BASE_URL}/rest/assets/user/{username}/{start_index}/{length}"

        return parse_assets(
            await self.get_response_text(url)
        )

    async def get_user_sporecasts(
        self,
        username: str,
    ) -> "Sporecasts":
        url = f"{BASE_URL}/rest/sporecasts/{username}"

        return parse_sporecasts(
            await self.get_response_text(url)
        )

    async def get_sporecast_assets(
        self,
        sporecast_id: Union[int, str],
        start_index: Union[int, str],
        length: Union[int, str],
    ) -> "SporecastAssets":
        url = f"{BASE_URL}/rest/assets/sporecast/{sporecast_id}/{start_index}/{length}"

        return parse_sporecast_assets(
            await self.get_response_text(url)
        )

    async def get_user_achievements(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str],
    ) -> "Achievements":
        url = f"{BASE_URL}/rest/achievements/{username}/{start_index}/{length}"

        return parse_achievements(
            await self.get_response_text(url)
        )

    async def get_asset_info(
        self,
        asset_id: Union[int, str],
    ) -> "FullAsset":
        url = f"{BASE_URL}/rest/asset/{asset_id}"

        return parse_full_asset(
            await self.get_response_text(url)
        )

    async def get_asset_comments(
        self,
        asset_id: Union[int, str],
        start_index: Union[int, str],
        length: Union[int, str],
    ) -> "AssetComments":
        url = f"{BASE_URL}/rest/comments/{asset_id}/{start_index}/{length}"

        return parse_asset_comments(
            await self.get_response_text(url)
        )

    async def get_user_buddies(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str],
    ) -> "Buddies":
        url = f"{BASE_URL}/rest/users/buddies/{username}/{start_index}/{length}"

        return parse_buddies(
            await self.get_response_text(url)
        )

    async def get_user_subscribers(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str],
    ) -> "Buddies":
        url = f"{BASE_URL}/rest/users/subscribers/{username}/{start_index}/{length}"

        return parse_buddies(
            await self.get_response_text(url)
        )

    async def search_assets(
        self,
        view_type: ViewType,
        start_index: Union[int, str],
        length: Union[int, str],
        asset_type: Optional[AssetType] = None,
    ) -> "Assets":
        url = (
            f"{BASE_URL}/rest/assets/search/{view_type}/{start_index}/{length}"
            if asset_type is None else
            f"{BASE_URL}/rest/assets/search/{view_type}/{start_index}/{length}/{asset_type}"
        )

        return parse_assets(
            await self.get_response_text(url)
        )

    async def get_response_text(self, url: str) -> str:
        text = await self._get_response_text(url)
        self.check_status_spore_api(text)
        return text

    def check_status_spore_api(self, text: str) -> None:
        api_status_parse = re.search(r"<status>(\d+)</status>", text)
        if api_status_parse is not None:
            api_status = int(api_status_parse.group(1))

            if api_status != 1:
                raise SporeApiStatusError(api_status)

    async def _get_response_text(self, url: str) -> str:
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
