# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:51:39 2017

@author: Ankurt.04
"""

#Chapter 8 - In chapter Exercises and examples

#reverse print a string
def rev_print(string):
    index = -1
    while abs(index) <= len(string):
        letter = string[index]
        print(letter, end=' ')
        index -= 1
        
        
rev_print('Ankur')



#string addition example
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if (letter == 'O') or (letter =='Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

        
        
#string slicing         
a = 'this is a string'
print(a[0:2])
print(a[4:])
print(a[:6])
print(a[:])




#check if strings are reverse of each other
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True
    
a = 'India'
b = 'aidni'
if is_reverse(a.upper(), b.upper()):
    print('Yes')
else:
    print('No')
    
#######