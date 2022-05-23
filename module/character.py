import re
from command.transactor import Transaction
from command.transactor import DefaultState

create_character_transaction = "Create Character"

class Character:
    def __init__(self, connection, transactor):
        self.connection = connection
        self.transactor = transactor

    async def handle_command(self, command, message):
        if command[0] in ["character", "char", "ch"]:
            if len(command) > 1 and command[1] == "create":
                await self.__create_character(message)
                return True

        return False

    async def __create_character(self, message):
        character_rows = self.connection.get_query(get_existing_character, [message.author.id])
        existing_character = len(character_rows) > 0 and character_rows[0][0]
        if existing_character:
            await message.channel.send(f"> You've been here before. I remember you as {existing_character}.")
            return

        await message.channel.send("> Ah, a new Adventurer. What is your name?")
        transaction = Transaction(create_character_transaction, self.__set_character_name, DefaultState())
        self.transactor.add_transaction(message.author.id, transaction)

    async def __set_character_name(self, message, state):
        name = message.content.strip()

        name_regex = "^[A-z'-]{2,25}( [A-z'-]{2,25})?$"
        pattern = re.compile(name_regex)

        if pattern.match(name):
            print(f"Registering new user: {message.author} with character: {name}...")
            self.connection.execute_query(insert_new_character, [message.author.id, name])

            await message.channel.send(f"> Welcome {name}, a grand adventure awaits.")
            self.transactor.clear_transaction(message.author.id)
            return
        
        await message.channel.send(f"> The name '{name}' is too complex, it may only contain letters apostrophes hyphens and a single space. Try another name instead.")
        

get_existing_character = """
SELECT display_name FROM character WHERE discord_id = ?
"""

insert_new_character = """
INSERT INTO character (
    discord_id,
    display_name
) VALUES (
    ?,
    ?
);
"""