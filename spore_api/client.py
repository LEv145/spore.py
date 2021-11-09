from dataclasses import dataclass
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Optional, Type, Union

import aiohttp
import xmltodict


from .constants import BASE_URL
from .enums import AssetType, ViewType
from .builders import (
    StatsBuilder,
    CreatureBuilder,
    UserBuilder,
    AssetsBuilder,
    SporecastsBuilder,
    SporecastAssetsBuilder,
    AchievementsBuilder,
    FullAssetBuilder,
    AssetCommentsBuilder,
    BuddiesBuilder
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
        FullAsset
    )


@dataclass
class Builders():  # TODO: Delete
    stats: StatsBuilder
    creature: CreatureBuilder
    user: UserBuilder
    assets: AssetsBuilder
    sporecasts: SporecastsBuilder
    sporecast_assets: SporecastAssetsBuilder
    achievements: AchievementsBuilder
    full_asset: FullAssetBuilder
    asset_comments: AssetCommentsBuilder
    buddies: BuddiesBuilder


class SporeClient():
    _decoder: Callable[[str], dict[str, Any]]
    _base_url: str

    def __init__(self) -> None:
        self._session = None
        self._init()

        self._builders = Builders(
            stats=StatsBuilder(self._decoder),
            creature=CreatureBuilder(self._decoder),
            user=UserBuilder(self._decoder),
            assets=AssetsBuilder(self._decoder),
            sporecasts=SporecastsBuilder(self._decoder),
            sporecast_assets=SporecastAssetsBuilder(self._decoder),
            achievements=AchievementsBuilder(self._decoder),
            full_asset=FullAssetBuilder(self._decoder),
            asset_comments=AssetCommentsBuilder(self._decoder),
            buddies=BuddiesBuilder(self._decoder)
        )  # TODO: Delete

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
        return self._builders.stats.build(
            await self.request(f"{self._base_url}/rest/stats")
        )

    async def get_creature(
        self,
        creature_id: Union[int, str]
    ) -> "Creature":
        return self._builders.creature.build(
            await self.request(f"{self._base_url}/rest/creature/{creature_id}")
        )

    async def get_user_info(
        self,
        username: str
    ) -> "User":
        return self._builders.user.build(
            await self.request(f"{self._base_url}/rest/user/{username}")
        )

    async def get_user_assets(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Assets":
        return self._builders.assets.build(
            await self.request(
                f"{self._base_url}/rest/assets/user/{username}/{start_index}/{length}"
            )
        )

    async def get_user_sporecasts(
        self,
        username: str
    ):
        return self._builders.sporecasts.build(
            await self.request(f"{self._base_url}/rest/sporecasts/{username}")
        )

    async def get_sporecast_assets(
        self,
        sporecast_id: Union[int, str],
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "SporecastAssets":
        return self._builders.sporecast_assets.build(
            await self.request(
                f"{self._base_url}/rest/assets/sporecast/{sporecast_id}/{start_index}/{length}"
            )
        )

    async def get_user_achievements(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Achievements":
        return self._builders.achievements.build(
            await self.request(
                f"{self._base_url}/rest/achievements/{username}/{start_index}/{length}"
            )
        )

    async def get_asset_info(
        self,
        asset_id: Union[int, str]
    ) -> "FullAsset":
        return self._builders.full_asset.build(
            await self.request(
                f"{self._base_url}/rest/asset/{asset_id}"
            )
        )

    async def get_asset_comments(
        self,
        asset_id: Union[int, str],
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "AssetComments":
        return self._builders.asset_comments.build(
            await self.request(
                f"{self._base_url}/rest/comments/{asset_id}/{start_index}/{length}"
            )
        )

    async def get_user_buddies(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Buddies":
        return self._builders.buddies.build(
            await self.request(
                f"{self._base_url}/rest/users/buddies/{username}/{start_index}/{length}"
            )
        )

    async def get_user_subscribers(
        self,
        username: str,
        start_index: Union[int, str],
        length: Union[int, str]
    ) -> "Buddies":
        return self._builders.buddies.build(
            await self.request(
                f"{self._base_url}/rest/users/subscribers/{username}/{start_index}/{length}"
            )
        )

    async def get_assets_searches(
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

        return self._builders.assets.build(await self.request(url))

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
