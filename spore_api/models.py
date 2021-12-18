from typing import TYPE_CHECKING, List, Optional
from datetime import datetime
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from .enums import AssetType, AssetSubtype


@dataclass
class Stats(DataClassJsonMixin):
    total_uploads: int
    day_uploads: int
    total_users: int
    day_users: int


@dataclass
class Creature(DataClassJsonMixin):
    asset_id: int

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
class User(DataClassJsonMixin):
    id: int
    name: str
    image_url: str
    tagline: str
    create_at: "datetime"


@dataclass
class Sporecast(DataClassJsonMixin):
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
class Asset(DataClassJsonMixin):
    id: int
    name: str
    author_name: str
    create_at: "datetime"
    rating: float
    type: "AssetType"
    subtype: "AssetSubtype"
    parent_id: Optional[int]
    description: Optional[str]
    tags: Optional[List[str]]
    thumbnail_url: str
    image_url: str


@dataclass
class FullAsset(DataClassJsonMixin):
    id: int
    name: str
    author_name: str
    create_at: "datetime"
    rating: float
    type: "AssetType"
    subtype: "AssetSubtype"
    parent_id: Optional[int]
    description: Optional[str]
    tags: Optional[List[str]]
    comments: "Comments"
    author_id: int


@dataclass
class Achievement(DataClassJsonMixin):
    name: Optional[str]
    description: Optional[str]
    guid: str
    image_url: str
    date: "datetime"


@dataclass
class Comment(DataClassJsonMixin):
    message: str
    sender_name: str


@dataclass
class Buddy(DataClassJsonMixin):
    id: int
    name: str


@dataclass
class Assets(DataClassJsonMixin):
    assets: List[Asset]

    @property
    def count(self) -> int:
        return len(self.assets)


@dataclass
class SporecastAssets(Assets):
    id: int
    name: str


@dataclass
class Sporecasts(DataClassJsonMixin):
    username: str
    sporecasts: List[Sporecast]

    @property
    def count(self) -> int:
        return len(self.sporecasts)


@dataclass
class Achievements(DataClassJsonMixin):
    username: str
    achievements: List[Achievement]

    @property
    def count(self) -> int:
        return len(self.achievements)


@dataclass
class Comments(DataClassJsonMixin):
    comments: List[Comment]

    @property
    def count(self) -> int:
        return len(self.comments)


@dataclass
class AssetComments(Comments):
    id: int
    name: str


@dataclass
class Buddies(DataClassJsonMixin):
    buddies: List[Buddy]

    @property
    def count(self) -> int:
        return len(self.buddies)
