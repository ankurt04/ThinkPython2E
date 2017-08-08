# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 09:27:12 2017

@author: Ankurt.04
"""

#Ex15.1

def point_in_circle(cir, dx, dy):
    distance = (((dx - circle1.center.x) ** 2) + ((dy - circle1.center.y) ** 2)) ** 0.5
    if distance <= circle1.radius:
        print("Point is within the circle")
        return True
    else:
        print("Point is outside the circle")
        return False
        
#def rect_in_circle():


class Point:
    """contains coordinates of center"""
    
    
class Circle:
    """Have attributes radius and 
    center. an embedded class is Point
    to have coordinates of center"""
    
    
def main():    
    circle1 = Circle()
    circle1.radius = 75.0
    circle1.center = Point()
    circle1.center.x = 150.0
    circle1.center.y = 100.0
    
    dx = 80.0
    dy = 80.0
        
    point_in_circle(circle1, dx, dy)
    

if __name__ == '__main__':
    main()