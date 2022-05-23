from ast import Assert
from content.locations.location_dictionary import LocationDictionary

class Location:
    def __init__(self, connection, interpreter, transactor, door_index):
        self.connection = connection
        self.interpreter = interpreter
        self.transactor = transactor
        self.door_index = door_index

    async def handle_command(self, command, message):
        if command[0] in ["location", "loc", "lc"]:
            if len(command) > 1 and command[1] in ["info"]:
                if len(command) > 2:
                    await self.__describe_command_location(command, message)
                    return True

                await self.__describe_current_location(message)
                return True

        return False

    async def __describe_current_location(self, message):
        location = await self.get_character_location(message.author.id)

        location_message = "> You are in...\n> \n"
        location_message += self.__describe_location(location)
        await message.channel.send(location_message)

    async def __describe_command_location(self, command, message):
        if len(command) < 3:
            raise AssertionError("Unable to find location, message does not contain enough commands")

        command_location = self.interpreter.get_command_suffix(command, message, 2)

        location = LocationDictionary.find_location_by_display_name(command_location)
        if location == None:
            await message.channel.send(f"> There is no location: '{command_location}'")
            return

        location_message = self.__describe_location(location, False)
        await message.channel.send(location_message)

    def __describe_location(self, location, verbose = True):

        # Describe location
        location_description = f">>> ***{location.display_name}***"
        location_description += f"\n`{location.description}`"

        # If not verbose, just print the description
        if not verbose:
            return location_description

        # Describe adjacent locations
        location_description += "\n"
        doors = self.door_index.get_doors_for_location(location.natural_id)
        location_description += f"\nYou can see {len(doors)} nearby {'location' if len(doors) == 1 else 'locations'}:"

        for door in doors:
            location_description += f"\n`{door.display_name}`"

        return location_description

    async def get_character_location(self, discord_id):
        print(f"Getting location for user_id: {discord_id}")
        location_row = self.connection.get_query(get_character_location, [discord_id])

        location = LocationDictionary.get_default_location()
        if len(location_row) > 0:
            location_id = location_row[0][0]
            if location_id != None:
                location = LocationDictionary.find_location_by_id(location_id)

        print(f"User_id: {discord_id} is in location: {location.natural_id}")
        return location

get_character_location = """
SELECT location_id FROM character WHERE discord_id = ?
"""