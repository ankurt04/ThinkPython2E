# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:03:39 2017

@author: Ankurt.04
"""

#Ex 15.1
"""Take two points as arguments 
and return the distance
between them. 

Two points of a class

"""

def distance_between_points(p1, p2):
    distance = (((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2)) ** 0.5
    print("Distance between given two points is %g" %distance)
    return distance
    
class Point:
    """Represent a point in 2-D space"""
    
point1 = Point()
point2 = Point()

point1.x = 5
point1.y = 5

point2.x = 3
point2.y = 3

z = distance_between_points(point1, point2)

#Ex 15.2
"""Move the corner 
of a rectangle
by given points"""

def move_rectangle(rect, dx, dy):
    print("Given coordinates of the rectangle are %g and %g" %(rect.corner.x, rect.corner.y))
    rect.corner.x += dx
    rect.corner.y += dy
    print("New coordinates for the given corner of the rectangle are %g and %g" %(rect.corner.x , rect.corner.y))
    return rect
    
class Rectangle:
    """defined length and width of a rectangle
    and the coordiantes of a corner"""

    
box = Rectangle()
box.lenth = 10.0
box.height = 5.0
box.corner = Point()
box.corner.x = 0
box.corner.y = 0

z = move_rectangle(box, 5, 0)
print(box)


