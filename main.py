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