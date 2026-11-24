"""What the invoice should do on a normal day."""

import unittest

from invoice import total_cents


class NormalDay(unittest.TestCase):
    def test_adds_up_lines(self):
        self.assertEqual(total_cents([(1000, 2), (250, 4)]), 3000)

    def test_takes_a_discount(self):
        self.assertEqual(total_cents([(1000, 1)], discount_percent=10), 900)

    def test_empty_order_is_zero(self):
        self.assertEqual(total_cents([]), 0)


if __name__ == "__main__":
    unittest.main()
