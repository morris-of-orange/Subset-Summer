# -*- coding: utf-8 -*-

import pandas as pd
from Actual import Find_Sub_Pool as fsb
#from Testing_Ground import Find_Sub_Pool as fsb2
import time

def str_to_array(string):
    string=string.replace('[','').replace(']','').replace(' ','')
    return [int(ele) for ele in string.split(',')]

Results=pd.read_excel('Test.xlsx')
Results['Result1']=''
Results['Time1']=1000000
Results['Is_Equal']=False


for i in Results.index:
#for i in range(10):
#original pool
#i = 1
    pool = str_to_array(Results.loc[i,'Pool'])
    #Sample was the original, we use it to check our work
    sample = str_to_array(Results.loc[i,'Sub'])
    sample.sort()
    sample.reverse()
    #what we are looking for
    subtotal = int(Results.loc[i,'Sub_Tot'])
    
    #Tic will calculate how long this takes
    try:
        tic=time.time()
        output=fsb(pool,subtotal)
        toc=time.time()
        output.sort()
        output.reverse()
    except:
        tic=0
        toc=0
        output = 'FAILURE'
    
    
    
    Results.loc[i,'Result1']=str(output)
    Results.loc[i,'Time1']=toc-tic
    Results.loc[i,'Is_Equal']=output==sample
    
    print(str(i))
Results.to_excel('Test_Results.xlsx')

            
