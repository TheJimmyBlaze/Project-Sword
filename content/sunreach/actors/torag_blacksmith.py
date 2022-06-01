
from model.actor import Actor
from content.actor_professions import ActorProfessions
from model.conversation import ConversationNode

class ToragTheBlacksmith(Actor):
    
    natural_id = "torag_blacksmith"

    async def shop(self, message):
        await message.channel.send("TODO: Make Torag have a shop")
    
    def __init__(self):
        Actor.__init__(
            self,
            self.natural_id,
            "Torag",
            ActorProfessions.blacksmith,
            ConversationNode(
                None,
                "Adventurer, welcome! We have have the Tools you need, theres some weapons around here somewhere too.",
                [
                    ConversationNode(
                        "[Shop] Show me what you've got for sale.",
                        "Certainly",
                        None,
                        self.shop
                    ),
                    ConversationNode(
                        "Have you got any quests?",
                        "Nope, no-ones implemented quests yet :(",
                        None
                    )
                ]
            )
        )