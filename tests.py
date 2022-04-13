import unittest

from round_percentages import round_percentages


class TestRoundedPercentages(unittest.TestCase):
    def test_results_sum_to_100_and_in_correct_order(self):
        input_ = [13.626332, 47.989636, 9.596008, 28.788024]
        self.assertEqual(sum(input_), 100)

        result = round_percentages(input_)

        self.assertEqual(result,  [14, 48, 9, 29])
        self.assertEqual(sum(result), 100)

    def test_already_integers_return_unchanged(self):
        input_ = [5, 90, 5]
        self.assertEqual(sum(input_), 100)

        result = round_percentages(input_)

        self.assertEqual(result, input_)
        self.assertEqual(sum(result), 100)


if __name__ == '__main__':
    unittest.main()
