# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:34:55 2017

@author: Ankurt.04
"""

#Chapter 6 - end of chapter


#Ex 6.2
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
       return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    
a = ack(3,4)
print(a)

#Ex 6.4
def is_power(a, b):
    if b == 0:
        return False
    elif a % b == 0:
        return True
    else:
        return False

if is_power(45, 9):
    print("true")
else: 
    print("false")
    
#Ex 6.5
def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)
        
a = gcd(5,4)
print(a)