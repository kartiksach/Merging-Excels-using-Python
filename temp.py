#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:48:50 2018

@author: kartik
"""

import pandas as pd
import os

#Setting directory
path = os.getcwd()
files = os.listdir(path)

#Storing names of xls files in a list
files_xls = [f for f in files if f[-3:] == 'xls']

#creating an empty dataFrame
df = pd.DataFrame

#ls is the list to store the data of each xls file
ls = []

for f in files_xls:
    data = pd.read_excel(f, 'Sheet1')
    ls.append(data)

#Concatenate data from ls into data frame result
result = pd.concat(ls)