#importing the required libraries
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

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
EP = PrimaryEnergy.merge(RetailPrices, on = 'YYYYMM', how='left', suffixes=('_Energy','_Prices'))

EP = EP[['YYYYMM', 'Value_Energy','Description_Energy', 'Value_Prices','Description_Prices']]

#creating a pivot of the data
pivot_Energy = EP.pivot_table(values=["Value_Energy"], index=["YYYYMM"], columns=["Description_Energy"], aggfunc='sum')
print(pivot_Energy)

pivot_Prices = EP.pivot_table(values=["Value_Prices"], index=["YYYYMM"], columns=["Description_Prices"], aggfunc='sum')
print(pivot_Prices)

#subsetting the data
EP_TotalPrices= EP[(EP['Description_Energy'] == 'Total Primary Energy Production')
                   &(EP['Description_Prices'] == 'Average Retail Price of Electricity, Total')
                    &(EP["YYYYMM"]%13!=0) ]
print(EP_TotalPrices)


EP_RewPrices= EP[(EP['Description_Energy'] == 'Total Renewable Energy Production')&(EP['Description_Prices'] == 'Average Retail Price of Electricity, Total')]
print(EP_RewPrices)

#plotting graphs
EP_TotalPrices.plot(x="YYYYMM", y="Value_Energy", kind="scatter")
plt.show()

EP_RewPrices.plot(x="YYYYMM", y="Value_Prices", kind="scatter")
plt.show()
