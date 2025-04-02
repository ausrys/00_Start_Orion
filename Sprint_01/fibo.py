# Python program to display the Fibonacci sequence
from functools import lru_cache


class Fibo:

    def __init__(self, iterations: int) -> None:
        self.iterrations = iterations

    @lru_cache(maxsize=None)

    def recur_fibo(self, n: int) ->int:

        if n <= 1:
            return n
        else:
            return self.recur_fibo(n - 1) + self.recur_fibo(n - 2)
        
    def display_sequence(self):

        # Check if the number of iterations is valid
        if type(self.iterrations) != int or self.iterrations <= 0:
            print("Plese enter a positive integer")
            return
        print("Fibonacci sequence:")
        for i in range(self.iterrations):
            print(self.recur_fibo(i))
 

Fibonaci: Fibo = Fibo(5)
Fibonaci.display_sequence()
