# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 10:45:14 2017

@author: Ankurt.04
"""

#Think Python - End of Chapter 4 -  In lessson exercises

import turtle
import math
bob = turtle.Turtle()


def square(t, length):
    i = 0
    while i <= 3:
        t.fd(length)
        t.lt(90)
        i +=1

#function to draw a polygon of n sides, each side lenght long
def polygon(t, length, n):
    angle = 360.0/n
    i = 0
    while i <= n:
        t.fd(length)
        t.lt(angle)
        i += 1
        
#function to draw a circle of radius r
def circle(t, r):
    #pi = 3.14
    circum = 2*math.pi*r
    length = 1
    n = circum / length
    polygon(t, length, n)
    
def arc(t, r, angle):
    #pi = 3.14
    circum = 2*math.pi*r
    desired_circum = circum * (angle/360.0)
    length = 1
    n = int(desired_circum / length)
    step_angle = angle / n
    for i in range(n):
        t.fd(length)
        t.lt(step_angle)

polygon(bob, length = 70, n = 6)  #names of parameters can be included in the argument list
arc(bob, 50, 180)
