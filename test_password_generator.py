import unittest
import password_generator

class TestPasswordGenerator(unittest.TestCase):
    def test_password_generator_empty(self):
        pw = password_generator.password_generator()
        self.assertIsNone(pw)

    def test_password_generator_length_no_flags(self):
        pw = password_generator.password_generator(10)
        self.assertIsNone(pw)

    def test_password_generator_lengths(self):
        pw = password_generator.password_generator(10, True)
        self.assertEqual(len(pw), 10)
        pw = password_generator.password_generator(200, True, True, True)
        self.assertEqual(len(pw), 200)

if __name__ == '__main__':
    unittest.main()
