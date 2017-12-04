# encoding: utf-8
'''
Created on 2017年11月12日

@author: niko
'''
import turtle

def draw_eng():
    t = turtle.Turtle()
    s = t.getscreen()
    t.penup()
    t.setx(-200)
    t.pendown()
    
    #paint N
    t.lt(90)
    t.fd(100)
    t.rt(150)
    t.fd(114)
    t.lt(150)
    t.fd(100)
    t.penup()
    
    #paint I
    t.setx(-100)
    t.pendown()
    t.rt(180)
    t.fd(100)
    t.penup()
    
    #paint K
    t.setx(-50)
    t.pendown()
    t.lt(180)
    t.fd(50)
    t.rt(150)
    t.fd(55)
    t.back(55)
    t.lt(120)
    t.fd(55)
    t.back(55)
    t.lt(30)
    t.fd(50)
    t.penup()
    
    #paint o
    t.setx(30)
    t.sety(0)
    t.rt(90)
    t.pendown()
    for i in range(2):
        t.fd(2)
        t.circle(20, 90)
        t.fd(60)
        t.circle(20, 90)
    
    s.exitonclick()
    
draw_eng()