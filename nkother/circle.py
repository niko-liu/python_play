# encoding: utf-8
'''
Created on 2017年11月19日

@author: niko
'''
import turtle

t = turtle.Turtle()
s = t.getscreen()

t.speed(30)
for i in range(36):
    t.circle(55)
    t.rt(10)

s.exitonclick()