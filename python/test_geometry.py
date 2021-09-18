# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:23:36 2021

@author: Matthias
"""

from unittest.mock import MagicMock, patch
import pytest
from geometry import GeometryQuadrilatere, GeometryTriangle, \
    f_aire_quadrilatere

# https://docs.python-guide.org/writing/tests/
# https://aaronlelevier.github.io/python-unit-testing-with-magicmock/

@pytest.fixture
def cotes_quadri():
    return (3,4,3,4,5,12)

def test_aire_quadrilatere(cotes_quadri):
    # mock un objet GeometryTriangle
    geoTriangle = GeometryTriangle()
    geoTriangle.aire_triangle = MagicMock(return_value=6)
    # facts
    a, b, c, d, diag, expected_area = cotes_quadri
    geoQuadri = GeometryQuadrilatere(geoTriangle)
    # act
    res = geoQuadri.aire_quadrilatere(a,b,c,d,diag)
    # verify
    assert res == expected_area
    geoTriangle.aire_triangle.assert_called_with(3,4,5)
    
    
def mock_aire_triangle(a,b,c):
    return 6
    
@patch('surface.aire_triangle', mock_aire_triangle)
def test_f_aire_quadrilatere(cotes_quadri):
    # facts
    a, b, c, d, diag, expected_area = cotes_quadri
    # act
    res = f_aire_quadrilatere(a,b,c,d,diag)
    # verify
    assert res == expected_area
    # geoTriangle.aire_triangle.assert_called_with(3,4,5)   

mock_aire_triangle2 = MagicMock(return_value=6) 

@patch('surface.aire_triangle', mock_aire_triangle2)
def test_f_aire_quadrilatere2(cotes_quadri):
    # facts
    a, b, c, d, diag, expected_area = cotes_quadri
    # act
    res = f_aire_quadrilatere(a,b,c,d,diag)
    # verify
    assert res == expected_area
    mock_aire_triangle2.assert_called_with(3,4,5) 
    # mock_aire_triangle2.reset_mock()
    # mock_aire_triangle2.assert_called_with(3,4,5) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    