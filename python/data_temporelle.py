# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:05:21 2021

@author: Matthias
"""

import pandas as pd
from datetime import timedelta

df = pd.read_csv('data.csv', parse_dates=['debut'],
                 encoding='UTF-8')
print(df)

print(df.debut.dt.month)

print(df.label.str.upper())