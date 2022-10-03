import unittest
import linear

class TestlinerEquations(unittest.TestCase):
    def testLinearEquation(self):
        self.assertEqual(linear.linearEquation("2(4x + 3) + 6 = 24 -4x"),3)

        
        
if __name__ == '__main__':
    unittest.main()
