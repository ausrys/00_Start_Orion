from data_simulation import populate_data
from sql_queries import create_tables


if __name__ == "__main__":
    create_tables()
    populate_data(user_count=10, history_per_user=5, transactions_per_user=3)
