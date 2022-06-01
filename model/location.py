
class Location:
    def __init__(
        self,
        natural_id,
        display_name,
        description,
        location_type,
        is_interior,
        sub_locations,
        actors
    ):
        self.natural_id = natural_id
        self.display_name = display_name
        self.description = description
        self.location_type = location_type
        self.is_interior = is_interior
        self.sub_locations = sub_locations
        self.actors = actors