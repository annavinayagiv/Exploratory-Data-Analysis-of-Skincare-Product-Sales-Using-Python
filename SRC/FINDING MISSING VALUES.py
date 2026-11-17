# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:29:53 2026

@author: hp
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Desktop\MINI PROJECT\sales_data.csv")

print(df.isnull().sum())