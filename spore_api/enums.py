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


class AssetSubtype(int, Enum):
    # CREATURE
    animals = 501095725504
    tribal = 501095388742
    civ = 501083781321
    space = 501095312644
    captains = 501095829971

    # BUILDING
    city_hall = 0
    house = 0
    factory = 0
    entertainment = 0

    # VEHICLE
    military = 0
    economic = 0
    religious = 0
    colony = 0
    land = 2597835946
    air = 0
    sea = 0
    spaceship = 0

    # ADVENTURE
    attack = 0
    collect = 0
    defend = 0
    explore = 0
    puzzle = 0
    quest = 0
    socialize = 0
    story = 0
    template = 0
    no_Genre = 0



