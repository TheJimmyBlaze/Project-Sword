from datetime import datetime
from datetime import timezone
from sqlite3 import Error
from database.migrations.migration_0001 import Migration0001

migrations = [
    Migration0001
]

class Schema:
    def __init__(self, connection):
        self.connection = connection

    def prepare(self):
        print("Preparing schema...")

        migration_version = self.__get_migration_version()
        print(f"Current migration version is: {migration_version}")

        newlyAppliedMigrations = 0
        lastAppliedMigration = 0

        for migration in migrations:

            migration = migration(self.connection)
            version = migration.version()

            if version > migration_version:
                print(f"Applying migration version: {version}...")
                migration.apply()
                self.__set_migration_version(version)
                lastAppliedMigration = version
                newlyAppliedMigrations += 1

        if newlyAppliedMigrations > 0:
            print(f"Applied: {newlyAppliedMigrations} new migration(s)")
            print(f"New migration version is: {lastAppliedMigration}")
        else:
            print("No migrations to apply")

        print("Schema ready")

    def __get_migration_version(self):
        try: 
            migration_version_rows = self.connection.get_query(get_migration_version, silent=True)
            migration_version = migration_version_rows[0][0]
            return migration_version
        except Error:
            return 0

    def __set_migration_version(self, version):
        self.connection.execute_query(set_migration_version, [version, datetime.now(timezone.utc)])

get_migration_version = """
SELECT migration_version FROM version ORDER BY migration_version desc LIMIT 1;
"""

set_migration_version = """
INSERT INTO version VALUES (?, ?);
"""