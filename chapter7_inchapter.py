# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:47:48 2017

@author: Ankurt.04
"""

#Chapter 7 
#square root 

def sq_root(a, estimate_root):
    print("Calculating square root of number: ", a)
    epsilon = 0.00000000000001
    while True:
        sq_root = (estimate_root + (a / estimate_root)) / 2
        if abs(sq_root - estimate_root) < epsilon:
            break
        estimate_root = sq_root
    return sq_root
    
a = 169
b = 1
print("The square root of {} is: {}".format(a, sq_root(a, b)))