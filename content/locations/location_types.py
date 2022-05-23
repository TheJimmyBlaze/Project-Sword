
village = "location_village"
inn = "location_inn"
blacksmith = "location_blacksmith"

icons = {
    village: ":circus_tent:",
    inn: ":beers:",
    blacksmith: ":dagger:"
}

class LocationTypes:

    def get_icon(location_type):
        if location_type in icons:
            return icons[location_type]
        return None