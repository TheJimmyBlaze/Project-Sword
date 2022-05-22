import sys
import discord

from command.interpreter import Interpreter
from command.transactor import Transactor
from database.connection import DbConnection
from database.schema import Schema

from module.door import DoorIndex

token_path = '.token'
discord_client = discord.Client()

db_path = "project_sword.sqlite"
db_connection = None

transactor = None

command_prefix = "."
command_timeout = 30 # Seconds
interpreter = None

door_index = None

# On ready setup all required resources
@discord_client.event
async def on_ready():
    print("Initializing...")

    print(f"Logged in as '{discord_client.user}'")

    try:
        global db_connection
        db_connection = DbConnection(db_path)
        Schema(db_connection).prepare()

        global transactor
        transactor = Transactor()

        global interpreter
        interpreter = Interpreter(discord_client, command_prefix, command_timeout, db_connection, transactor)

        global door_index
        door_index = DoorIndex()
        
    except BaseException as ex:
        print("An critical error occurred during startup, Project-Sword could not start")
        print(f"Error: {ex}")
        sys.exit()

    print("Your Sword is ready!\n")

# On message send the data to the interpreter to handle
@discord_client.event
async def on_message(message):
    try:
        await interpreter.interpret(message)

    except BaseException as ex:
        print(f"An error occurred interpreting the message: '{message.content}'")
        print(f"Error: {ex}")

# Read the token and start the server
print("Launching Project-Sword...")
try:
    print("Loading token...")

    with open(token_path, "r") as file:
        token = file.read().replace("\n", "")
        print("Connecting discord client...")
        discord_client.run(token)

except OSError:
    print(f"Unable to load Discord Bot Token expected in file: '{token_path}'")
    sys.exit()