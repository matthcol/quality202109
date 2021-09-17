# -*- coding: utf-8 -*-
from math import sqrt

def aire_triangle(a,b,c):
    """aire d'un triangle de cotés a,b et c avec  la formule de Héron"""
    p = (a+b+c) / 2
    return sqrt(p*(p-a)*(p-b)*(p-c))

def aire_triangle_opt(a,b,c):
    """aire d'un triangle de cotés a,b et c avec  la formule de Héron
    optimisée par William Kahan pour les triangles en épingle"""
    a,b,c = sorted((a,b,c), reverse=True)
    return sqrt(
        (a + (b + c)) 
        * (c - (a - b)) 
        * (c + (a - b)) 
        * (a + (b - c))) / 4
