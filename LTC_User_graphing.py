# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:48:27 2021

@author: macke
"""
import os
import time
from LTC_graph import Graph_Last_Week, Graph_Last_Hour, Graph_Last_24_Hours, Graph_All
print('To Graph Last Hour press 0')
print('To Graph Last Day press 1')
print('To Graph Last Week press 2')
print('To Graph all Data press 3')
userinput = input('Please enter a number between 0-3:')

if userinput == 0:
    Graph_Last_Hour()
if userinput == 1:
    Graph_Last_24_Hours()
if  userinput == 2:
    Graph_Last_Week()
if userinput == 3:
    Graph_All()
    
time.sleep(5)

os.system('graph.png')

    