# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:45:38 2021

@author: Matthias
"""
from math import sqrt, hypot
#from math import *


def hypothenuse(a,b):
    #return sqrt(a**2 + b**2) 
    if a <= 0 or b<= 0:
        raise ValueError("coté d'un triangle négatif ou nul")
    return hypot(a,  b)
    