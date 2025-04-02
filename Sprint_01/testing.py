import unittest
from fibo import Fibo

class TestFibo(unittest.TestCase):
    
    def test_fibo_base_case(self):
        # Testing base cases of Fibonacci
        fibo = Fibo(5)
        self.assertEqual(fibo.recur_fibo(0), 0)  # Fibonacci(0) should return 0
        self.assertEqual(fibo.recur_fibo(1), 1)  # Fibonacci(1) should return 1
    
    def test_fibo_recursive(self):
        # Testing some recursive cases of Fibonacci
        fibo = Fibo(5)
        self.assertEqual(fibo.recur_fibo(2), 1)  # Fibonacci(2) should return 1
        self.assertEqual(fibo.recur_fibo(3), 2)  # Fibonacci(3) should return 2
        self.assertEqual(fibo.recur_fibo(4), 3)  # Fibonacci(4) should return 3

    def test_invalid_iterations(self):
        # Testing when iterations are less than or equal to zero
        fibo = Fibo(0)
        with self.assertRaises(ValueError):
            fibo.display_sequence()  # This should raise an error when the iteration is 0 or less
if __name__ == '__main__':
    unittest.main()
