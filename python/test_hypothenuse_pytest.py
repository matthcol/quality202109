# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:43:22 2021

@author: Matthias
"""

import pytest
from hypothenuse import hypothenuse

def test_hypothenuse():
    res = hypothenuse(3.0, 4.0)
    assert res == 5.0
    

@pytest.fixture
def cotes():
    return (3.0, 4.0)    

@pytest.fixture
def expected_hypo():
    return 5.0    

def test_hypothenuse2(cotes, expected_hypo):
    res = hypothenuse(*cotes)
    assert res == expected_hypo
    

@pytest.fixture
def facts_hypot(cotes):
    return (*cotes, 5)
    
def test_hypothenuse3(facts_hypot):
    a, b, expected_res = facts_hypot
    res = hypothenuse(a,b)
    assert res == expected_res