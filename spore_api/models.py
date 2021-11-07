from typing import TYPE_CHECKING, List, Optional
from dataclasses import dataclass


if TYPE_CHECKING:
    from datetime import datetime

    from .enums import AssetType


@dataclass
class Stats():
    total_uploads: int
    day_uploads: int
    total_users: int
    day_users: int


@dataclass
class Creature():
    cost: int
    health: float
    height: float
    meanness: float
    cuteness: float
    sense: float
    bonecount: float
    footcount: float
    graspercount: float
    basegear: float
    carnivore: float
    herbivore: float
    glide: float
    sprint: float
    stealth: float
    bite: float
    charge: float
    strike: float
    spit: float
    sing: float
    dance: float
    gesture: float
    posture: float

    # @classmethod
    # def from_dict(cls: Type[CreatureType], data: Dict[str, Any]) -> CreatureType:
    #     data = data["creature"]
    #     return cls(
    #         cost=int(data["cost"]),
    #         health=float(data["health"]),
    #         height=float(data["height"]),
    #         meanness=float(data["meanness"]),
    #         cuteness=float(data["cuteness"]),
    #         sense=float(data["sense"]),
    #         bonecount=float(data["bonecount"]),
    #         footcount=float(data["footcount"]),
    #         graspercount=float(data["graspercount"]),
    #         basegear=float(data["basegear"]),
    #         carnivore=float(data["carnivore"]),
    #         herbivore=float(data["herbivore"]),
    #         glide=float(data["glide"]),
    #         sprint=float(data["sprint"]),
    #         stealth=float(data["stealth"]),
    #         bite=float(data["bite"]),
    #         charge=float(data["charge"]),
    #         strike=float(data["strike"]),
    #         spit=float(data["spit"]),
    #         sing=float(data["sing"]),
    #         dance=float(data["dance"]),
    #         gesture=float(data["gesture"]),
    #         posture=float(data["posture"]),
    #     )


@dataclass
class User():
    id: int
    image_url: str
    tagline: str
    create_at: "datetime"

    # @classmethod
    # def from_dict(cls: Type[UserType], data: Dict[str, Any]) -> UserType:
    #     data = data["user"]
    #     return cls(
    #         id=int(data["id"]),
    #         image_url=data["image"],
    #         tagline=data["tagline"],
    #         create_at=datatime_from_string(data["creation"])
    #     )


@dataclass
class Sporecast():
    id: int
    title: str
    subtitle: str
    author_name: str
    update_at: "datetime"
    rating: float
    subscription_count: int
    tags: List[str]
    assets_count: int

    # @classmethod
    # def from_dict(cls: Type[SporecastType], data: Dict[str, Any]) -> SporecastType:
    #     data = data["sporecast"]
    #     return cls(
    #         id=int(data["id"]),
    #         title=data["title"],
    #         subtitle=data["subtitle"],
    #         author_name=data["author"],
    #         update_at=data["updated"],
    #         rating=float(data["rating"]),
    #         subscription_count=data["subscriptioncount"],
    #         tags=data["tags"][1:-1].split(", "),
    #         assets_count=int(data["count"])
    #     )


@dataclass
class Asset():
    id: int
    name: str
    thumbnail_url: str
    image_url: str
    author_name: str
    create_at: "datetime"
    rating: float
    type: "AssetType"
    subtype: str  # TODO
    parent: str  # TODO
    description: str
    tags: Optional[List[str]]


@dataclass
class FullAsset(Asset):
    comments: "Comments"
    author_id: int


@dataclass
class Achievement():
    guid: str
    image_url: str
    date: "datetime"

    # @classmethod
    # def from_dict(cls: Type[AchievementType], data: Dict[str, Any]) -> AchievementType:
    #     data = data["achievement"]
    #     return cls(
    #         guild=data["guild"],
    #         image_url=f"{BASE_URL}/static/war/images/achievements/{data['guild']}.png",
    #         date=datatime_from_string(data["date"])
    #     )


@dataclass
class Comment():
    message: str
    sender_name: str

    # @classmethod
    # def from_dict(cls: Type[CommentType], data: Dict[str, Any]) -> CommentType:
    #     data = data["comment"]
    #     return cls(
    #         message=data["message"],
    #         sender_name=data["sender"]
    #     )


@dataclass
class Buddy():
    name: str
    id: int

    # @classmethod
    # def from_dict(cls: Type[BuddyType], data: Dict[str, Any]) -> BuddyType:
    #     data = data["buddy"]
    #     return cls(
    #         name=data["name"],
    #         id=int(data["id"])
    #     )


@dataclass
class Assets():
    assets: List[Asset]

    @property
    def count(self) -> int:
        return len(self.assets)


@dataclass
class SporecastAssets(Assets):
    name: str

@dataclass
class Sporecasts():
    sporecasts: List[Sporecast]

    @property
    def count(self) -> int:
        return len(self.sporecasts)


@dataclass
class Achievements():
    achievements: List[Achievement]

    @property
    def count(self) -> int:
        return len(self.achievements)


@dataclass
class Comments():
    comments: List[Comment]

    @property
    def count(self) -> int:
        return len(self.comments)


@dataclass
class AssetComments(Comments):
    name: str


@dataclass
class Buddies():
    buddies: List[Buddy]

    @property
    def count(self) -> int:
        return len(self.buddies)
