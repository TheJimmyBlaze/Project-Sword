from content.locations.location_types import LocationTypes

from content.locations.sunreach.lodestone_inn import LodestoneInn
from content.locations.sunreach.torags_anvil_blacksmith import ToragsAnvilBlacksmith

class SunreachVillage:
    natural_id = "sunreach_village"
    display_name = "Sunreach Village"
    description = "TODO: Add a description"
    location_type = LocationTypes.village
    is_interior = False
    sub_locations = [
        LodestoneInn(),
        ToragsAnvilBlacksmith()
    ]