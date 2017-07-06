# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:02:01 2017

@author: Ankurt.04
"""

#Chapter 7 - end of chapter execises

#Ex 1 has already been done as part of inchapter study

import math

#Ex2
def eval_loop():
    while True: 
        a = input('Enter the calulcation that you want to carry out: ')
        if a == 'done':
            break
        b = eval(a)
        print('The result is: ', b)
    print('The result is: ', b) #if user inputs 'done' then loop breaks and prints value of last caclulated expression
    
    
eval_loop()    


#Ex3
def estimate_pi():
    product = (2 * math.sqrt(2)) / 9801
    k = 0.0
    last_term = 1.0
    term_sum = 0.0  #all these variables are initialised to a float value as they will be required to be float during caclulation (to avoid data type mismatch)
    while last_term > 1e-15:
        last_term = ((math.factorial(4.0 * k)) * (1103.0 + (26390.0 * k))) / ((math.factorial(k)**4.0) * (396.0**(4.0 * k)))
        term_sum += last_term
        k += 1.0
    #when last terms becomes less, loop exists
    result = product * term_sum
    return 1 / result
    
a = estimate_pi()
b = math.pi
print('calculated pi value is:', a)
print('module pi value is:', b)
