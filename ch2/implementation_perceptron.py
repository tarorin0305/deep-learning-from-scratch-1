import numpy as np
import matplotlib.pyplot as plt
import unittest

# and gate function
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # weight1, weight2, threshold
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

# unit test pf AND function
class TestANDFunction(unittest.TestCase):
    def test_AND(self):
        self.assertEqual(AND(0, 0), 0)
        self.assertEqual(AND(0, 1), 0)
        self.assertEqual(AND(1, 0), 0)
        self.assertEqual(AND(1, 1), 1)

# and gate function with bias and weight
def AND_bias(x1, x2):
    x = np.array([x1, x2]) # input
    w = np.array([0.5, 0.5]) # weight
    b = -0.7 # bias
    tmp = np.sum(w*x) + b # sum of input*weight + bias
    if tmp <= 0:
        return 0
    else:
        return 1

# unit test of AND function with bias
class TestANDFunctionBias(unittest.TestCase):
    def test_AND_bias(self):
        self.assertEqual(AND_bias(0, 0), 0)
        self.assertEqual(AND_bias(0, 1), 0)
        self.assertEqual(AND_bias(1, 0), 0)
        self.assertEqual(AND_bias(1, 1), 1)

# nand gate function
def NAND(x1, x2):
    x = np.array([x1, x2]) # input
    w = np.array([-0.5, -0.5]) # weight
    b = 0.7 # bias
    tmp = np.sum(w*x) + b # sum of input*weight + bias
    if tmp <= 0:
        return 0
    else:
        return 1

# unit test of NAND function
class TestNANDFunction(unittest.TestCase):
    def test_NAND(self):
        self.assertEqual(NAND(0, 0), 1)
        self.assertEqual(NAND(0, 1), 1)
        self.assertEqual(NAND(1, 0), 1)
        self.assertEqual(NAND(1, 1), 0)

# or gate function
def OR(x1, x2):
    x = np.array([x1, x2]) # input
    w = np.array([0.5, 0.5]) # weight
    b = -0.2 # bias
    tmp = np.sum(w*x) + b # sum of input*weight + bias
    if tmp <= 0:
        return 0
    else:
        return 1

# unit test of OR function
class TestORFunction(unittest.TestCase):
    def test_OR(self):
        self.assertEqual(OR(0, 0), 0)
        self.assertEqual(OR(0, 1), 1)
        self.assertEqual(OR(1, 0), 1)
        self.assertEqual(OR(1, 1), 1)

# execute unit test
if __name__ == '__main__':
    unittest.main()
