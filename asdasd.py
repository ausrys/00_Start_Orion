def log_odd_numbers(func):
    # This decorator will log only odd Fibonacci numbers
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 != 0:  # Check if the number is odd
            print(f"Odd Fibonacci number: {result}")
            func(*args, **kwargs)
    return wrapper


@log_odd_numbers
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Test the Fibonacci function with logging only odd numbers
num_terms = 4  # Define how many Fibonacci numbers to compute
for i in range(num_terms):
    fibonacci(i)
