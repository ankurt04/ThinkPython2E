# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:07:47 2017

@author: Ankurt.04
"""

#Chapter 9
    
#Ex 9.1
fin = open('words.txt')
for l in fin:
    word = fin.readline()
    if len(word) > 20:
        print(word)
  

#Ex 9.2
def has_no_e(word):  #return True / word, if word has no e
    for c in word:
        if c != 'e':
            continue
        else: 
            return False
    return word

fin = open('words.txt')
t_sum = 0
all_sum = 0    
for l in fin:
    word = fin.readline()
    a = has_no_e(word)
    all_sum += 1
    if a != False:
        t_sum += 1
        print(a)
per = (t_sum / all_sum) * 100
print('Percentage of the words that has no e is: ' + str(round(per, 2)) +'%')


#Ex9.3
def avoids(word, forbidden_string): #Returns True if word contain any letter from forbidden_string
    counter = 0
    while counter < len(word):
        if word[counter] in forbidden_string:
            return False
        else:
            counter += 1
            continue
    return word #True
    
forbidden_string = input("Enter the string of forbidden characters: ")
fin = open('words.txt')
for w in fin:
    word = fin.readline()
    result = avoids(word, forbidden_string)
    if result != False:
        print(result)



#Ex 9.4
def uses_only(word, mandatory_string): #Returns true if word contains only letters from mandatory_string
    d = 0
    while d < len(word):
        if word[d] in mandatory_string:
            d += 1
            continue
        else:
            return False
    return True


word = 'Ankur'
mandatory_string = 'Ankurfghfghgfhf'
print(uses_only(word, mandatory_string))        
        

"""
Function returns True if word contains 
all characters of required_string atleast one
"""        
#Ex 9.5
def uses_all(word, required_string):
    d = 0
    while d < len(required_string):
        if required_string[d] in word:
            d += 1
            continue
        else:
            return False
    return True
    
word = 'Ankur'
required_string = 'AArrrnnnuuuuukkk'
print(uses_all(word, required_string))


#Ex 9.6
"""
Function returns true if letters in word
are in alphabetical order
same letter multiple times is okay
if it is at right place

"""
def is_abecedarian(word):
    new_word = word.lower()  #first convert all letters into lowercase
    #print(new_word)
    z = len(word) - 1
    #print(z)
    d = 0
    while d < z:
        if ord(new_word[d] ) <= ord(new_word[d+1]):
            d += 1
            continue
        else:
            return False
    return True

    
word = 'AbcdeZ'
a = is_abecedarian(word)
print(a)
    