import unittest
from arraysearch import algorithms
from arraysearch import data_generator
from arraysearch import constants

test_cases = [
    ([1, 3, 5, 7, 9], 5),
    ([2, 4, 6, 8, 10], 8),
    ([10, 20, 30, 40, 50], 25),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ([], -1)
]

expected_results = [2, 3, -1, 0, 9, -1]


class AlgorithmsTests(unittest.TestCase):
    def test_linear_search(self):
        for i in range(len(test_cases)):
            array, elem = test_cases[i]
            result = algorithms.linear_search(array, elem)
            self.assertEqual(result, expected_results[i])

    def test_binary_search(self):
         for i in range(len(test_cases)):
            array, elem = test_cases[i]
            result = algorithms.binary_search(array, elem)
            self.assertEqual(result, expected_results[i])


    def test_ternary_search(self):
         for i in range(len(test_cases)):
            array, elem = test_cases[i]
            result = algorithms.ternary_search(array, elem)
            self.assertEqual(result, expected_results[i])

if __name__ == "__main__":
    unittest.main()
