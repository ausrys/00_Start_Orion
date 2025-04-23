import random
from datetime import timedelta

from faker import Faker

from db_connection import DatabaseSingleton

fake = Faker()


def populate_data(user_count=10, history_per_user=5, transactions_per_user=3):
    db = DatabaseSingleton('postgres')
    cursor = db.get_cursor()

    # 1. Insert fake transaction types
    transaction_types = ['deposit', 'withdrawal', 'transfer', 'payment']
    type_ids = []

    for t_type in transaction_types:
        cursor.execute(
            "INSERT INTO type_transactions (type) VALUES (%s) RETURNING id;",
            (t_type,))
        type_ids.append(cursor.fetchone()[0])

    # 2. Insert fake users
    user_ids = []
    for _ in range(user_count):
        name = fake.name()
        email = fake.email()
        cursor.execute(
            "INSERT INTO \"user\" (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        user_ids.append(cursor.fetchone()[0])

    # 3. Insert history records per user
    for user_id in user_ids:
        for _ in range(history_per_user):
            url = fake.url()
            date = fake.date_time_this_year()
            time_spend = date + timedelta(minutes=random.randint(1, 30))
            cursor.execute(
                '''INSERT INTO history (user_id, url, date, time_spend)
                VALUES (%s, %s, %s, %s);''',
                (user_id, url, date, time_spend)
            )

    # 4. Insert transactions and store last_operation_id for balance
    for user_id in user_ids:
        last_op_id = None
        for _ in range(transactions_per_user):
            transaction_type = random.choice(type_ids)
            balance_change = round(random.uniform(-100.0, 1000.0), 2)
            date = fake.date_time_this_year()
            time = date + timedelta(seconds=random.randint(0, 3600))
            cursor.execute('''
                INSERT INTO transactions (user_id, transaction_type,
                balance_change, date, time)
                VALUES (%s, %s, %s, %s, %s) RETURNING id;
            ''', (user_id, transaction_type, balance_change, date, time))
            last_op_id = cursor.fetchone()[0]

        # 5. Insert balance for user
        active_balance = round(random.uniform(0, 5000), 2)
        cursor.execute('''
            INSERT INTO balance (user_id, active_balance, last_operation_id)
            VALUES (%s, %s, %s);
        ''', (user_id, active_balance, last_op_id))

    db.commit()
    print("Fake data inserted successfully.")
