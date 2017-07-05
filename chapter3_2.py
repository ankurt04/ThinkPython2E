# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Think Python - End of Chapter 3 - exercises

#Ex 2-1

def do_twice(f):
    f()
    f()
    
def print_spam():
    print('Spam')

    
do_twice(print_spam)

#2-2

def do_twice(f, a):
    f(a)
    f(a)
    
def print_value(val):
    print(val)
    
do_twice(print_value, 'abc')