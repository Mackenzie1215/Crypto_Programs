# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:49:31 2021

@author: macke
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import subprocess
import time
import os

os.system('python Get_Data.py')  
LTC_F = pd.read_csv('Crypto_Data_File\CryptoLocalData\LTC_File.csv')
#LTC_F = pd.read_csv('LTC_File_LowDetail.csv')
print(LTC_F.tail(5))
def Graph_All():
    
    plt.plot(LTC_F['Time'],LTC_F['Price'])
    lh = LTC_F
    first = lh.head(1)
    last = lh.tail(1)
    first_v = (first.iloc[0]['Price'])
    last_v = (last.iloc[0]['Price'])
    
    if (last_v > first_v):
        gain = ((float(last_v) - float(first_v)) / first_v)
        gain_conv = format(gain, '.3f')
        title = ('Gain of ', gain_conv , '% ', ' total.')
 
    if (first_v > last_v):
        loss = ((float(first_v) - float(last_v)) / first_v)
        loss_conv = format(loss, '.3f')
        title = ('Loss of ', loss_conv , '% ', ' total.')
    plt.plot(lh['Time'],lh['Price'])
    plt.title(title)
    plt.savefig('graph.png')
    

def Graph_Last_Hour():

    lh = LTC_F.tail(12)
    
    plt.plot(lh['Time'],lh['Price'])
    first = lh.head(1)
    last = lh.tail(1)
    first_v = (first.iloc[0]['Price'])
    last_v = (last.iloc[0]['Price'])
    
    if (last_v > first_v):
        gain = ((float(last_v) - float(first_v)) / first_v)
        gain_conv = format(gain, '.3f')
        title = ('Gain of ', gain_conv , '% ', ' in past hour.')
 
    if (first_v > last_v):
        loss = ((float(first_v) - float(last_v)) / first_v)
        loss_conv = format(loss, '.3f')
        title = ('Loss of ', loss_conv , '% ', ' in past hour.')
    plt.plot(lh['Time'],lh['Price'])
    plt.title(title)
    plt.savefig('graph.png')

def Graph_Last_24_Hours():
    
    lh = LTC_F.tail(800)
    
    first = lh.head(1)
    last = lh.tail(1)
    first_v = (first.iloc[0]['Price'])
    last_v = (last.iloc[0]['Price'])
    
    if (last_v > first_v):
        gain = ((float(last_v) - float(first_v)) / first_v)
        gain_conv = format(gain, '.3f')
        title = ('Gain of ', gain_conv , '% ', ' in past 24 hour.')
 
    if (first_v > last_v):
        loss = ((float(first_v) - float(last_v)) / first_v)
        loss_conv = format(loss, '.3f')
        title = ('Loss of ', loss_conv , '% ', ' in past 24 hour.')
    plt.plot(lh['Time'],lh['Price'])
    plt.title(title)
    plt.savefig('graph.png')

def Graph_Last_Week():

    lh = LTC_F.tail(2016)  
    
    first = lh.head(1)
    last = lh.tail(1)
    first_v = (first.iloc[0]['Price'])
    last_v = (last.iloc[0]['Price'])
    
    if (last_v > first_v):
        gain = ((float(last_v) - float(first_v)) / first_v)
        gain_conv = format(gain, '.3f')
        title = 'Gain of ', gain_conv , '% ',' in past week.'
 
    if (first_v > last_v):
        loss = ((float(first_v) - float(last_v)) / first_v)
        loss_conv = format(loss, '.3f')
        title = 'Loss of ', loss_conv , '% ', ' in past week'
        
    plt.plot(lh['Time'],lh['Price'])
    plt.title(title)
    plt.savefig('graph.png')
    
Graph_Last_Hour()