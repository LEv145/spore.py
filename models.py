from datetime import datetime
from typing import Any, TypeVar
from abc import ABC, abstractmethod
from dataclasses import dataclass


ModelType = TypeVar("ModelType", bound="ABCModel")


class ABCModel(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls: type[ModelType], data: dict[str, Any]) -> ModelType:
        """Собираем объект из словаря"""


@dataclass
class Stats(ABCModel):
    StatsType = TypeVar("StatsType", bound="Stats")

    total_uploads: int
    day_uploads: int
    total_users: int
    day_users: int

    @classmethod
    def from_dict(cls: type[StatsType], data: dict[str, Any]) -> StatsType:
        data = data["stats"]  # FIXME: Странно
        return cls(
            total_uploads=int(data["totalUploads"]),
            day_uploads=int(data["dayUploads"]),
            total_users=int(data["totalUsers"]),
            day_users=int(data["dayUsers"])
        )


@dataclass
class Creature(ABCModel):
    CreatureType = TypeVar("CreatureType", bound="Creature")

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

    @classmethod
    def from_dict(cls: type[CreatureType], data: dict[str, Any]) -> CreatureType:
        data = data["creature"]
        return cls(
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


@dataclass
class User(ABCModel):
    UserType = TypeVar("UserType", bound="User")

    id: int
    image_url: str
    tagline: str
    create_at: datetime

    @classmethod
    def from_dict(cls: type[UserType], data: dict[str, Any]) -> UserType:
        data = data["user"]
        return cls(
            id=int(data["id"]),
            image_url=data["image"],
            tagline=data["tagline"],
            create_at=datetime.strptime(data["creation"], "%Y-%m-%d %H:%M:%S.%f")
        )


@dataclass
class Sporecast(ABCModel):
    SporecastType = TypeVar("SporecastType", bound="Sporecast")

    id: int
    title: str
    subtitle: str
    author_name: str
    update_at: datetime
    rating: float
    subscription_count: str
    tags: list[str]  # TODO: Tag object
    count: int  # Каунт чего?

    @classmethod
    def from_dict(cls: type[SporecastType], data: dict[str, Any]) -> SporecastType:
        data = data["user"]
        return cls(
            id=int(data["id"]),
            title=data["title"],
            subtitle=data["subtitle"],
            author_name=data["author"],
            update_at=data["updated"],
            rating=float(data["rating"]),
            subscription_count=data["subscriptioncount"],
            tags=data["tags"][1:-1].split(", "),
            count=int(data["count"])
        )


@dataclass
class Asset(ABCModel):
    AssetType = TypeVar("AssetType", bound="Asset")

    id: int
    name: str
    thumbnail_url: str
    image_url: str
    author_name: str
    create_at: datetime
    rating: float
    asset_type: str  # TODO: Enum?
    subtype: str  # TODO
    parent: str  # TODO
    description: str
    tags: str  # TODO

    @classmethod
    def from_dict(cls: type[AssetType], data: dict[str, Any]) -> AssetType:
        data = data["asset"]
        return cls(
            id=int(data["id"]),
            name=data["name"],
            thumbnail_url=data["thumb"],
            image_url=data["image_url"],
            author_name=data["author"],
            create_at=datetime.strptime(data["created"], "%Y-%m-%d %H:%M:%S.%f"),
            rating=float(data["rating"]),
            asset_type=data["type"],
            subtype=data["subtype"],
            parent=data["parent"],
            description=data["description"],
            tags=data["tags"]
        )
