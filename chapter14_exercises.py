# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:26:58 2017

@author: Ankurt.04
"""

#Chapeter 14 End of chapter exercises

#Ex 14.1

def sed(pat_str, rep_str, file1, file2):
    try:
        fin = open(file1)
    except:
        print("Can't open file %s" %file1)
        return
        
    try:
        fout = open(file2, 'w')
    except:
        print("Can't open file %s" %file2)
        return
        
    for line in fin:
        word = line.replace(pat_str, rep_str)
        try:
            fout.write(word)
        except:
            print("Can't write in file %s" %file2)
            return
    try:
        fout.close()   
    except:
        print("Can't close file %s" %file2)
        return
    try:
        fin.close()
    except:
        print("Can't close file %s" %file1)
        return
            

pat_str = "Made in China" #pattern string to be replaced
rep_str = "Make in India" #new string to be placed
file1 = "production.txt"  #original file
file2 = "newproduction.txt" #new file
        
sed(pat_str, rep_str, file1, file2)


#Ex 14.3


