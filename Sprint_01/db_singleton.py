import sqlite3
import threading


class DatabaseSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_name):
        with cls._lock:
            if cls._instance is None:
                # Call the superclass's __new__ method to create the instance
                cls._instance = super(DatabaseSingleton, cls).__new__(cls)
                # Define attributes explicitly to avoid linter warnings
                cls._instance.db_name = db_name
                cls._instance.connection = sqlite3.connect(db_name)
                cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def __init__(self, db_name):
        # Initialize these attributes only if they are not set
        if not hasattr(self, 'connection'):
            self.db_name = db_name
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


# Usage example:
if __name__ == "__main__":
    # Create a singleton instance
    db = DatabaseSingleton("my_database.db")

    # Create a table (if not exists)
    cursor = db.get_cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER)''')

    # Insert data
    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
    db.commit()

    # Retrieve data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    db.close()
