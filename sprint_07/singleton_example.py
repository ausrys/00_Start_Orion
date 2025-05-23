class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialize any attributes here if needed
            cls._instance.value = 42
        return cls._instance


# Usage example
a = Singleton()
b = Singleton()

print(a is b)  # True, both are the same instance
print(a.value)  # 42
b.value = 100
print(a.value)  # 100, changes reflect in both since they are the same instance
