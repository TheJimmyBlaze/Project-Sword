from datetime import datetime

class DefaultState:
    pass

class Transaction:
    def __init__(self, description, function, state):
        self.description = description
        self.function = function
        self.state = state
        self.timestamp = datetime.now()

class Transactor:
    def __init__(self):
        self.transactions = {}
        print("Transactor initialized")

    def clear_transaction(self, discord_id):
        if discord_id in self.transactions.keys():
            del self.transactions[discord_id] 

    def add_transaction(self, discord_id, transaction):
        self.transactions[discord_id] = transaction

    def find_transaction(self, discord_id):
        if discord_id in self.transactions.keys():
            return self.transactions[discord_id]