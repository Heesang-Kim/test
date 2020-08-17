import unittest
import truefalse

class truefalsetest(unittest.TestCase):

    def test_true_1(self):
        self.assertEqual(truefalse.solution("1,2,3,4"), True)

    def test_true_2(self):
        self.assertEqual(truefalse.solution("a,2,3,4"), False)
