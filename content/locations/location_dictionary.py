import re

from content.locations.sunreach.sunreach_village import SunreachVillage
from content.locations.sunreach.lodestone_inn import LodestoneInn
from content.locations.sunreach.torags_anvil_blacksmith import ToragsAnvilBlacksmith

default_location_id = SunreachVillage.natural_id

locations = {
    SunreachVillage.natural_id: SunreachVillage(),
    LodestoneInn.natural_id: LodestoneInn(),
    ToragsAnvilBlacksmith.natural_id: ToragsAnvilBlacksmith()
}

class LocationDictionary:

    def get_default_location():
        return locations[default_location_id]

    def find_location_by_id(location_id):
        if location_id in locations:
            return locations[location_id]
        return None

    def find_location_by_display_name(display_name):
        remove_specials_regex = "[^a-zA-Z0-9 ]"
        clean_name = re.sub(remove_specials_regex, "", display_name).lower()

        for location in locations.values():
            location_clean_name = re.sub(remove_specials_regex, "", location.display_name).lower()
            if location_clean_name == clean_name:
                return location
                
        return None
