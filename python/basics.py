# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:34:04 2021

@author: Matthias
"""
import numpy as np

def f(x: int) -> int:
    return x + 1

print(f(1))
print(f(1.1))
print(f(np.random.normal(10,2,100)))

print(f("Pau"))