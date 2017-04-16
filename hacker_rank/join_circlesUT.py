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
        self.assertEqual(720, join_circles.getProduct(1, [1,2,3,4,5]))
        self.assertEqual(5850, join_circles.getProduct(2, [1,2,3,4,5]))
        self.assertEqual(26390, join_circles.getProduct(3, [1,2,3,4,5]))

if __name__ == "__main__":
    unittest.main()