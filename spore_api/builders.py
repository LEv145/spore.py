from typing import List

from .utils import datatime_from_string
from .abc import ABCBuilder
from .enums import AssetType
from .models import (
    Stats,
    Creature,
    Asset,
    SporecastAssets
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
    def build(self, raw_data: str) -> List[Asset]:
        data = self._decoder(raw_data)["assets"]
        return [
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
                author_id=None
            )
            for raw_asser in data["asset"]
        ]


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
                    ),
                    author_id=None
                )
                for raw_asser in data["asset"]
            ]
        )
