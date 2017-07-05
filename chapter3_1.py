# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Think Python - End of Chapter 3 - exercises

#Ex1

def right_justify(s):
    a = len(s)
    if a <= 70:
        b = 70 - a
        blank_spaces = ' ' * b
        final_string = blank_spaces + s
        print("length of blank spaces is:", len(blank_spaces))
    else:  #if argument string's length is more than 70 then shorten it from the beginning so that last latter displays on 70
        b = a - 70
        final_string = s[b:a]
    print(final_string)
    
input_string = input('Enter a string:')
right_justify(input_string)


#Ex2

