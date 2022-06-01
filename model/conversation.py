
class ConversationNode:
    def __init__(self, prompt, dialogue, paths, action = None):
        self.prompt = prompt
        self.dialogue = dialogue
        self.paths = paths
        self.action = action