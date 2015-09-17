# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:57:31 2015

@author: Kruthika
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#Box plot for amount requested
plt.figure()
loansData.boxplot(column='Amount.Requested')
plt.show()

#Histogram for amount Requested
loansData.hist(column='Amount.Requested')
plt.show()

#QQ plot for amount Requested
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()

#Box plot for amount funded by investors
plt.figure()
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

#Histogram for amount funded by inverstors
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

#QQ plot for amount funded by investors
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()


