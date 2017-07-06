# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:22:04 2017

@author: Ankurt.04
"""

#Chapter 8 exercises

#Ex2

word = 'banana'
print(word.count('a'))


#Ex3
def is_palindrome(word1, word2):
    word3 = word1[::-1]
    if word3 == word2:
        print('Palindrome')
    else:
        print('not palindrome')
    
a = 'india'
b = 'aidnI'
is_palindrome(a, b)

#Ex4
def any_lowercase1(s):     #Outputs true only if first character is lowercase. Returns after checking only first character
    for c in s:
        if c.islower():
            return True
        else:
            return False

#def any_lowercase2(s) is wrong - wont work
            
def any_lowercase3(s):    #Outputs true only if last character is lowercase. Checks all characters.
    for c in s:
        flag = c.islower()
    return flag
            

def any_lowercase4(s):    #works fine - outputs True if any character is lowercase. Checks all characters.
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):  #Returns false the moment it encounters any uppercase and loop ends
    for c in s:
        if not c.islower():
            #print(c)
            return False
    return True    

a = 'TEGv'
b = 'TBBvF'
c = 'cZfefe'
print(any_lowercase1(a))
print(any_lowercase3(a))
print(any_lowercase4(b))
print(any_lowercase5(c))

#Ex5  -- this is a good question for discussion
def rotate_word(string, number):
    new_word = ''
    word = string.lower()  
    number = number % 26  #make the number lie between 0 to 25
    for c in word:
        if c == ' ':
            order = ord(c)
        else: 
            order = ord(c) + number
            if order > ord('z'):
                order = order - 26 #make the number jump from 122 [ord(z)] to 97 [ord(a)]
        new_word += chr(order)
            
    print(new_word)
    
sentence = 'This is going to be an encrypted joke'
nu = 13 #rotate by this number
rotate_word(sentence, nu)


    