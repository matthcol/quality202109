# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:50:41 2021

@author: Matthias
"""

import unittest
import numpy as np

from hypothenuse import hypothenuse

class TestHypothenuse(unittest.TestCase):
    
    def test_hypothenuse_courant(self):
        self.assertEqual(
            hypothenuse(3.0,4.0),
            5.0)
        
    def test_hypothenuse_imprecision(self):
        self.assertAlmostEqual(
            hypothenuse(0.1, 0.2),
            0.2236,
            places=4)
        
    def test_hypothenuse_imprecision2(self):
        self.assertAlmostEqual(
            hypothenuse(0.001, 0.002),
            0.002236,
            places=6)
        
    def test_hypothenuse_imprecision3(self):
        self.assertTrue(np.isclose(
            hypothenuse(0.001, 0.002),
            0.002236,
            rtol=1e-4))
    
    def test_hypothenuse_big(self):
        self.assertEqual(
            hypothenuse(3E300,4E300),
            5E300)
        
    def test_hypothenuse_little(self):
        self.assertEqual(
            hypothenuse(3E-300,4E-300),
            5E-300)
        
    def test_hypothenuse_nan(self):
        self.assertTrue(np.isnan(
            hypothenuse(np.nan,4.0)))
        
    def test_hypothenuse_range(self):
        for exposant in range(5):
            base10 = 10**exposant
            with self.subTest(exposant=exposant):
                self.assertTrue(np.isclose(
                    hypothenuse(3*base10, 4*base10),
                    5*base10,
                    rtol=1e-8))
                
    def test_hypothenuse_multiple_values(self):
        facts = (
            (3.0, 4.0, 5.0),
            (6.0, 8.0, 10.0))
        for a, b, r in facts:
            with self.subTest(a=a, b=b):
                self.assertEquals(
                    hypothenuse(a, b),
                    r+1)
                     
if __name__ == '__main__':
    unittest.main() 