"""The rule checks itself."""

import unittest

from fix_needs_check import check


class FixNeedsCheck(unittest.TestCase):
    def test_a_fix_with_a_test_passes(self):
        self.assertIsNone(check("fix: discount taken twice", ["invoice.py", "test_fixes.py"]))

    def test_a_fix_without_a_test_is_refused(self):
        self.assertIsNotNone(check("fix: discount taken twice", ["invoice.py"]))

    def test_a_change_that_is_not_a_fix_needs_no_test(self):
        self.assertIsNone(check("Add a dark mode", ["styles.css"]))

    def test_it_reads_plain_words_too(self):
        self.assertIsNotNone(check("This fixes the login button", ["login.js"]))

    def test_javascript_tests_count(self):
        self.assertIsNone(check("fix: login button", ["login.js", "login.test.js"]))


if __name__ == "__main__":
    unittest.main()
