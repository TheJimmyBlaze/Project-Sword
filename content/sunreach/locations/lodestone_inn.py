from model.location import Location
from content.location_types import LocationTypes

class LodestoneInn(Location):

    natural_id = "lodestone_inn"

    def __init__(self):
        Location.__init__(
            self,
            self.natural_id,
            "The Lodestone",
            """Drunken and rowdy in the evenings, and lazy with travelers during the day.
The lodestone is as much an Inn as it is a Pub, good drink, cheap food, and rooms to rent.
Adventurers, traders, and locals commonly gather here to discuss business and make deals.""",
            LocationTypes.inn,
            True,
            [],
            []
        )