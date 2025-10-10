python
# app/python/tests/test_app.py

import unittest

class TestApp(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1, 1)

    def test_another_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()