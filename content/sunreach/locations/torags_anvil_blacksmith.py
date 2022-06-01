from content.sunreach.actors.torag_blacksmith import ToragTheBlacksmith
from model.location import Location
from content.location_types import LocationTypes

class ToragsAnvilBlacksmith(Location):

    natural_id = "torags_anvil_blacksmith"

    def __init__(self):
        Location.__init__(
            self,
            self.natural_id,
            "Torag's Anvil",
            """Torag's is a work smith, but he can still make a sword as heavy as any other. Amour maybe not so much.
The blacksmith mainly provides tools for the farmers and woodsmen of the village.
There is a sign offering to buy any ores, or scrap metal brought in.""",
            LocationTypes.blacksmith,
            True,
            [],
            [
                ToragTheBlacksmith()
            ]
        )
