# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:16:02 2017

@author: Ankurt.04
"""
#Ex 17.1 
""" time_to_int rewritten as method """

class Time:
    """Represent the time of the day """
    def time_to_int(self):
        mins = (self.hour * 60) + self.minutes
        secs = (mins * 60) + self.seconds
        #return secs
        print(secs)
        

def main():
    lecture_duration = Time()
    lecture_duration.hour = 1
    lecture_duration.minutes = 5
    lecture_duration.seconds = 10
    
    lecture_duration.time_to_int()
    
    
if __name__ == '__main__':
    main()


#Ex 17.2

        
        