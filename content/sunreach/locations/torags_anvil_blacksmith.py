from content.location_types import LocationTypes

class ToragsAnvilBlacksmith:
    natural_id = "torags_anvil_blacksmith"
    display_name = "Torag's Anvil"
    description = """Torag's is a work smith, but he can still make a sword as heavy as any other. Amour maybe not so much.
The blacksmith mainly provides tools for the farmers and woodsmen of the village.
There is a sign offering to buy any ores, or scrap metal brought in."""
    location_type = LocationTypes.blacksmith
    is_interior = True
    sub_locations = []
