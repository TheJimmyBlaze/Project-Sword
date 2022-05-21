
migration_version = 1

class Migration0001:
    def __init__(self, connection):
        self.connection = connection

    def version(self):
        return migration_version

    def apply(self):
        self.__create_tables()

    def __create_tables(self):
        self.connection.execute_query(create_version_table)
        self.connection.execute_query(create_user_table)

create_version_table = """
CREATE TABLE IF NOT EXISTS version (
    migration_version INTEGER PRIMARY KEY,
    date_applied TEXT NOT NULL
);
"""

create_user_table = """
CREATE TABLE IF NOT EXISTS character (
    identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id TEXT NOT NULL UNIQUE,
    display_name TEXT NOT NULL,
    location_id TEXT NULL
);
"""