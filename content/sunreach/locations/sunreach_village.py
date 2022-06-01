from model.location import Location
from content.location_types import LocationTypes

from content.sunreach.locations.lodestone_inn import LodestoneInn
from content.sunreach.locations.torags_anvil_blacksmith import ToragsAnvilBlacksmith

class SunreachVillage(Location):

    natural_id = "sunreach_village"

    def __init__(self):
        Location.__init__(
            self,
            self.natural_id,
            "Sunreach Village",
            """Sunreach sits within the Archon Forests, but much of the nearby forest has made way to farmland.
The village makes a good trade of grain and vegetables, with the road to the north being heavily trafficked by trade caravans.
The center of Sunreach opens to a cobbled town square, with market stalls surrounding a fresh water fountain.
There are some stores, a few houses, and the castle, but Sunreach is a small but bustling village.""",
            LocationTypes.town_center,
            False,
            [
                LodestoneInn(),
                ToragsAnvilBlacksmith()
            ],
            []
        )