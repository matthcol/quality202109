# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:59:16 2021

@author: Matthias
"""

import unittest
from .functions import aire_triangle

class TestAireTriangle(unittest.TestCase):

    def test_aire_triangle_int(self):
        self.assertEqual(aire_triangle(3,4,5), 6)
        
    def test_aire_triangle_range(self):
        for e in range(1,6):
            exposant = 10**e
            with self.subTest(e=e):
                self.assertEqual(aire_triangle(3*exposant,4*exposant,5*exposant), 6*exposant*exposant)
        
    @unittest.expectedFailure
    def test_aire_triangle_overflow(self):
        self.assertEqual(aire_triangle(3E307,4E307,5E307), 6E307)
        
    def test_aire_triangle_round(self):
        self.assertEqual(aire_triangle(0.3,0.4,0.5), 0.6)

    def test_aire_triangle_epingle(self):
        self.assertEqual(aire_triangle(3E100,4E100,1), 6E307)



if __name__ == '__main__':
    unittest.main()