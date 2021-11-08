from enum import Enum


class AssetType(str, Enum):
    building = "BUILDING"
    creature = "CREATURE"
    vehicle = "VEHICLE"
    adventure = "ADVENTURE"


class ViewType(str, Enum):
    top_rated = "TOP_RATED"
    top_rated_new = "TOP_RATED_NEW"
    newest = "NEWEST"
    featured = "FEATURED"
    maxis_made = "MAXIS_MADE"
    random = "RANDOM"
    cute_and_creepy = "CUTE_AND_CREEPY"
