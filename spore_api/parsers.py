import re
import json
from typing import Any, Dict, List
from pathlib import Path

import xmltodict

from spore_api.constants import BASE_URL

from .utils import datatime_from_string, find_dict_by_value
from .enums import AssetType, AssetSubtype
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
    Comment,
    User,
)


def parse_stats(text: str) -> Stats:
    """
    Build stats
    http://www.spore.com/rest/stats
    """
    raw_data: Dict[str, Any] = xmltodict.parse(text)  # type: ignore

    data: Dict[str, str] = raw_data["stats"]

    return Stats(
        total_uploads=int(data["totalUploads"]),
        day_uploads=int(data["dayUploads"]),
        total_users=int(data["totalUsers"]),
        day_users=int(data["dayUsers"])
    )


def parse_creature(text: str) -> Creature:
    """
    [Pages]

    Creature stats:
    http://www.spore.com/rest/creature/<CreatureAssetId>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(text)  # type: ignore

    data: Dict[str, str] = raw_data["creature"]

    return Creature(
        asset_id=int(data["input"]),
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


def parse_user(text: str) -> User:
    """
    [Pages]

    Profile Info:
    http://www.spore.com/rest/user/<Username>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(text)  # type: ignore

    data: Dict[str, str] = raw_data["user"]

    return User(
        id=int(data["id"]),
        name=data["input"],
        image_url=data["image"],
        tagline=data["tagline"],
        create_at=datatime_from_string(data["creation"])
    )


def parse_assets(text: str) -> Assets:
    """
    [Pages]

    Assets for user:
    http://www.spore.com/rest/assets/user/<Username>/<StartIndex>/<Length>

    Special Searches:
    http://www.spore.com/rest/assets/search/<ViewType>/<StartIndex>/<Length>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("asset",),
    )  # type: ignore

    data: Dict[str, Any] = raw_data["assets"]
    raw_assets: List[Dict[str, str]] = data["asset"]

    return Assets(
        assets=[
            Asset(
                id=int(raw_asser["id"]),
                name=raw_asser["name"],
                thumbnail_url=raw_asser["thumb"],
                image_url=raw_asser["image"],
                author_name=raw_asser["author"],
                create_at=datatime_from_string(raw_asser["created"]),
                rating=float(raw_asser["rating"]),
                type=AssetType(raw_asser["type"]),
                subtype=AssetSubtype(int(raw_asser["subtype"], 16)),
                parent_id=(
                    None
                    if raw_asser["parent"] == "NULL" else
                    int(raw_asser["parent"])
                ),
                description=(
                    None
                    if raw_asser["description"] == "NULL" else
                    raw_asser["description"]
                ),
                tags=(
                    None
                    if raw_asser["tags"] == "NULL" else
                    raw_asser["tags"].split(", ")
                ),
            )
            for raw_asser in raw_assets
        ]
    )


def parse_sporecasts(text: str) -> Sporecasts:
    """
    [Pages]

    Sporecasts for user:
    http://www.spore.com/rest/sporecasts/<Username>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("sporecast",)
    )  # type: ignore

    data: Dict[str, Any] = raw_data["sporecasts"]
    raw_sporecast: List[Dict[str, str]] = data["sporecast"]

    return Sporecasts(
        username=data["input"],
        sporecasts=[
            Sporecast(
                id=int(raw_sporecast["id"]),
                title=raw_sporecast["title"],
                subtitle=raw_sporecast["subtitle"],
                author_name=raw_sporecast["author"],
                update_at=datatime_from_string(raw_sporecast["updated"]),
                rating=float(raw_sporecast["rating"]),
                subscription_count=int(raw_sporecast["subscriptioncount"]),
                tags=re.sub(r"\W", " ", raw_sporecast["tags"]).split(),
                assets_count=int(raw_sporecast["count"])
            )
            for raw_sporecast in raw_sporecast
        ]
    )


