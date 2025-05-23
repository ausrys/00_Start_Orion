class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Usage
p = Person("Alice", 30)
print(p.name)  # Alice
print(p.age)   # 30
