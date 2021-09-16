# -*- coding: utf-8 -*-
from math import sqrt

def aire_triangle(a,b,c):
    p = (a+b+c) / 2
    return sqrt(p*(p-a)*(p-b)*(p-c))
