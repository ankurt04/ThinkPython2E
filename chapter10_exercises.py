# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:25:23 2017

@author: Ankurt.04
"""

"""
Chapter 10 - exercise at the end of the chapter 10
"""

#Ex 10.1
"""
list t has to be a list of list of integers
"""
def nested_sums(t):
    f_sum = 0
    for i in t:
        f_sum += sum(i)
    return f_sum
    
    
t = [[1, 2], [4, 5], [2, 12], [21, 22]]
a = nested_sums(t)
print(a)


#Ex 10.2
"""
list t has to be a list of integers
"""
def cumsum(t):
    new_t = []
    i = 0
    while i < len(t):
        new_t.append(sum(t[:i+1]))
        i += 1
    return new_t
    
t = [1, 3, 5, 7, 9]
a = cumsum(t)
print(a)


#Ex 10.3
def middle(t):
    new_t = t[1:-1]
    return new_t
    
t = [4, 5, 6, 7, 8, 9, 12, 13, 14]
a = middle(t)
print(a)    


#Ex 10.4
def chop(t):
    del t[0]  #del returns None
    del t[-1]
    return t
    
t = [11, 22, 33, 44, 55, 66, 77]
a = chop(t)
print(t)

#Ex 10.5
def is_sorted(t):
    p = t[:]
    p.sort()
    if p == t:
        return True
    else:
        return False
        
t = [3, 13, 1, 56, 23, 0, 67, 0, 1, 45, 6, 1, 0, 99]
t1 = [0, 1, 2, 3]
print(is_sorted(t1))

"""
anagrams will have same number of 
letters but can have differnt number of spaces

e.g.  'abcd' and 'ab cd' are anagrams

so, both string must be converted into lists and have their
space i.e. ' ' removed if any. 
"""
#Ex 10.6
def is_anagram(s1, s2): #
    s3 = list(s1)
    s4 = list(s2)
    if ' ' in s3:
        s3.remove(' ')
    if ' ' in s4:
        s4.remove(' ')
    if len(s3) != len(s4):
        return False
    else:
        for s in s3:
            if s in s4:
                continue
            else:
                return False
        return True
        
        
s1 = 'ab cd'
s2 = 'cabd'
print(is_anagram(s1, s2))


#Ex 10.7

