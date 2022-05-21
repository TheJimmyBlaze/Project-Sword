from content.locations.location_dictionary import LocationDictionary

class Location:
    def __init__(self, connection, transactor):
        self.connection = connection
        self.transactor = transactor

    async def handle_command(self, command, message):
        if command[0] in ["location", "loc", "lc"]:
            if command[1] in ["info", "where"]:
                await self.__describe_location(message)
                return True

        return False

    async def __describe_location(self, message):
        location = await self.get_character_location(message.author.id)
        await message.channel.send(f"> You're currently at {location.display_name}.")

    async def get_character_location(self, discord_id):
        print(f"Getting location for user_id: {discord_id}")
        location_row = self.connection.get_query(get_character_location, [discord_id])

        location_id = None
        if len(location_row) > 0:
            location_id = location_row[0][0]

        print(f"User_id: {discord_id} is in location: {location_id}")
        location = LocationDictionary.find_location(location_id)
        return location

get_character_location = """
SELECT location_id FROM character WHERE discord_id = ?
"""