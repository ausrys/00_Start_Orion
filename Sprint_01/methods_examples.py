class MyClass:
    count = 0

    def __init__(self, name):
        self.name = name
        MyClass.count += 1  # Increment count when a new instance is created

    # Static method: doesn't require access to the class or instance. It can
    # only be called on the class it self, not on the object.
    @staticmethod
    def greet():
        return "Hello from the static method!"

    # Class method: takes the class as the first argument
    # Can be called on the object or the class itself
    @classmethod
    def get_instance_count(cls):
        return f"There are {cls.count} instances of MyClass."


obj1 = MyClass("Alice")
obj2 = MyClass("Bob")

# Calling the static method using the class
print(MyClass.greet())  # Static method doesn't need an instance

# Calling the class method using the class
# Class method can be called without an instance
print(MyClass.get_instance_count())

# Calling the class method using an instance
# Class method can also be called from an instance
print(obj1.get_instance_count())
