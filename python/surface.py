# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:04:23 2021

@author: Matthias
"""
from math import sqrt

def aire_triangle(a,b,c):
    """aire d'un triangle de cotés a,b et c avec  la formule de Héron"""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("coté d'un triangle négatif ou nul")
    p = (a+b+c) / 2
    return sqrt(p*(p-a)*(p-b)*(p-c))
