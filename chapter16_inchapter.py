# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:13:17 2017

@author: Ankurt.04
"""

#Ex 16.1
def print_time(time):
    print("Given time is %.2d:%.2d:%.2d" % (time.hour, time.min, time.sec))

 
def main():
    class Time:
        """Represents the time of the day
        
        attributes: hour, min, sec
        """
    time = Time()
    time.hour = 7
    time.min = 34
    time.sec = 29
    
    t1 = Time()
    t1.hour = 4
    t1.min = 10
    t1.sec = 45
    
    t2 = Time()
    t2.hour = 8
    t2.min = 54
    t2.sec = 12
    
    print_time(time)
    #print(is_after(t1, t2))
    
if __name__ == '__main__':
    main()
    
#Ex 16.2
def increment(time, seconds):
    
    """modifier"""
    
    time.seconds += seconds
    
    mins = time.seconds // 60
    secs = time.seconds % 60
    time.seconds = secs
    
    time.minutes += mins
    hrs = time.minutes // 60
    mins = time.minutes % 60
    time.minutes = mins
    
    time.hour += hrs
    time.hour = time.hour % 24
    
        
def main():
    class Time:
        """represents Times"""
    time = Time()
    time.hour = 5
    time.minutes = 59
    time.seconds = 57
    
    seconds = 114
    print("Given time is %.2d:%.2d:%.2d" % (time.hour, time.minutes, time.seconds))
    increment(time, seconds)
    print("Final time is %.2d:%.2d:%.2d" % (time.hour, time.minutes, time.seconds))
    
if __name__ == '__main__':
    main()
    
#Ex 16.3

class Time:
        """represents Times"""

def increment_pure(time, seconds):
    """pure"""
    final_time = Time()
    
    final_time.seconds = time.seconds + seconds
    mins = final_time.seconds // 60
    secs = final_time.seconds % 60
    final_time.seconds = secs
    
    final_time.minutes = time.minutes + mins
    hrs = final_time.minutes // 60
    mins = final_time.minutes % 60
    final_time.minutes = mins
    
    final_time.hour = time.hour + hrs
    final_time.hour = final_time.hour % 24
    
    return final_time
    
def main():
    
    time = Time()
    time.hour = 12
    time.minutes = 59
    time.seconds = 58
    
    seconds = 114
    print("Given time is %.2d:%.2d:%.2d" % (time.hour, time.minutes, time.seconds))
    final = increment_pure(time, seconds)
    print("Final time is %.2d:%.2d:%.2d" % (final.hour, final.minutes, final.seconds))
    print("Original time was %.2d:%.2d:%.2d" % (time.hour, time.minutes, time.seconds))
    
    
if __name__ == '__main__':
    main()