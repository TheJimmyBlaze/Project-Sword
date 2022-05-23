from content.locations.location_dictionary import LocationDictionary

class Location:
    def __init__(self, connection, transactor, door_index):
        self.connection = connection
        self.transactor = transactor
        self.door_index = door_index

    async def handle_command(self, command, message):
        if command[0] in ["location", "loc", "lc"]:
            if len(command) >= 1 and command[1] in ["info", "where"]:
                await self.__describe_location(message)
                return True

        return False

    async def __describe_location(self, message, verbose = True):
        location = await self.get_character_location(message.author.id)

        # Describe location
        locationDescription = f"> You're currently at {location.display_name}."
        locationDescription += f"\n> `{location.description}`"

        # If not verbose, just print the description
        if not verbose:
            await message.channel.send(locationDescription)
            return

        # Describe adjacent locations
        locationDescription += "\n> "
        doors = self.door_index.get_doors_for_location(location.natural_id)
        locationDescription += f"\n> There is {len(doors)} nearby locations:"

        for door in doors:
            locationDescription += f"\n> `{door.display_name}`"

        await message.channel.send(locationDescription)

    async def get_character_location(self, discord_id):
        print(f"Getting location for user_id: {discord_id}")
        location_row = self.connection.get_query(get_character_location, [discord_id])

        location_id = None
        if len(location_row) > 0:
            location_id = location_row[0][0]
        location = LocationDictionary.find_location(location_id)

        print(f"User_id: {discord_id} is in location: {location.natural_id}")
        return location

get_character_location = """
SELECT location_id FROM character WHERE discord_id = ?
"""