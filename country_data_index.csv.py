#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:23:30 2024

@author: florence
"""
import pandas as pd

df = pd.read_csv("data_02/country_data_index.csv")
#print(df)

df = pd.read_csv("data_02/country_data_index.csv",index_col=0)
#print(df)

df = pd.read__csv("data_02/insurance_data.csv")
print(df)

