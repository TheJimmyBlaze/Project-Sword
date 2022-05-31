
class ConversationNode:
    def __init__(self, prompt, dialogue, paths, action = None):
        self.prompt = prompt
        self.dialogue = dialogue
        self.paths = paths
        self.action = action

class Conversation:
    def __init__(self, transactor):
        self.transactor = transactor

    async def handle_command(self, command, message):
        if command[0] in ['talk']:
            pass