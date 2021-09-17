# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:43:22 2021

@author: Matthias
"""

import pytest
import sys

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

# fixture déplace dans conftest.py
# @pytest.fixture
# def cotes_resource():
#     # init resource : setup
#     logger.info("init resource")
#     print("init resource")
#     yield (3.0,4.0,5.0)
#     # clean resource : tearDown
#     print("cleanup resource")    
#     logger.info("cleanup resource")
    
def test_hypothenuse4(cotes_resource):
    a, b, expected_res = cotes_resource
    res = hypothenuse(a,b)
    assert res == expected_res
    
    
@pytest.mark.parametrize("a,b,expected_res",
        ((3.0, 4.0, 5.0),
         (6.0, 8.0, 10.0)))
def test_hypothenuse5(a,b, expected_res):
    res = hypothenuse(a,b)
    assert res == expected_res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    