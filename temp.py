#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:48:50 2018

@author: kartik
"""

import pandas as pd
import os
import glob


path = os.getcwd()
files = os.listdir(path)


files_xls = [f for f in files if f[-3:] == 'xls']

df = pd.DataFrame

for f in files_xls:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)
    
