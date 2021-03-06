from os import sys, path
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils.helpers import flatten_list, will_it_float, count_truthy, read_csv_to_arrays


class TestHelperMethods(unittest.TestCase):

    def test_flatten_list(self):
        test_case_1 = [[0, 1, 2, 0], [1, 2, 3, 0]]
        solu_case_1 = [0, 1, 2, 0, 1, 2, 3, 0]

        self.assertEqual(flatten_list(
            test_case_1), solu_case_1)

    def test_will_it_float_string(self):
        test_case_1 = 'string'

        self.assertEqual(will_it_float(
            test_case_1), False)

    def test_will_it_float_int(self):
        test_case_1 = '12'

        self.assertEqual(will_it_float(
            test_case_1), True)

    def test_will_it_float_float(self):
        test_case_1 = '12.2'

        self.assertEqual(will_it_float(
            test_case_1), True)

    def test_count_truthy(self):
        test_case_1 = [True, False, False]
        self.assertEqual(count_truthy(
            test_case_1), 1)

    def test_read_csv_to_arrays_header(self):
        test_case_1 = 'tests/mock_data/mock_1.csv'
        test_solu_1 = [['7', '4000'], ['8', '5000']]
        self.assertEqual(read_csv_to_arrays(test_case_1), test_solu_1)

    def test_read_csv_to_arrays_no_header(self):
        test_case_1 = 'tests/mock_data/mock_1.csv'
        test_solu_1 = [['8', '5000']]
        self.assertEqual(read_csv_to_arrays(test_case_1, True), test_solu_1)


if __name__ == '__main__':
    unittest.main()
