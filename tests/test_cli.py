import unittest
import subprocess

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


APP_NANE = "spore"


class TestCLI(unittest.IsolatedAsyncioTestCase):

    async def test_stats(self):
        result = subprocess.run(
            [APP_NANE, "get-stats"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Stats.from_json(result.stdout)

    async def test_creature(self):
        result = subprocess.run(
            [APP_NANE, "get-creature", "500267423060"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Creature.from_json(result.stdout)

    async def test_user_info(self):
        result = subprocess.run(
            [APP_NANE, "get-user-info", "MaxisDangerousYams"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        User.from_json(result.stdout)

    async def test_user_assets(self):
        result = subprocess.run(
            [APP_NANE, "get-user-assets", "MaxisCactus", "0", "3"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Assets.from_json(result.stdout)

    async def test_user_sporecasts(self):
        result = subprocess.run(
            [APP_NANE, "get-user-sporecasts", "MaxisMichael"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Sporecasts.from_json(result.stdout)

    async def test_user_achievements(self):
        result = subprocess.run(
            [APP_NANE, "get-user-achievements", "MaxisLucky", "0", "5"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Achievements.from_json(result.stdout)

    async def test_user_buddies(self):
        result = subprocess.run(
            [APP_NANE, "get-user-buddies", "MaxisDangerousYams", "0", "10"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Buddies.from_json(result.stdout)

    async def test_user_subscribers(self):
        result = subprocess.run(
            [APP_NANE, "get-user-subscribers", "MaxisDangerousYams", "0", "10"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Buddies.from_json(result.stdout)

    async def test_asset_info(self):
        result = subprocess.run(
            [APP_NANE, "get-asset-info", "500005649853"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        FullAsset.from_json(result.stdout)

    async def test_asset_comments(self):
        result = subprocess.run(
            [APP_NANE, "get-asset-comments", "500005649853", "0", "5"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        AssetComments.from_json(result.stdout)

    async def test_sporecast_assets(self):
        result = subprocess.run(
            [APP_NANE, "get-sporecast-assets", "500190457259", "2", "3"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        SporecastAssets.from_json(result.stdout)

    async def assets_search(self):
        result = subprocess.run(
            [APP_NANE, "assets-search", "top_rated", "0", "2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Assets.from_json(result.stdout)

        # With AssetType
        result = subprocess.run(
            [APP_NANE, "assets-search", "featured", "0", "5", "building"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Assets.from_json(result.stdout)
