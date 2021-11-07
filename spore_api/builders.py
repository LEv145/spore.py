from typing import Any

from .abc import ABCBuilder
from .models import (
    Stats,
    Creature
)


class StatsJsonBuilder(ABCBuilder):
    """
    Build Stats from json
    http://www.spore.com/rest/stats
    """

    def build(self, raw_data: dict[str, Any]) -> Stats:
        data = raw_data["stats"]
        return Stats(
            total_uploads=int(data["totalUploads"]),
            day_uploads=int(data["dayUploads"]),
            total_users=int(data["totalUsers"]),
            day_users=int(data["dayUsers"])
        )


class CreatureJsonBuilder(ABCBuilder):
    """
    Build Creature from json
    http://www.spore.com/rest/creature/500267423060
    """

    def build(self, raw_data: dict[str, Any]) -> Creature:
        data = raw_data["creature"]
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
