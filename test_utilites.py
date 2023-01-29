import unittest
import utilities

class TestUtilities(unittest.TestCase):
    def test_try_parse_int(self):
        self.assertIs(utilities.try_parse_int("3"), 3)
        self.assertIs(utilities.try_parse_int(13), 13)
        self.assertIs(utilities.try_parse_int("Actual String"), None)

if __name__ == '__main__':
    unittest.main()
