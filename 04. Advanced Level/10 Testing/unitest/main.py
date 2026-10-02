import unittest
from test import MathOperations   # test.py 

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.calc = MathOperations()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(self.calc.sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(self.calc.mul(10, 5), 50)

    def test_div(self):
        self.assertEqual(self.calc.div(10, 5), 2)

    def test_mod(self):
        self.assertEqual(self.calc.mod(10, 3), 1)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(25), 5)

    def test_log(self):
        import math
        self.assertAlmostEqual(self.calc.log(math.e), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
