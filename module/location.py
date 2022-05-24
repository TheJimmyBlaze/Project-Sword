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
            # Give info about a location
            if len(command) > 1 and command[1] in ["info"]:
                # Info about a named location
                if len(command) > 2:
                    await self.__describe_command_location(command, message)
                    return True
                # Info about current location
                await self.__describe_current_location(message)
                return True

            # Move to a nearby location 
            if len(command) > 1 and command[1] in ["move"]:
                await self.__move_to_location(command, message)
                return True

        return False

    async def __describe_current_location(self, message):
        # Get the characters current location
        location = self.get_character_location(message.author.id)

        # Describe the location in verbose detail
        location_message = "> You are in...\n> \n"
        location_message += self.__describe_location(location)
        await message.channel.send(location_message)

    async def __describe_command_location(self, command, message):
        # This command can only be used when the command is length 3 or greater
        if len(command) < 3:
            raise AssertionError("Unable to find location, message does not contain enough commands")

        # Get the part of the message that describes the location
        command_location = self.interpreter.get_command_suffix(command, message, 2)

        # Get the location specified in the command
        location = LocationDictionary.find_location_by_display_name(command_location)
        if location == None:
            await message.channel.send(f"> There is no location: '{command_location}'")
            return

        # Briefly describe the location
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

    async def __move_to_location(self, command, message):
        # If the command is too short, ask to specify a location
        if len(command) < 3:
            await message.channel.send("> You must name a nearby location to move to.")
            return

        # Get the characters location, and it's doors
        current_location = self.get_character_location(message.author.id)
        doors = self.door_index.get_doors_for_location(current_location.natural_id)

        # Get the location specified in the command
        command_location = self.interpreter.get_command_suffix(command, message, 2)
        location = LocationDictionary.find_location_by_display_name(command_location)
        if location == None:
            await message.channel.send(f"> There is no location: '{command_location}'")
            return

        # Check if the command location is in the doors list
        can_move_to_location = False
        for door in doors:
            if door.natural_id == location.natural_id:
                can_move_to_location = True
                break

        # If the location is not a door, return an error message
        if not can_move_to_location:
            await message.channel.send(f"> {location.display_name} is too far away. You can only move to nearby locations.")
            return

        # Move the player to the location
        self.set_character_location(message.author.id, location.natural_id)
        await message.channel.send(f"> You are now in {location.display_name}.")

    def get_character_location(self, discord_id):
        # Query the DB for the characters location
        print(f"Getting location for user_id: {discord_id}")
        location_row = self.connection.get_query(get_character_location, [discord_id])

        # Get the location from the ID, if the ID is null return the default location
        location = LocationDictionary.get_default_location()
        location_id = location_row[0][0]
        if location_id == None:
            self.set_character_location(discord_id, location.natural_id)
        else:
            location = LocationDictionary.find_location_by_id(location_id)

        print(f"User_id: {discord_id} is in location: {location.natural_id}")
        return location

    def set_character_location(self, discord_id, location_id):
        # Set the characters location in the DB
        print(f"Setting location for user_id: {discord_id} to: {location_id}")
        self.connection.execute_query(set_character_location, [location_id, discord_id])


get_character_location = """
SELECT location_id FROM character WHERE discord_id = ?
"""

set_character_location = """
UPDATE character SET location_id = ? WHERE discord_id = ?
"""