# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:09:30 2017

@author: Ankurt.04
"""

#Chapter 6 - Ex 2 - Palindrome
def first_word(word):
    return word[0]
    
def last_word(word):
    return word[-1]
    
def middle(word):
    return word[1:-1]
    
    
str = 'abcde'

print(first_word(str))
print(last_word(str))
print(middle(str))


def is_palindrome(word):
   word1 = word
   while len(word1) > 1:
        if first_word(word) == last_word(word):
            word1 = middle(word1)
            continue
        else: 
            return False
   return True
    
    
str1 = 'ab'  
print(is_palindrome(str1))
        