# Python program to display the Fibonacci sequence
def odd_return_decorator(func):
    def wrapper(self, n):
        result = func(self, n)
        if result % 2 != 0:  # Check if the result is odd
            return result
        else:
            # If the result is even, return the next Fibonacci number
            return func(self, n + 1) if n + 1 <= self.iterations else result
    return wrapper


class Fibo:

    def __init__(self, iterations: int) -> None:
        self.iterations = iterations
        self.cache: dict = {}

    # @odd_return_decorator  # Apply the decorator to recur_fibo
    def recur_fibo(self, n: int) -> int:
        # Check if the value is already cached
        if n in self.cache:
            return self.cache[n]

        if n <= 1:
            return n
        else:
            # Compute and cache the Fibonacci value
            self.cache[n] = self.recur_fibo(n - 1) + self.recur_fibo(n - 2)
            return self.cache[n]

    def display_sequence(self):
        # Check if the number of iterations is valid
        if not isinstance(self.iterations, int) or self.iterations <= 0:
            raise ValueError("Error: Invalid input, provide a number that is\
                            type of integer and is equal or greater than 1")
        # print("Fibonacci sequence:")
        for i in range(self.iterations):
            print(self.recur_fibo(i))


Fibonaci: Fibo = Fibo(10)
Fibonaci.display_sequence()
