# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:47:06 2021

@author: Matthias
"""

import unittest
import numpy as np

class TestNumpy(unittest.TestCase):
    
    def test_min_nan(self):
        # facts (given)
        data = np.array([3.0, np.nan, 4.0])
        # act (when)
        res = np.min(data)
        # verify (then)
        self.assertTrue(np.isnan(res))
        
    def test_nanmin_nan(self):
        # facts (given)
        data = np.array([3.0, np.nan, 4.0])
        # act (when)
        res = np.nanmin(data)
        # verify (then)
        self.assertEqual(res, 3.0)
        
if __name__ == '__main__':
    unittest.main()
        