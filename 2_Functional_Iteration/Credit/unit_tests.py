"""


"""

import unittest
import credit_doctest2 as credit


class TestValidate(unittest.TestCase):

    def test_check_digit(self):
        test_account = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
        sliced_off = test_account[:-1]
        self.assertEqual(credit.check_digit(test_account), (sliced_off, 5))

    def test_reversing(self):
        test_account = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5]
        rverse = test_account[::-1]
        self.assertEqual(credit.reversing(test_account), (rverse, [5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]))

    #

    # def test_reversing(self):
    #     test_reverse =