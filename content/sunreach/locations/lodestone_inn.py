from content.location_types import LocationTypes

class LodestoneInn:
    natural_id = "lodestone_inn"
    display_name = "The Lodestone"
    description = """Drunken and rowdy in the evenings, and lazy with travelers during the day.
The lodestone is as much an Inn as it is a Pub, good drink, cheap food, and rooms to rent.
Adventurers, traders, and locals commonly gather here to discuss business and make deals."""
    location_type = LocationTypes.inn
    is_interior = True
    sub_locations = []