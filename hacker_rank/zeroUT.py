import unittest
import zero_game

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStock(self):
        self.assertEqual(False, zero_game.outcomes([0,0,0,0]))
        self.assertEqual(True, zero_game.outcomes([0,0,0,1]))
        self.assertEqual(False, zero_game.outcomes([0,0,1,0]))
        self.assertEqual(False, zero_game.outcomes([0,0,1,1]))
        self.assertEqual(False, zero_game.outcomes([0,1,0,0]))
        self.assertEqual(True, zero_game.outcomes([0,1,0,1]))
        self.assertEqual(False, zero_game.outcomes([0,1,1,0]))
        self.assertEqual(False, zero_game.outcomes([0,1,1,1]))
        self.assertEqual(True, zero_game.outcomes([1,0,0,0]))
        self.assertEqual(False, zero_game.outcomes([1,0,0,1]))
        self.assertEqual(True, zero_game.outcomes([1,0,1,0]))
        self.assertEqual(False, zero_game.outcomes([1,0,1,1]))
        self.assertEqual(False, zero_game.outcomes([1,1,0,0]))
        self.assertEqual(False, zero_game.outcomes([1,1,0,1]))
        self.assertEqual(False, zero_game.outcomes([1,1,1,0]))
        self.assertEqual(False, zero_game.outcomes([1,1,1,1]))

        self.assertEqual(True, zero_game.outcomes([0,0,0,0,0]))
        self.assertEqual(False, zero_game.outcomes([0,0,0,0,1]))
        self.assertEqual(True, zero_game.outcomes([0,0,0,1,0]))
        self.assertEqual(True, zero_game.outcomes([0,0,0,1,1]))
        self.assertEqual(True, zero_game.outcomes([0,0,1,0,0]))
        self.assertEqual(False, zero_game.outcomes([0,0,1,0,1]))
        self.assertEqual(False, zero_game.outcomes([0,0,1,1,0]))
        self.assertEqual(False, zero_game.outcomes([0,0,1,1,1]))
        self.assertEqual(True, zero_game.outcomes([0,1,0,0,0]))
        self.assertEqual(False, zero_game.outcomes([0,1,0,0,1]))
        self.assertEqual(True, zero_game.outcomes([0,1,0,1,0]))
        self.assertEqual(True, zero_game.outcomes([0,1,0,1,1]))
        self.assertEqual(False, zero_game.outcomes([0,1,1,0,0]))
        self.assertEqual(False, zero_game.outcomes([0,1,1,0,1]))
        self.assertEqual(False, zero_game.outcomes([0,1,1,1,0]))
        self.assertEqual(False, zero_game.outcomes([0,1,1,1,1]))
        self.assertEqual(False, zero_game.outcomes([1,0,0,0,0]))
        self.assertEqual(True, zero_game.outcomes([1,0,0,0,1]))
        self.assertEqual(False, zero_game.outcomes([1,0,0,1,0]))
        self.assertEqual(False, zero_game.outcomes([1,0,0,1,1]))
        self.assertEqual(False, zero_game.outcomes([1,0,1,0,0]))
        self.assertEqual(True, zero_game.outcomes([1,0,1,0,1]))
        self.assertEqual(False, zero_game.outcomes([1,0,1,1,0]))
        self.assertEqual(False, zero_game.outcomes([1,0,1,1,1]))
        self.assertEqual(True, zero_game.outcomes([1,1,0,0,0]))
        self.assertEqual(False, zero_game.outcomes([1,1,0,0,1]))
        self.assertEqual(True, zero_game.outcomes([1,1,0,1,0]))
        self.assertEqual(False, zero_game.outcomes([1,1,0,1,1]))
        self.assertEqual(False, zero_game.outcomes([1,1,1,0,0]))
        self.assertEqual(False, zero_game.outcomes([1,1,1,0,1]))
        self.assertEqual(False, zero_game.outcomes([1,1,1,1,0]))
        self.assertEqual(False, zero_game.outcomes([1,1,1,1,1]))

if __name__ == "__main__":
    unittest.main()