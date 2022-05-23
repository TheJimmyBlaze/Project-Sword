from content.locations.location_types import LocationTypes
from content.locations.sunreach.sunreach_village import SunreachVillage
from content.locations.sunreach.lodestone_inn import LodestoneInn
from content.locations.sunreach.sunreach_village import SunreachVillage

default_location_id = SunreachVillage.natural_id

locations = {
    SunreachVillage.natural_id: SunreachVillage(),
    LodestoneInn.natural_id: LodestoneInn()
}

class LocationDictionary:

    def get_default_location():
        return locations[default_location_id]

    def find_location_by_id(location_id):
        if location_id in locations:
            return locations[location_id]
        return None

    def find_location_by_display_name(display_name):
        for location in locations.values():
            if location.display_name.lower() == display_name.lower():
                return location
        return None
