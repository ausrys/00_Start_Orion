import psycopg2


class DatabaseSingleton:
    _instance = None

    def __new__(cls, db_name):
        if cls._instance is None:
            # Call the superclass's __new__ method to create the instance
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            # Define attributes explicitly to avoid linter warnings
            cls._instance.db_name = db_name
            cls._instance.connection = psycopg2.connect(
                host="localhost", dbname='postgres', user='postgres',
                password='lopinis123', port='5432')
            cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def __init__(self, db_name):
        # Initialize these attributes only if they are not set
        if not hasattr(self, 'connection'):
            self.db_name = db_name
            self.connection = psycopg2.connect(db_name)
            self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
