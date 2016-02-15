'''
Created on Feb 15, 2016

@author: ryan
'''
import unittest
import stockProblem

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStock(self):
        self.assertEqual([16, 1, 15], stockProblem.stockProblem([5, 7, 1, 9, 2, 16, 3]))
        self.assertEqual([9, 2, 7], stockProblem.stockProblem([5, 2, 9, 6, 8]))
        self.assertEqual([18, 1, 17], stockProblem.stockProblem([10, 4, 20, 1, 18]))
        self.assertEqual([20, 12, 8], stockProblem.stockProblem([12, 20, 1, 6]))
        self.assertEqual([None, None, 0], stockProblem.stockProblem([20, 13, 10, 5, 1]))
        self.assertEqual([None, None, 0], stockProblem.stockProblem([1, 1, 1, 1]))
        self.assertEqual([40, 1, 39], stockProblem.stockProblem([1, 10, 15, 40]))
        self.assertEqual([None, None, 0], stockProblem.stockProblem([]))


if __name__ == "__main__":
    unittest.main()