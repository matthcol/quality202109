# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:10:49 2021

@author: Matthias
"""
from math import hypot, sqrt
import surface

class GeometryTriangle:
    
    def hypothenuse(self, a,b):
        if a <= 0 or b<= 0:
            raise ValueError("coté d'un triangle négatif ou nul")
        return hypot(a,  b)
    
    def aire_triangle(self, a,b,c):
        """aire d'un triangle de cotés a,b et c avec  la formule de Héron"""
        # if a <= 0 or b <= 0 or c <= 0:
        #     raise ValueError("coté d'un triangle négatif ou nul")
        # p = (a+b+c) / 2
        # return sqrt(p*(p-a)*(p-b)*(p-c))
        pass
    
class GeometryQuadrilatere:
    
    def __init__(self, geometryTriangle: GeometryTriangle):
        self.geometryTriangle = geometryTriangle
        
    def aire_quadrilatere(self, a,b,c,d, diag):
        s1 = self.geometryTriangle.aire_triangle(a, b, diag)
        s2 = self.geometryTriangle.aire_triangle(c, d, diag)
        return s1 + s2
        # return 12
        
def f_aire_quadrilatere(a,b,c,d, diag):
        s1 = surface.aire_triangle(a, b, diag)
        s2 = surface.aire_triangle(c, d, diag)
        return s1 + s2
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    