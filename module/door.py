from content.locations.location_dictionary import locations

class DoorIndex:
    def __init__(self):
        self.index = self.__build_index()
        print("Door index initialized")

    def __build_index(self):
        index = {}
        for location in locations.values():
            doors = location.sub_locations

            for parent_location in locations.values():
                if location.natural_id == parent_location.natural_id:
                    continue
                
                if len(parent_location.sub_locations) > 0:
                    for parent_sub_location in parent_location.sub_locations:
                        if parent_sub_location.natural_id == location.natural_id:
                            doors.append(parent_location)
                            break

            index[location.natural_id] = doors
        return index

    def get_doors_for_location(self, location_id):
        return self.index[location_id]


