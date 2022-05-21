from datetime import datetime
from datetime import timedelta

from module.help import Help
from module.character import Character
from module.location import Location

class Interpreter:
    def __init__(self, discord_client, prefix, timeout, connection, transactor):
        self.discord_client = discord_client

        self.prefix = prefix
        self.timeout = timeout

        self.transactor = transactor
        self.connection = connection

        self.help_module = Help()
        self.character_module = Character(connection, transactor)
        self.location_module = Location(connection, transactor)
        
        print("Interpreter initialized")

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

    async def __handle_command(self, command, message):
        if await self.help_module.handle_command(command, message):
            return
        if await self.character_module.handle_command(command, message):
            return
        if await self.location_module.handle_command(command, message):
            return

        print(f"Command: {command} is not supported by any modules")

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
