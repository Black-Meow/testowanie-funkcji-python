import unittest

# Zadanie 1: Testowanie funkcji dodawania
def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_positive_and_negative(self):
        self.assertEqual(add_numbers(5, -3), 2)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-4, -6), -10)

    def test_with_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)


# Zadanie 2: Testowanie funkcji sprawdzającej parzystość
def is_even(n):
    return n % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(0))

    def test_odd_numbers(self):
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-1))

    def test_large_even(self):
        self.assertTrue(is_even(1000000))


# Zadanie 3: Testowanie funkcji konwertującej temperaturę
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_standard_temperatures(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14)

    def test_large_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(1000), 1832)

    def test_zero_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)


# Zadanie 4: Testowanie funkcji obliczającej silnię
def factorial(n):
    if n < 0:
        raise ValueError("Negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_larger_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_performance_large_number(self):
        self.assertTrue(factorial(20) > 0)


# Zadanie 5: Testowanie funkcji sprawdzającej, czy liczba jest liczbą pierwszą
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        for prime in [2, 3, 5, 7]:
            self.assertTrue(is_prime(prime))

    def test_non_prime_numbers(self):
        for non_prime in [4, 6, 8, 9]:
            self.assertFalse(is_prime(non_prime))

    def test_numbers_below_two(self):
        for n in [-5, 0, 1]:
            self.assertFalse(is_prime(n))

    def test_large_prime(self):
        self.assertTrue(is_prime(7919))


if __name__ == "__main__":
    unittest.main()
