# -*- coding: utf-8 -*-

from random import random
import pandas as pd


max_Pool = 1000
min_Pool = 30
max_num_size=1000
num_of_pools=1000


class sample:
    def __init__(self,Pool,Sub_pool):
        self.Pool=Pool
        self.Sub_pool=Sub_pool
        self.Total=sum(Pool)
        self.Sub_Total=sum(Sub_pool)
        self.Pool_len=len(Pool)
        self.Sub_len=len(Sub_pool)

def make_sample(size):
    Pool=[]
    Sub_pool=[]
    perc_pool=random()
    for i in range(size):
        new_samp=int(round(random()*max_num_size,0))
        Pool.append(new_samp)
        if random()<perc_pool:
            Sub_pool.append(new_samp)
    output=sample(Pool,Sub_pool)
    if len(Sub_pool)>0 and len(Sub_pool)<len(Pool):
        return output
    else:
        return(make_sample(size))
        

    
output=pd.DataFrame(columns=["Pool","Sub","Pool_Tot","Sub_Tot","Pool_Len","Sub_Len"])

for i in range(num_of_pools):
    sample_size=round(random()*max_Pool)
    while sample_size < min_Pool:
        sample_size = round(random()*max_Pool)
        
    new_samp=make_sample(sample_size)
    
    output=output.append({'Pool':new_samp.Pool,
                   'Sub': new_samp.Sub_pool,
                   'Pool_Tot':new_samp.Total,
                   'Sub_Tot': new_samp.Sub_Total,
                   'Pool_Len':new_samp.Pool_len,
                   'Sub_Len':new_samp.Sub_len
                   },ignore_index=True)


    
output.to_excel('Test.xlsx',index=False)
