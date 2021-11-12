# Spore REST API asyncio client
* Python 3.7+


**Install:**
```py
pip install spore.py
```


**Simple examples:**
```py
import asyncio

from spore_api import SporeClient


async def main() -> None:
    async with SporeClient() as client:
        print(await client.get_creature(500267423060))


asyncio.run(main())
```

In sync code:
```py
import asyncio

from spore_api import SporeClient


async def client_logic() -> str:
    async with SporeClient() as client:
        result = await client.get_creature(500267423060)

    return result.to_json()


def main() -> None:
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(client_logic())
    print(f"Json result: {result!r}")


main()
```

**Client methods:**

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
get_user_subscribers(username: str, start_index: int | str, length: int | str) -> Buddies
assets_search(view_type: ViewType, start_index: int | str, length: int | str, asset_type: AssetType | None = None) -> Assets
```


# TODO:
- [ ] Update readme
- [ ] Error handler
- [ ] Mock apps for tests
- [ ] Bin for `spore`
- [ ] Sync Client?
