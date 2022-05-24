from content.locations.location_dictionary import locations

class DoorIndex:
    def __init__(self):
        self.index = self.__build_index()
        print("Door index initialized")

    def __build_index(self):
        index = {}
        # For every location, calculate it's doors
        for location in locations.values():
            # A location declaratively has sub_locations as doors
            doors = location.sub_locations

            # A location implicitly has all locations that list the location as a sub_location
            # For every location, check to see if this location is a sub_location of it
            for parent_location in locations.values():
                # If the location is this location, skip it
                if location.natural_id == parent_location.natural_id:
                    continue
                
                # If the location has sub_locations and this location is listed as a sub_location, add the location to this locations doors
                if len(parent_location.sub_locations) > 0:
                    for parent_sub_location in parent_location.sub_locations:
                        if parent_sub_location.natural_id == location.natural_id:
                            doors.append(parent_location)
                            break

            # Add all the doors for this location to the index
            index[location.natural_id] = doors

        # Return the index
        return index

    def get_doors_for_location(self, location_id):
        return self.index[location_id]
