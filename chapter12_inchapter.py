# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:00:23 2017

@author: Ankurt.04
"""
"""
chapter 12 - exercises within the chapter 12
"""
#Ex 12.1

"""
sumall takes any number of inputs and gives out their sum
"""

def sumall(*nos):
    a = len(nos)
    i = 0
    sumall = 0
    while i < a:
        sumall += nos[i]
        i += 1
    return sumall


print(sumall(2, 3, 7, 12, 6, -27))


