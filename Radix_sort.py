# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:35:56 2017

@author: warremn
"""

import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

max_num = 1000000
arr_size = 20000
base = 10


def count_sort(arr, digit):
    # Be ware of alising issue in list
    # count = pos = [0]*base
    
    # initial
    count = [0]*base
    new_arr = [0]*arr_size
    pos = [0]*base
                   
    # count each digit element
    for i in arr:
        count[(i//digit) % 10] += 1
    
    logging.debug("==== %d base ====", digit)  
    logging.debug("base counter: {} ".format(' '.join(map(str,count))))
    
    # compute starting position of each digit
    pos[base-1] = arr_size - count[base-1]
    for i in range(base-2,-1,-1):
        pos[i] = pos[i+1] - count[i]    
        
    logging.debug("position: {}".format(' '.join(map(str,pos))))
    
    
    # sort digit based on position list
    for i in arr:
        element = (i//digit) % 10
        new_arr[pos[element]] = i
        pos[element] += 1

    logging.debug("sort: {}".format(' '.join(map(str,new_arr))))
    
    return new_arr
    
    
    
def radix_sort(arr):
    
    digit = 1
    while digit < max_num:
        arr = count_sort(arr, digit)   
        digit *= base
        
    return arr


if __name__ == '__main__':
    

    arr = random.sample(range(max_num), arr_size)
    print("original array:", arr)
    arr = radix_sort(arr)
    print("sorted array:", arr)
    
    
    
    
    
    