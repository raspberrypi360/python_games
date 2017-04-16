import unittest
import join_circles

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStock(self):
        self.assertEqual(18, join_circles.numCombos([1,2,3,4], 3))
        self.assertEqual(180, join_circles.numCombos([1,2,3,4,5], 3))

if __name__ == "__main__":
    unittest.main()