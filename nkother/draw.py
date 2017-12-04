# encoding: utf-8
'''
Created on 2017年11月12日

@author: niko
'''
from turtle import Turtle

def drawSquare():
    myt = Turtle()
    mys = myt.getscreen()
    mys.bgcolor("red")
    myt.color("yellow")
    myt.shape("turtle")
    myt.speed(2)
    
    for i in range(4) :
        myt.forward(100)
        myt.right(90)
    
    angie = Turtle()
    angie.penup()
    angie.sety(50)
    angie.pendown()
    angie.shape("triangle")
    angie.color("blue")
    angie.circle(100)
    
    third = Turtle()
    third.penup()
    third.setx(-50)
    third.pendown()
    third.shape("turtle")
    third.color("black")
    for i in range(3):
        third.backward(100)
        third.right(120)
    
    mys.exitonclick()

#画菱形
def draw_rhombus(rh_t):
    for i in range(2):
        rh_t.forward(50)
        rh_t.right(30)
        rh_t.forward(50)
        rh_t.right(150)

def draw_flower():
    t1 = Turtle()
    s = t1.getscreen()
    t1.speed(10)
    s.bgcolor("white")
    t1.color("blue")
    for i in range(30 * 4):
        if (i % 2) == 0 :
            t1.begin_fill()
        else :
            t1.color("blue")
        draw_rhombus(t1)
        t1.right(3)
        if (i % 2) == 0 :
            t1.color("yellow")
            t1.end_fill()
            
    for i in range(10):
        draw_rhombus(t1)
        t1.right(3)
        
    t1.right(60)
    t1.forward(200)
        
    s.exitonclick()
    
if __name__ == '__main__':
    draw_flower()
    pass