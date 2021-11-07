from typing import List

from spore_api.constants import BASE_URL

from .utils import datatime_from_string
from .abc import ABCBuilder
from .enums import AssetType
from .models import (
    Achievement,
    Achievements,
    AssetComments,
    Assets,
    Buddies,
    Buddy,
    Comments,
    FullAsset,
    Sporecast,
    Sporecasts,
    Stats,
    Creature,
    Asset,
    SporecastAssets,
    Comment
)


class StatsBuilder(ABCBuilder):
    """
    Build stats
    http://www.spore.com/rest/stats
    """
    def build(self, raw_data: str) -> Stats:
        data = self._decoder(raw_data)["stats"]
        return Stats(
            total_uploads=int(data["totalUploads"]),
            day_uploads=int(data["dayUploads"]),
            total_users=int(data["totalUsers"]),
            day_users=int(data["dayUsers"])
        )


class CreatureStatsBuilder(ABCBuilder):
    """
    Build creature stats
    http://www.spore.com/rest/creature/500267423060
    """
    def build(self, raw_data: str) -> Creature:
        data = self._decoder(raw_data)["creature"]
        return Creature(
            cost=int(data["cost"]),
            health=float(data["health"]),
            height=float(data["height"]),
            meanness=float(data["meanness"]),
            cuteness=float(data["cuteness"]),
            sense=float(data["sense"]),
            bonecount=float(data["bonecount"]),
            footcount=float(data["footcount"]),
            graspercount=float(data["graspercount"]),
            basegear=float(data["basegear"]),
            carnivore=float(data["carnivore"]),
            herbivore=float(data["herbivore"]),
            glide=float(data["glide"]),
            sprint=float(data["sprint"]),
            stealth=float(data["stealth"]),
            bite=float(data["bite"]),
            charge=float(data["charge"]),
            strike=float(data["strike"]),
            spit=float(data["spit"]),
            sing=float(data["sing"]),
            dance=float(data["dance"]),
            gesture=float(data["gesture"]),
            posture=float(data["posture"]),
        )


class ProfileInfoBuilder(ABCBuilder):
    """
    Build profile info
    http://www.spore.com/rest/creature/500267423060
    """
    def build(self, raw_data: str) -> Creature:
        data = self._decoder(raw_data)["creature"]
        return Creature(
            cost=int(data["cost"]),
            health=float(data["health"]),
            height=float(data["height"]),
            meanness=float(data["meanness"]),
            cuteness=float(data["cuteness"]),
            sense=float(data["sense"]),
            bonecount=float(data["bonecount"]),
            footcount=float(data["footcount"]),
            graspercount=float(data["graspercount"]),
            basegear=float(data["basegear"]),
            carnivore=float(data["carnivore"]),
            herbivore=float(data["herbivore"]),
            glide=float(data["glide"]),
            sprint=float(data["sprint"]),
            stealth=float(data["stealth"]),
            bite=float(data["bite"]),
            charge=float(data["charge"]),
            strike=float(data["strike"]),
            spit=float(data["spit"]),
            sing=float(data["sing"]),
            dance=float(data["dance"]),
            gesture=float(data["gesture"]),
            posture=float(data["posture"]),
        )


class UserAssetsBuilder(ABCBuilder):
    """
    Build assets for user
    http://www.spore.com/rest/assets/user/MaxisCactus/0/3
    """
    def build(self, raw_data: str) -> Assets:
        data = self._decoder(raw_data)["assets"]
        return Assets(
            assets=[
                Asset(
                    id=int(raw_asser["id"]),
                    name=raw_asser["name"],
                    thumbnail_url=raw_asser["thumb"],
                    image_url=raw_asser["image_url"],
                    author_name=raw_asser["author"],
                    create_at=datatime_from_string(raw_asser["created"]),
                    rating=float(data["rating"]),
                    type=AssetType(data["type"]),
                    subtype=data["subtype"],
                    parent=data["parent"],
                    description=data["description"],
                    tags=(
                        None
                        if data["tags"] == "NULL" else
                        data["tags"].split(",")
                    ),
                )
                for raw_asser in data["asset"]
            ]
        )


