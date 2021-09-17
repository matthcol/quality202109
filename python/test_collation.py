# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:54:11 2021

@author: Matthias
"""

import unittest
import pandas as pd
import locale
from functools import cmp_to_key


class TestCollation(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # reglage executé 1 seule fois
        # avant tous les tests de la classe
        locale.setlocale(locale.LC_ALL, 'fr_FR')
    
    def test_find_case_insensitive(self):
        villes = [ "Toulouse", "pau", "RENNES" ]
        serieVilles = pd.Series(villes)
        ville = "Rennes"
        self.assertTrue(
            ville.casefold() == villes[2].casefold())
        self.assertTrue(
            serieVilles.str.contains(ville, case=False).any())
        
    def test_sorted_collation_fr(self):
        # fact
        mots = ["été", "étage", "étuve", "expérience" ]
        # act
        sorted_mots = sorted(mots,
                         key=cmp_to_key(locale.strcoll))
        # verify
        expected_sorted_mots = ["étage", "été", "étuve", "expérience" ]
        self.assertEqual(sorted_mots, expected_sorted_mots)
            

if __name__ == '__main__':
    unittest.main()