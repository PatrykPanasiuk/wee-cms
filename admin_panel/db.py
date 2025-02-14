import sqlite3

class Database:
    """Handles SQLite3 connection for PyQt6."""
    
    def __init__(self, db_path="../database/data.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        """Executes an SQL query."""
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query):
        """Fetches all rows from a query."""
        self.cursor.execute(query)
        return self.cursor.fetchall()