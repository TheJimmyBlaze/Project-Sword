
class Help:

    async def handle_command(self, command, message):
        if command[0] in ["help", "hlp", "h", "?"]:
            print("Handling Help command...")
            await self.__print_help(message)
            return True

        return False
    
    async def __print_help(self, message):
        await message.channel.send("> TODO: Link to a quickstart guide, and the wiki")