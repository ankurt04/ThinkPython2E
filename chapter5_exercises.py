# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:30:05 2017

@author: Ankurt.04
"""
#Ex1
import time

def current_time():
    a = time.localtime(time.time())
    local_time = time.asctime(a)
    print(a)
    print("the year is:", a[0])
    print("the month is:", a[1])
    print(local_time)
    time_since_epoch = ((a[0] - 1970)*365)+(a[1]*30)
    print("Days since Epoch are:", time_since_epoch)
    
current_time()

#Ex2
def check_fermat(a, b, c, n):
    if n > 2:
        if (a**n) + (b**n) == c**n:
            print("Holy smokes! Fermat was wrong!")
        else: 
            print("No, that doesn't work")
    else: 
        print("Value of exponant n must be greater than 2 to check fermat's theorem")

def fermat_inputs():
    a = int(input("Input value of a check fermat's theorem:"))
    b = int(input("Input value of b check fermat's theorem:"))
    c = int(input("Input value of c check fermat's theorem:"))
    n = int(input("Input value of n check fermat's theorem:"))
    check_fermat(a, b, c, n)
    
    
#fermat_inputs()


#Ex3
def is_triangle(a, b, c):
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        print("No")
    else: 
        print("Yes")
        
def triangle_input():
    a = int(input("Input first side a:"))
    b = int(input("Input second side b:"))
    c = int(input("Input third side c:"))
    is_triangle(a, b, c)
    
triangle_input()