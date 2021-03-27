from ..functions.utils import find_middle
from ..functions.utils import realign_data

import unittest
import numpy as np
import pandas as pd

class TestMethods(unittest.TestCase):

    def test_find_middle_odd(self):
        test_array = np.arange(9)
        mid = 4
        output = find_middle(test_array)
        assert output == mid

    def test_find_middle_even(self):
        test_array = np.arange(12)
        mid = 6
        output = find_middle(test_array)
        assert output == mid

    def test_realign_max(self):
        d1 = np.arange(9)
        d2 = np.arange(6)
        d1 = d1 * d1[::-1]
        d2 = d2 * d2[::-1]
        true_shift = np.array([0, 2])
        test_df = pd.DataFrame([d1, d2]).fillna(0)
        test_df = test_df.T
        d, shift = realign_data(test_df)
        np.testing.assert_array_equal(true_shift, shift)

if __name__ == '__main__':
    unittest.main()
