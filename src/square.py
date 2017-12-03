# encoding: utf-8
'''
Created on 2017年11月19日

@author: niko
'''
import turtle

t = turtle.Turtle()
s = t.getscreen()

t.speed(30)
for i in range(4):
    t.fd(100)
    t.rt(90)

s.exitonclick()