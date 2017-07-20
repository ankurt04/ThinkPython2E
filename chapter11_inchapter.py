# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:06:53 2017

@author: Ankurt.04
"""

"""
Chapter 11 - Exercise appearing within the chapter with theory
"""

#Ex 1

"""
function hisotgram using get eliminating if statement

Counts how many times a letters has appeared in a string
"""
def histogram(s):
    d = dict()
    for c in s:
        dict_val = d.get(c, 0)
        d[c] = dict_val + 1
    return d
    
test_str = 'oolalala'
re = histogram(test_str)
print (re)
