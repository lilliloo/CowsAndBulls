# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:46:10 2020

@author: lilliloo
"""

import random

#------Functions----------    
def make_digit(l):
    digit = []
    while len(digit) < 4:
        r = random.randint(0,9)
        if r not in digit:            
            digit.append(r)
    return digit

def count_cows(correct,answer):
        cow_num = 0
        cow_order = []
        for l in range(len(correct)):
            #cows
            #correct number and correct place
            if correct[l] == answer[l]:
                cow_num +=1
                cow_order.append(l)
        cow_info = cow_num , cow_order
        return cow_info
    
def count_bulls(correct,answer,cow_place):
        bull_num = 0
        for b in range(len(correct)):
            if b not in cow_place:
                judge = answer[b] in correct
                if judge == True:
                    bull_num +=1                
        return bull_num
    
def get_cows_bulls(correct , answer):
    # 1. Count cows
    cow_count , cow_place = count_cows(correct,answer)
    # 2. Count bulls
    bull_count = count_bulls(correct, answer, cow_place)
    # 3. Joint cows and bulls
    return cow_count , bull_count
#---------------------------
