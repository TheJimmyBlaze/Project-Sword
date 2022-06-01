
class ConversationModule:
    def __init__(self, transactor):
        self.transactor = transactor

    async def handle_command(self, command, message):
        if command[0] in ['talk']:
            pass