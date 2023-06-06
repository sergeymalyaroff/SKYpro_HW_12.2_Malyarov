import unittest
from utils import arrs

class ArrsTestCase(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        index = 2
        default_value = "Not found"
        expected_value = 3

        result = arrs.get(array, index, default=default_value)
        self.assertEqual(result, expected_value)

    def test_get_non_existing_index(self):
        array = [1, 2, 3, 4, 5]
        index = 5
        default_value = "Not found"
        expected_value = "Not found"

        result = arrs.get(array, index, default=default_value)
        self.assertEqual(result, expected_value)

    def test_my_slice_default_arguments(self):
        array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        result = arrs.my_slice(array)
        self.assertEqual(result, expected_result)

    def test_my_slice_with_start_index(self):
        array = [1, 2, 3, 4, 5]
        start = 2
        expected_result = [3, 4, 5]

        result = arrs.my_slice(array, start=start)
        self.assertEqual(result, expected_result)

    def test_my_slice_with_end_index(self):
        array = [1, 2, 3, 4, 5]
        end = 3
        expected_result = [1, 2, 3]

        result = arrs.my_slice(array, end=end)
        self.assertEqual(result, expected_result)

    def test_my_slice_with_negative_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        start = -3
        end = -1
        expected_result = [3, 4]

        result = arrs.my_slice(array, start=start, end=end)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
