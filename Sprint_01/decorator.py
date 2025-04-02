def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_decorator
def get_input(input: str):
    return input


print(get_input("Test message"))
