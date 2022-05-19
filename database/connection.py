import sqlite3
from sqlite3 import Error

class DbConnection:
    def __init__(self, path):
        self.connection = None
        try:
            print(f"Connecting to DB: {path}...")
            self.connection = sqlite3.connect(path)
            print(f"Connection to DB: {path} established")

        except Error as e:
            print(f"DB setup error: {e}")
            raise e

    def execute_query(self, query, args = [], silent = False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, args)
            self.connection.commit()
        except Error as e:
            if not silent:
                print(f"DB execution error: {e}, in query: {query}, args: {args}")
            raise e

    def get_query(self, query, args = [], silent = False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, args)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            if not silent:
                print(f"DB query error: {e}, in query: {query}, args: {args}")
            raise e
            