def parse_sporecast_assets(text: str) -> SporecastAssets:
    """
    [Pages]

    Assets for sporecast:
    http://www.spore.com/rest/assets/sporecast/<Sporecast Id>/<StartIndex>/<Length>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("asset",),
    )  # type: ignore

    data: Dict[str, Any] = raw_data["assets"]
    raw_assets: List[Dict[str, str]] = data["asset"]

    return SporecastAssets(
        id=int(data["input"]),
        name=data["name"],
        assets=[
            Asset(
                id=int(raw_asser["id"]),
                name=raw_asser["name"],
                thumbnail_url=raw_asser["thumb"],
                image_url=raw_asser["image"],
                author_name=raw_asser["author"],
                create_at=datatime_from_string(raw_asser["created"]),
                rating=float(raw_asser["rating"]),
                type=AssetType(raw_asser["type"]),
                subtype=AssetSubtype(int(raw_asser["subtype"], 16)),
                parent_id=(
                    None
                    if raw_asser["parent"] == "NULL" else
                    int(raw_asser["parent"])
                ),
                description=(
                    None
                    if raw_asser["description"] == "NULL" else
                    raw_asser["description"]
                ),
                tags=(
                    None
                    if raw_asser["tags"] == "NULL" else
                    raw_asser["tags"].split(",")
                )
            )
            for raw_asser in raw_assets
        ]
    )


def parse_achievements(text: str) -> Achievements:
    """
    [Pages]

    Achievements for user:
    http://www.spore.com/rest/assets/achievements/<Username>/<StartIndex>/<Length>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("achievement",),
    )  # type: ignore

    data: Dict[str, Any] = raw_data["achievements"]
    raw_achievements: List[Dict[str, str]] = data["achievement"]

    with open(Path("./spore_api/static/achievements.json")) as fp:
        achievements_data = json.load(fp)

    achievements: List["Achievement"] = []

    for raw_achievement in raw_achievements:
        achievement_data = find_dict_by_value(
            achievements_data,
            "id",
            raw_achievement["guid"],
        )
        name = (
            achievement_data.get("name")
            if achievement_data is not None
            else None
        )
        description = (
            achievement_data.get("description")
            if achievement_data is not None
            else None
        )

        achievements.append(
            Achievement(
                name=name,
                description=description,
                guid=raw_achievement["guid"],
                image_url=(
                    f"{BASE_URL}/static/war/images/achievements/{raw_achievement['guid']}.png"
                ),
                date=datatime_from_string(raw_achievement["date"])
            )
        )

    return Achievements(
        username=data["input"],
        achievements=achievements,
    )


@staticmethod
def parse_full_asset(text: str) -> FullAsset:
    """
    [Pages]

    Info about an asset:
    http://www.spore.com/rest/asset/<AssetId>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("comment",),
    )  # type: ignore

    data: Dict[str, Any] = raw_data["asset"]
    raw_comments: List[Dict[str, str]] = data["comments"]["comment"]

    return FullAsset(
        id=int(data["input"]),
        name=data["name"],
        author_name=data["author"],
        create_at=datatime_from_string(data["created"]),
        rating=float(data["rating"]),
        type=AssetType(data["type"]),
        subtype=AssetSubtype(int(data["subtype"], 16)),
        parent_id=(
            None
            if data["parent"] == "NULL" else
            int(data["parent"])
        ),
        description=(
            None
            if data["description"] == "NULL" else
            data["description"]
        ),
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
                for raw_comment in raw_comments
            ]
        )
    )


def parse_asset_comments(text: str) -> AssetComments:
    """
    [Pages]

    Comments for an asset:
    http://www.spore.com/rest/comments/<AssetId>/<StartIndex>/<Length>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("comment",),
    )  # type: ignore

    data: Dict[str, Any] = raw_data["comments"]
    raw_comments: List[Dict[str, str]] = data["comment"]

    return AssetComments(
        id=int(data["input"]),
        name=data["name"],
        comments=[
            Comment(
                message=raw_comment["message"],
                sender_name=raw_comment["sender"]
            )
            for raw_comment in raw_comments
        ]
    )


def parse_buddies(text: str) -> Buddies:
    """
    [Pages]

    Buddies for user:
    http://www.spore.com/rest/users/buddies/<Username>/<StartIndex>/<Length>

    Who has added a user as a buddy:
    http://www.spore.com/rest/users/subscribers/<Username>/<StartIndex>/<Length>
    """
    raw_data: Dict[str, Any] = xmltodict.parse(
        text,
        force_list=("buddy",),
    )  # type: ignore

    data: Dict[str, Any] = raw_data["users"]
    raw_buddy: List[Dict[str, str]] = data["buddy"]

    return Buddies(
        buddies=[
            Buddy(
                name=raw_buddy["name"],
                id=int(raw_buddy["id"])
            )
            for raw_buddy in raw_buddy
        ]
    )
