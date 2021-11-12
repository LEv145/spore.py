from enum import Enum


class AssetType(str, Enum):
    building  = "BUILDING"
    creature  = "CREATURE"
    vehicle   = "VEHICLE"
    adventure = "ADVENTURE"
    ufo       = "UFO"


class ViewType(str, Enum):
    top_rated       = "TOP_RATED"
    top_rated_new   = "TOP_RATED_NEW"
    newest          = "NEWEST"
    featured        = "FEATURED"
    maxis_made      = "MAXIS_MADE"
    random          = "RANDOM"
    cute_and_creepy = "CUTE_AND_CREEPY"


class AssetSubtype(int, Enum):
    # CREATURE
    сreature   = 0x9ea3031a  # animal
    tribal     = 0x372e2c04
    civ        = 0xccc35c46
    space      = 0x65672ade
    adventurey = 0x4178b8e8  # captains

    # BUILDING
    city_hall     = 0x99e92f05
    house         = 0x4e3f7777
    factory       = 0x47c10953
    entertainment = 0x72c49181

    # VEHICLE
    military_land  = 0x7d433fad
    military_water = 0x8f963dcb
    military_air   = 0x441cd3e6
    economic_land  = 0xf670aa43
    economic_water = 0x2a5147a9
    economic_air   = 0x1a4e0708
    cultural_land  = 0x9ad7d4aa
    cultural_water = 0x1f2a25b6
    cultural_air   = 0x449c040f
    colony_land    = 0xbc1041e6
    colony_water   = 0xc15695da
    colony_air     = 0x2090a11b
    ufo            = 0x98e03c0d

    # ADVENTURE
    attack    = 0x287adcdc
    collect   = 0x25a6ea6e
    defend    = 0xc34c5e14
    explore   = 0x37fd4e0d
    puzzle    = 0xe27ddad4
    quest     = 0xc422519e
    socialize = 0xfb734cd1
    story     = 0xb4707f8f
    template  = 0x27818fe6
    no_genre  = 0x20790816
