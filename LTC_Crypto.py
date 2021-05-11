# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:42:27 2021

@author: macke
"""
#%%
## Gather all of my inputs




import pandas as pd
from ViewCoinBaseAccount import Get_Price, Check_Account, Get_Da_price_Tho
import os
    
#%% THIS SEGMENT RUNS A WHILE LOOP FOR X AMOUNT OF TIME

counter_df = pd.read_csv('CryptoLocalData\LTC_File.csv')
index = counter_df.index

# get the count of rows currently in my file
count = len(index)

# Set x to the current number of rows in my file
x = count

print(' \n File count = ',count)
 
while x < 100000:
    Get_Da_price_Tho()
    if x/10 == 0:
        os.system('python try_file.py')

