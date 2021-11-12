import unittest

from spore_api.client import SporeClient
from spore_api.enums import ViewType, AssetType
from spore_api.models import (
    Achievements,
    AssetComments,
    Assets,
    Buddies,
    Creature,
    FullAsset,
    SporecastAssets,
    Sporecasts,
    Stats,
    User
)


class TestAPIModel(unittest.IsolatedAsyncioTestCase):

    async def test_stats(self):
        async with SporeClient() as client:
            result = await client.get_stats()
            self.assertIsInstance(result, Stats)

    async def test_creature(self):
        async with SporeClient() as client:
            result = await client.get_creature(500267423060)
            self.assertIsInstance(result, Creature)

    async def test_user_info(self):
        async with SporeClient() as client:
            result = await client.get_user_info("MaxisDangerousYams")
            self.assertIsInstance(result, User)

    async def test_user_assets(self):
        async with SporeClient() as client:
            result = await client.get_user_assets("MaxisCactus", 0, 3)
            self.assertIsInstance(result, Assets)

    async def test_user_sporecasts(self):
        async with SporeClient() as client:
            result = await client.get_user_sporecasts("MaxisMichael")
            self.assertIsInstance(result, Sporecasts)

    async def test_user_achievements(self):
        async with SporeClient() as client:
            result = await client.get_user_achievements("MaxisLucky", 0, 5)
            self.assertIsInstance(result, Achievements)

    async def test_user_buddies(self):
        async with SporeClient() as client:
            result = await client.get_user_buddies("MaxisDangerousYams", 0, 10)
            self.assertIsInstance(result, Buddies)

    async def test_user_subscribers(self):
        async with SporeClient() as client:
            result = await client.get_user_subscribers("MaxisDangerousYams", 0, 10)
            self.assertIsInstance(result, Buddies)

    async def test_asset_info(self):
        async with SporeClient() as client:
            result = await client.get_asset_info(500005649853)
            self.assertIsInstance(result, FullAsset)

    async def test_asset_comments(self):
        async with SporeClient() as client:
            result = await client.get_asset_comments(500226147573, 0, 5)
            self.assertIsInstance(result, AssetComments)

    async def test_sporecast_assets(self):
        async with SporeClient() as client:
            result = await client.get_sporecast_assets("500190457259", 2, 3)
            self.assertIsInstance(result, SporecastAssets)

    async def assets_search(self):
        async with SporeClient() as client:
            result = await client.assets_search(ViewType.top_rated, 0, 2)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.top_rated_new, 0, 2)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.newest, 0, 2)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.maxis_made, 0, 7)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.random, 0, 4)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.cute_and_creepy, 0, 8)
            self.assertIsInstance(result, Assets)

            # With AssetType
            result = await client.assets_search(ViewType.featured, 0, 5, AssetType.ufo)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.top_rated_new, 0, 2, AssetType.creature)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.random, 0, 5, AssetType.building)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.top_rated, 0, 2, AssetType.adventure)
            self.assertIsInstance(result, Assets)

            result = await client.assets_search(ViewType.top_rated, 0, 2, AssetType.vehicle)
            self.assertIsInstance(result, Assets)
