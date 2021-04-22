#importing the required libraries
import pandas as pd
import numpy as np
import os
import matplotlib as mpl
import seaborn as sb

#import the datasets
PrimaryEnergy = pd.read_csv("Primary Energy download.csv")
print(PrimaryEnergy.head())

RetailPrices = pd.read_csv("Retail Electricity Prices.csv")
print(RetailPrices.head())

#check for missing data
print(PrimaryEnergy.isnull().sum())
print(RetailPrices.isnull().sum())

#check all columns are accounted for
print(PrimaryEnergy.shape)
print(RetailPrices.shape)

#merging the two data sets
EP = PrimaryEnergy.merge(RetailPrices, on = 'YYYYMM', suffixes=('_Energy','_Prices'))
print(EP.columns)

#creating a pivot of the data
pivot_Energy = EP.pivot_table(values=["Value_Energy"], index=["YYYYMM"], columns=["Description_Energy"], aggfunc='sum')
print(pivot_Energy)

pivot_Prices = EP.pivot_table(values=["Value_Prices"], index=["YYYYMM"], columns=["Description_Prices"], aggfunc='sum')
print(pivot_Prices)