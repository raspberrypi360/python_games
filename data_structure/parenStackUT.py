import unittest
import parenStack

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStock(self):
        self.assertEqual(True, parenStack.match("()"))
        self.assertEqual(False, parenStack.match("("))
        self.assertEqual(False, parenStack.match(")()"))
        self.assertEqual(True, parenStack.match("()()"))
        self.assertEqual(True, parenStack.match("(())"))
        self.assertEqual(False, parenStack.match("(((()())())"))
        self.assertEqual(False, parenStack.match("())"))

if __name__ == "__main__":
    unittest.main()