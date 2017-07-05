# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:09:38 2017

@author: Ankurt.04
"""

#In chapter 6 Examples

#compare function
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
        

a = compare(3, 1)
b = compare(0, 1)
c = compare(5, 5)

print(a, b, c)
    

#boolen conditions
def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
         return False

if is_between(4,6,8):
    print('function has returned true')
else: 
    print('function has returned false')
    
#