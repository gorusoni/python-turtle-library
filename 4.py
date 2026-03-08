from turtle import *
import colorsys
bgcolor('black')
speed(0)
n = 100
h = 1
for i in range(250):
    c = colorsys.hsv_to_rgb(h ,1,0.8)
    pencolor(c)
    h += 1/n 
    forward(i+1)
    right(221)
    forward(i+2)
    right(98)
    left(90)
done