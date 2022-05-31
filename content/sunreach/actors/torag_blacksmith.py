
from module.conversation import ConversationNode

class ToragBlacksmith:
    natural_id="torag_blacksmith"
    display_name="Torag"

    async def shop(self, message):
        await message.channel.send("TODO: Make Torag have a shop")
    
    conversation=ConversationNode(
        None,
        "Adventurer, welcome! We have have the Tools you need, theres some weapons around here somewhere too.",
        [
            ConversationNode(
                "[Shop] Show me what you've got for sale.",
                "Certainly",
                None,
                shop
            ),
            ConversationNode(
                "Have you got any quests?",
                "Nope, no-ones implemented quests yet :(",
                None
            )
        ]
    )