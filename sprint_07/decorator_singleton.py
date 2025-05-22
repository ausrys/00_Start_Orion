def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(
                f"[singleton decorator] Creating new instance of {cls.__name__}")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(
                f"[singleton decorator] Using existing instance of {cls.__name__}")
        return instances[cls]

    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self):
        self.connected = False

    def connect(self):
        if not self.connected:
            print("[DatabaseConnection] Connecting to database...")
            self.connected = True
        else:
            print("[DatabaseConnection] Already connected.")

    def disconnect(self):
        if self.connected:
            print("[DatabaseConnection] Disconnecting...")
            self.connected = False


def main():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.connect()
    db2.connect()

    print("DB1 is DB2?", db1 is db2)  # True

    db1.disconnect()


if __name__ == "__main__":
    main()
