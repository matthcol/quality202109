# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:07:10 2021

@author: Matthias
"""
import pytest
from surface import aire_triangle

@pytest.fixture
def aire_expected():
    return 6

@pytest.mark.aire_triangle
def test_aire_triangle(cotes_resource, aire_expected):
    a,b,c = cotes_resource
    res = aire_triangle(a,b,c)
    assert res == aire_expected
    
@pytest.fixture
def cotes():
    return [3,4,5]

@pytest.fixture(autouse=True)
def cotes_with_result(cotes):
    cotes.append(6)

@pytest.mark.aire_triangle    
def test_aire_triangle2(cotes):
    a,b,c, aire_expected = cotes
    res = aire_triangle(a,b,c)
    assert res == aire_expected

# @pytest.mark.xfail
@pytest.mark.aire_triangle    
def test_aire_triangle_negatif():
    a,b,c = -10.0, 1.0, 1.0
    with pytest.raises(ValueError) as exInfo:
        aire_triangle(a,b,c)
    assert str(exInfo.value) == "coté d'un triangle négatif ou nul"
    # assert str(exInfo.value) == "math domain error"

@pytest.mark.skip
def test_aire_carre():
    assert True    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    