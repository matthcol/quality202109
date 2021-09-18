# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:30:58 2021

@author: Matthias
"""
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# pip install pytest-selenium

# def test_example(selenium):
#     selenium.get('http://localhost:5000')
    
    
#Fixture for Firefox
@pytest.fixture
def driver():
    d = webdriver.Firefox()
    yield d
    d.close()
    
def test_accueil(driver):
    driver.get('http://localhost:5000/')
    elements = WebDriverWait(driver, 10).until(
        lambda d:d.find_elements_by_css_selector("#view li"))
    assert len(elements) == 4
    assert elements[0].text == "Kate (2021)"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    