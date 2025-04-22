# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 22:52:17 2025

@author: anush
"""

import pandas as pd

#read csv file
data=pd.read_csv("Superstore.csv", encoding='ISO-8859-1')

#drop rows with null values and dupicates
data=data.dropna()
data=data.drop_duplicates()

#convert numeric values to date format
data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True)
data['Ship Date'] = pd.to_datetime(data['Ship Date'], dayfirst=True)

#rename column names to small case
data.columns= data.columns.str.lower()

#Create new columns
data['profit margin']=data['profit']/data['sales']
data['order year']=data['order date'].dt.year
data['order month']=data['order date'].dt.month

#cleaned file output
data.to_csv('Sample_Superstore.csv', index=False)