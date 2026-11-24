"""One test for every bug we fixed. Each one fails on the old code and passes on the new code.

This file only grows. When a bug is fixed, its test goes here in the same change, named for the
bug, so the same mistake can never come back quietly.
"""

import unittest

from invoice import total_cents


class EveryFixBecomesACheck(unittest.TestCase):
    def test_fix_1_discount_is_taken_once(self):
        # The bug: 10% off a $100 order came to $81, because the discount was taken twice.
        self.assertEqual(total_cents([(5000, 1), (5000, 1)], discount_percent=10), 9000)

    def test_fix_2_discount_over_100_is_refused(self):
        # The bug: a 150% discount made the customer's total negative.
        with self.assertRaises(ValueError):
            total_cents([(1000, 1)], discount_percent=150)

    def test_fix_3_negative_quantity_is_refused(self):
        # The bug: a quantity of -1 quietly took money off the bill.
        with self.assertRaises(ValueError):
            total_cents([(1000, 2), (1000, -1)])


if __name__ == "__main__":
    unittest.main()
