from datetime import datetime
from datetime import timedelta

from module.help_module import HelpModule
from module.character_module import CharacterModule
from module.location_module import LocationModule

class Interpreter:
    def __init__(self, discord_client, prefix, timeout, connection, transactor, door_index):
        self.discord_client = discord_client

        self.prefix = prefix
        self.timeout = timeout

        self.connection = connection
        self.transactor = transactor
        self.door_index = door_index

        self.help_module = HelpModule()
        self.character_module = CharacterModule(connection, transactor)
        self.location_module = LocationModule(connection, self, transactor, door_index)
        
        print("Interpreter initialized")

    async def __handle_command(self, command, message):
        if await self.help_module.handle_command(command, message):
            return
        if await self.character_module.handle_command(command, message):
            return
        if await self.location_module.handle_command(command, message):
            return

        print(f"Command: {command} is not supported by any modules")

    async def interpret(self, message):
        raw = message.content.strip()
        command = self.__clean(raw)
        if self.__ignore(raw, command, message):
            return

        if raw.startswith(self.prefix):
            print(f"Interpreting command: '{raw}' for user: {message.author}")
            self.transactor.clear_transaction(message.author.id)
            await self.__handle_command(command, message)
            return

        transaction = self.transactor.find_transaction(message.author.id)
        if transaction is not None:
            if transaction.timestamp + timedelta(seconds=self.timeout) < datetime.now():
                self.transactor.clear_transaction(message.author.id)
                print("An expired transaction has been cleared")

                await message.channel.send(f"> Your {transaction.description} command has timed out.")
                return
            
            print(f"Processing transaction response: {transaction.description}, {raw}")
            await transaction.function(message, transaction.state)
            return

    def __ignore(self, raw, command, message):
        if raw == self.prefix:
            return True
        if len(command) == 0:
            return True
        if message.author.id == self.discord_client.user:
            return True

        return False
            
    def __clean(self, raw):
        no_prefix = raw.replace(self.prefix, "")
        case_variant = no_prefix.split()
        lower_case = map(lambda cmd: cmd.lower(), case_variant)
        command = list(lower_case)
        return command

    def get_command_suffix(self, command, message, count):
        raw = message.content
        working = raw.replace(self.prefix, "")

        for i in range(count):
            working = working.replace(command[i], "")

        suffix = working.strip()
        return suffix
