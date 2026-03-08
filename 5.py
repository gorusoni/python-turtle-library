from turtle import *
import colorsys

bgcolor('black')
speed(0)
n =79
h=0
for i in range(368):
    c = colorsys.hsv_to_rgb(h , 1,0.8)
    h += 1/n
    pencolor(c)
    pensize(0)
    forward(i+1)
    circle(2,3)
    forward(i+2)
    left(34)
    right(56)
    circle(0,57)
done
