# Spore REST API asyncio client
* Python 3.7+


Simple example:
```py
import asyncio

from spore_api.client import SporeClient


async def main() -> None:
    async with SporeClient() as client:
        print(await client.get_creature(500267423060))


asyncio.run(main())
```


Client methods:

```py
get_stats() -> Stats
get_creature(asset_id: int | str) -> Creature
get_user_info(username: str) -> User
get_user_assets(username: str, start_index: int | str, length: int | str) -> Assets
get_user_sporecasts(username: str) -> Sporecasts:
get_sporecast_assets(sporecast_id: int | str, start_index: int | str, length: int | str) -> SporecastAssets
get_user_achievements(username: str, start_index: int | str, length: int | str) -> Achievements
get_asset_info(asset_id: int | str) -> FullAsset
get_asset_comments(asset_id: int | str, start_index: int | str, length: int | str) -> AssetComments
get_user_buddies(username: str, start_index: int | str, length: int | str) -> Buddies
get_user_subscribers(username: str, start_index: int | str, length: Uint | str) -> Buddies
assets_search(view_type: ViewType, start_index: int | str, length: int | str, asset_type: AssetType | None = None) -> Assets
```
