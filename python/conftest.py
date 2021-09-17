# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:13:01 2021

@author: Matthias
"""
import pytest
import logging

logger = logging.getLogger("pytest")


@pytest.fixture
def cotes_resource():
    # init resource : setup
    logger.info("init resource")
    print("init resource")
    yield (3.0,4.0,5.0)
    # clean resource : tearDown
    print("cleanup resource")    
    logger.info("cleanup resource")