import unittest
max_integer = __import__('6-max_integer').max_integer

class test(unittest.TestCase):
    def test_list(self):
        l = [1, 5, 2]
        self.assertEqual(max_integer(l), 5)
    def test_empty(self):
        l = []
        self.assertEqual(max_integer(l), None)
    def test_negative(self):
        l = [-1, -4, -10]
        self.assertEqual(max_integer(l), -1)
    def test_no_list(self):
        self.assertEqual(max_integer(), None)
    def test_one(self):
        l = [1]
        self.assertEqual(max_integer(l), 1)
    def test_same(self):
        l = [1, 1, 1]
        self.assertEqual(max_integer(l), 1)


if __name__ == '__main__':
    unittest.main()
