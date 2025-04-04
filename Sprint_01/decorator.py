def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def text_conact_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + " Concated text example"
    return wrapper


@uppercase_decorator
@text_conact_decorator
def get_input(input_text: str):
    return input_text


print(get_input("Test message"))
