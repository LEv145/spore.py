# Spore REST API client

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)

## How to use

```text
> spore_cli.exe --help
Usage: spore_cli [OPTIONS] COMMAND [ARGS]...

  CLI for Spore REST API

Options:
  --help  Show this message and exit.

Commands:
  get-asset-comments     Get comments of the asset
  get-asset-info         Get asset information
  get-creature           Get creature
  get-sporecast-assets   Get assets of the sporecast
  get-stats              Get stats
  get-user-achievements  Get achievements of the user
  get-user-assets        Get creature of the user
  get-user-buddies       Get buddies of the user
  get-user-info          Get user information
  get-user-sporecasts    Get sporecasts of the user
  get-user-subscribers   Get subscribers of the user
  search-assets          Search assets

> spore_cli.exe search-assets --help
Usage: spore_cli search-assets [OPTIONS] {top_rated|top_rated_new|newest|featu
                               red|maxis_made|random|cute_and_creepy}
                               [START_INDEX] [LENGTH]
                               [[building|creature|vehicle|adventure|ufo]]

  Search assets

Options:
  --help  Show this message and exit.

> spore_cli.exe get-creature 500267423060  # Get json info of creature
{"asset_id": 500267423060, "cost": 4065, "health": 3.0, "height": 1.3428643, "meanness": 9.0, "cuteness": 71.26385, "sense": 1.0, "bonecount": 44.0, "footcount": 4.0, "graspercount": 0.0, "basegear": 0.0, "carnivore": 1.0, "herbivore": 0.0, "glide": 0.0, "sprint": 2.0, "stealth": 2.0, "bite": 3.0, "charge": 2.0, "strike": 4.0, "spit": 0.0, "sing": 1.0, "dance": 2.0, "gesture": 5.0, "posture": 0.0}
```

## Build

Build binary:

```text
pyinstaller pyinstaller.spec \
  --distpath pyinstaller_builds/dist \
  --workpath pyinstaller_builds/build
```

Build for python (requires Python 3.7+)

```text
pip install --editable .
```

## Work in Python

### Install

```py
pip install git+https://github.com/LEv145/spore.py
```

Or from pypi

```py
pip install spore.py
```

### Simple examples

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

## Client methods

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

TODO:

- Tests
- IMPLEMENTATION.md
