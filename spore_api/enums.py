from enum import Enum


class AssetType(str, Enum):
    building = "BUILDING"
    creature = "CREATURE"
    vehicle = "VEHICLE"
    adventure = "ADVENTURE"
