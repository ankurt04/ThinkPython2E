# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:54:15 2017

@author: Ankurt.04
"""

"""
"""
#Ex 12.1

def create_histogram(s): #dictionary with letters and frequencies
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
    
def most_frequent(s):
    t = []
    d = create_histogram(s)
    for key, freq in d.items(): #d.item returns dict's key value pair as tuples
        t.append((freq, key))
    t.sort(reverse = True)
    #print(t)
    final = []
    for freq, key in t:
        final.append(key)
    #print(final)
    return(final)
        
        
s = 'abcdefabddccc'
most_frequent(s)
        
    
#Ex 12.2