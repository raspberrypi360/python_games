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
        s, num = join_circles.getProduct([1,2,3,4,5], 1)
        self.assertEqual(720, s)
        s, num = join_circles.getProduct([1,2,3,4,5], 2)
        self.assertEqual(5850, s)
        s, num = join_circles.getProduct([1,2,3,4,5], 3)
        self.assertEqual(25200, s)
        k=6
        self.assertEqual(150, join_circles.numCombos([i+1 for i in range(k)], 2))
        self.assertEqual(900, join_circles.numCombos([i+1 for i in range(k)], 3))
        self.assertEqual(2700, join_circles.numCombos([i+1 for i in range(k)], 4))
        s, num = join_circles.getProduct([i+1 for i in range(k)], 2)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 2), s)
        s, num = join_circles.getProduct([i+1 for i in range(k)], 3)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 3), s)
        s, num = join_circles.getProduct([i+1 for i in range(k)], 4)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 4), s)
        k=7
        s, num = join_circles.getProduct([i+1 for i in range(k)], 2)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 2), s)
        s, num = join_circles.getProduct([i+1 for i in range(k)], 3)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 3), s)
        s, num = join_circles.getProduct([i+1 for i in range(k)], 4)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 4), s)
        s, num = join_circles.getProduct([i+1 for i in range(k)], 5)
        self.assertEqual(join_circles.getSquare([i+1 for i in range(k)], 5), s)


if __name__ == "__main__":
    unittest.main()