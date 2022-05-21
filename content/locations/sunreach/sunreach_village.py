from content.locations.location_types import LocationTypes

from content.locations.sunreach.lodestone_inn import LodestoneInn

class SunreachVillage:
    natural_id = "sunreach_village"
    display_name = "Sunreach Village"
    description = "TODO: Add a description"
    location_type = LocationTypes.village
    is_interior = False
    sub_locations = [
        LodestoneInn
    ]