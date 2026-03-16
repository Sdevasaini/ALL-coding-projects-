import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2*k) - 2 * \
           math.cos(3*k) - \
           math.cos(4*k)

speed(0)          
bgcolor("black") 
pensize(2)        

for i in range(1000):

    color("#f73487") 
    
    x = hearta(i) * 20
    y = heartb(i) * 20
    
    goto(x, y)
    
    goto(0, 0)

done()