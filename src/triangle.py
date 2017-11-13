# encoding: utf-8
'''
Created on 2017年11月12日

@author: niko
'''
import turtle


def draw_triangle():
    t = turtle.Turtle()
    s = t.getscreen()
    t.penup()
    t.setx(-200)
    t.sety(-200)
    t.pendown()
    len = 50
    angle = 120
    max = 8
    t.speed(10)
    t.begin_fill()
    for i in range(1, max + 1):
        if i > (max / 2):
            num = max - i
        else:
            num = i
        t.fd(len)
        if i == max:
            break
        else:
            rdraw(t, angle, num, len)
    t.lt(angle)        
    t.fd(len * max)
    t.lt(angle)
    t.fd(len * max)
    t.color("green")
    t.end_fill()
    
    
    t.lt(angle)
        
    s.exitonclick()
    pass

def rdraw(t, angle, num, len):
    t.lt(angle)
    tlen = len
    if num % 2 == 0:
        tlen = len * num
    t.fd(tlen)
    t.rt(angle)
    t.fd(len)
    
    if num % 2 == 0:
        for i in range(1, num):
            rdraw(t, angle, i, len)
            t.fd(len)
    t.rt(angle)
    t.fd(tlen)
    t.lt(angle)  
    pass
draw_triangle()