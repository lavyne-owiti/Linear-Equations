import unittest
import Linearmath

class TestlinerEquations(unittest.TestCase):
    def testLinearEquation(self):
        self.assertEqual(Linearmath.solve("7x-2=21"),3)
        
    def testlinearEquation2(self):
        self.assertEqual(Linearmath.solve("2(4x + 3) + 6 = 24 -4x"),1)



        
        
if __name__ == '__main__':
    unittest.main()
