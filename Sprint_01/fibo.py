# Python program to display the Fibonacci sequence
def log_odd_numbers(func):
    # This decorator will log only odd Fibonacci numbers
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:  # Check if the number is odd
            print("Not an odd number")
        else:
            print(result)
        return result
    return wrapper


class Fibo:

    def __init__(self) -> None:
        self.cache: dict = {}

    @log_odd_numbers
    def recur_fibo(self, n: int) -> int:
        # Check if the value is already cached
        if n in self.cache:
            return self.cache[n]

        if n <= 1:
            return n
        # Compute and cache the Fibonacci value
        result = self.recur_fibo(n - 1) + self.recur_fibo(n - 2)
        self.cache[n] = result
        return self.cache[n]


Fibonaci: Fibo = Fibo()
for number in range(1, 10):
    Fibonaci.recur_fibo(number)
