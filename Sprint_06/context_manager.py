import sqlite3
from functools import wraps

# custom file context manager


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# # loading a file
# with FileManager('Sprint_06/sprint_06.txt', 'r') as f:
#     print(f.read())

# print(f.closed)


def with_file(filename, mode):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with FileManager(filename, mode) as file:
                return func(file, *args, **kwargs)
        return wrapper
    return decorator


@with_file('Sprint_06/example.txt', 'w')
def write_to_file(f, text):
    f.write(text)


# write_to_file("Hello from context manager decorator!")


class SQLiteDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor  # Expose cursor for operations like execute()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()


# Create table (only needs to be done once)
with SQLiteDB('Sprint_06/example.db') as cur:
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )''')

# Insert a record
with SQLiteDB('Sprint_06/example.db') as cur:
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

# Fetch records
with SQLiteDB('Sprint_06/example.db') as cur:
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    print(users)
