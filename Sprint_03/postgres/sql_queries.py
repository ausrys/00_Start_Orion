from db_connection import DatabaseSingleton


def create_tables():
    db = DatabaseSingleton('postgres')
    cursor = db.get_cursor()

    # Create tables
    table_sql_statements = [
        '''
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS history (
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            url TEXT,
            date TIMESTAMP,
            time_spend TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES "user"(id)
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS type_transactions (
            id SERIAL PRIMARY KEY,
            type TEXT
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            transaction_type INT NOT NULL,
            balance_change FLOAT,
            date TIMESTAMP,
            time TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES "user"(id),
            FOREIGN KEY (transaction_type) REFERENCES type_transactions(id)
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS balance (
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            active_balance FLOAT,
            last_operation_id INT,
            FOREIGN KEY (user_id) REFERENCES "user"(id),
            FOREIGN KEY (last_operation_id) REFERENCES transactions(id)
        );
        '''
    ]

    for sql in table_sql_statements:
        cursor.execute(sql)

    db.commit()
    print("Tables created successfully.")