class UserSporecastsBuilder(ABCBuilder):
    """
    Build sporecasts for user
    http://www.spore.com/rest/sporecasts/MaxisMichael
    """

    def build(self, raw_data: str) -> Sporecasts:
        data = self._decoder(raw_data)["sporecasts"]
        return Sporecasts(
            sporecasts=[
                Sporecast(
                    id=int(raw_sporecast["id"]),
                    title=raw_sporecast["title"],
                    subtitle=raw_sporecast["subtitle"],
                    author_name=raw_sporecast["author"],
                    update_at=raw_sporecast["updated"],
                    rating=float(raw_sporecast["rating"]),
                    subscription_count=raw_sporecast["subscriptioncount"],
                    tags=raw_sporecast["tags"][1:-1].split(", "),
                    assets_count=int(raw_sporecast["count"])
                )
                for raw_sporecast in data["sporecast"]
            ]
        )


class SporecastAssetsBuilder(ABCBuilder):
    """
    Build assets for sporecast
    http://www.spore.com/rest/assets/sporecast/500190457259/2/3
    """
    def build(self, raw_data: str) -> SporecastAssets:
        data = self._decoder(raw_data)["assets"]
        return SporecastAssets(
            name=data["name"],
            assets=[
                Asset(
                    id=int(raw_asser["id"]),
                    name=raw_asser["name"],
                    thumbnail_url=raw_asser["thumb"],
                    image_url=raw_asser["image_url"],
                    author_name=raw_asser["author"],
                    create_at=datatime_from_string(raw_asser["created"]),
                    rating=float(data["rating"]),
                    type=AssetType(data["type"]),
                    subtype=data["subtype"],
                    parent=data["parent"],
                    description=data["description"],
                    tags=(
                        None
                        if data["tags"] == "NULL" else
                        data["tags"].split(",")
                    )
                )
                for raw_asser in data["asset"]
            ]
        )


class UserAchievementsBuilder(ABCBuilder):
    """
    Build achievements for user
    http://www.spore.com/rest/achievements/MaxisLucky/0/5
    """
    def build(self, raw_data: str) -> Achievements:
        data = self._decoder(raw_data)["achievements"]
        return Achievements(
            achievements=[
                Achievement(
                    guid=raw_achievement["guid"],
                    image_url=f"{BASE_URL}/static/war/images/achievements/{raw_achievement['guild']}.png",
                    date=datatime_from_string(raw_achievement["date"])
                )
                for raw_achievement in data["achievement"]
            ]
        )


class AssetInfoBuilder(ABCBuilder):
    """
    Build info about an asset
    http://www.spore.com/rest/asset/500005649853
    """
    def build(self, raw_data: str) -> FullAsset:
        data = self._decoder(raw_data)["achievements"]
        return FullAsset(
            id=int(data["id"]),
            name=data["name"],
            thumbnail_url=data["thumb"],
            image_url=data["image_url"],
            author_name=data["author"],
            create_at=datatime_from_string(data["created"]),
            rating=float(data["rating"]),
            type=AssetType(data["type"]),
            subtype=data["subtype"],
            parent=data["parent"],
            description=data["description"],
            tags=(
                None
                if data["tags"] == "NULL" else
                data["tags"].split(",")
            ),
            author_id=data["authorid"],
            comments=Comments(
                comments=[
                    Comment(
                        message=raw_comment["message"],
                        sender_name=raw_comment["sender"]
                    )
                    for raw_comment in data["comments"]
                ]
            )
        )


class AsserCommentsBuilder(ABCBuilder):
    """
    Build comments for an asset
    http://www.spore.com/rest/comments/500226147573/0/5
    """
    def build(self, raw_data: str) -> AssetComments:
        data = self._decoder(raw_data)["comments"]
        return AssetComments(
            name=data["name"],
            comments=[
                Comment(
                    message=raw_comment["message"],
                    sender_name=raw_comment["sender"]
                )
                for raw_comment in data["comments"]
            ]
        )


class UserBuddiesBuilder(ABCBuilder):
    """
    Build buddies for user
    http://www.spore.com/rest/users/buddies/MaxisDangerousYams/0/10
    """
    def build(self, raw_data: str) -> Buddies:
        data = self._decoder(raw_data)["users"]
        return Buddies(
            buddies=[
                Buddy(
                    name=raw_buddy["name"],
                    id=int(raw_buddy["id"])
                )
                for raw_buddy in data["buddy"]
            ]
        )
