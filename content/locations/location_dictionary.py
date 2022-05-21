from content.locations.location_types import LocationTypes
from content.locations.sunreach.sunreach_village import SunreachVillage
from content.locations.sunreach.lodestone_inn import LodestoneInn
from content.locations.sunreach.sunreach_village import SunreachVillage

default_location_id = SunreachVillage.natural_id

locations = {
    SunreachVillage.natural_id: SunreachVillage,
    LodestoneInn.natural_id: LodestoneInn
}

class LocationDictionary:

    def find_location(location_id):

        location = locations[default_location_id]
        if location_id in locations:
            location = locations[location_id]

        return location()