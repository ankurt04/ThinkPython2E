# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:48:54 2017

@author: Ankurt.04
"""

#Ex 11.1

file_dict = dict()

def file_into_dict():
    fin = open('words.txt')
    #print(fin)
    global file_dict
    for f in fin:
        #f = fin.readline() #copy the present line in a varaible
        
        file_dict[f.strip()] = 'A'
        
file_into_dict()    
#print(file_dict)
#print(len(file_dict)) 

test_string = 'Tiger'

a = test_string.lower() in file_dict #words.txt contains words in lowercase
print(a)
    

#Ex 11.2
"""
concise version of invert_dict based on 
setdefault method of dict

setdefault(key, default ), created the new key with value as default 
if key is not found
"""

def invert_dict(d):
    invert = dict()
    for c in d:
        val = d[c]
        invert.setdefault(val, [])
        invert[val].append(c)
    return invert
    
d = {'a': 1, 'b': 1, 'n': 5, 'z': 3, 'r': 2}
z = invert_dict(d)
print(d)
print(z)

#Ex 11.3

#Ex 11.4
def has_duplicates(t):
    #test_list = t[:]
    d = dict()
    for c in t:
        d.setdefault(c, 0) #this statement will do nothing if a key already exist
        d[c] += 1
        if d[c] > 1:
            print(d)
            return True #function returns as soon as it finds first duplicate value
    return False
    
  
t = ['a', 'b', 'c', 'd', 'c', 'e', 'z', 'd']
print(has_duplicates(t))
print(t)  #list remains unchanged

   