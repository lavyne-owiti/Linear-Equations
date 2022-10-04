import unittest
import new

class TestlinerEquations(unittest.TestCase):
    def testLinearEquation(self):
        self.assertEqual(new.solve("7x-2=21"),3)
        
    def testlinear2(self):
        self.assertEqual(new.solve("2(4x + 3) + 6 = 24 -4x"),0)



        
        
if __name__ == '__main__':
    unittest.main()
