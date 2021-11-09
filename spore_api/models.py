from typing import TYPE_CHECKING, List, Optional
from dataclasses import dataclass


if TYPE_CHECKING:
    from datetime import datetime

    from .enums import AssetType, AssetSubtype


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


@dataclass
class User():
    id: int
    image_url: str
    tagline: str
    create_at: "datetime"


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


@dataclass
class Asset():
    id: int  # FIXME
    name: str
    thumbnail_url: str
    image_url: str
    author_name: str
    create_at: "datetime"
    rating: float
    type: "AssetType"
    subtype: "AssetSubtype"
    parent_id: Optional[int]
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


@dataclass
class Comment():
    message: str
    sender_name: str


@dataclass
class Buddy():
    name: str
    id: int


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
