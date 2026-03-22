import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Amazing Neon Heart Animation")

t = turtle.Turtle()
t.speed(1)  
t.pensize(2)
t.hideturtle()

def heart_x(k):
    return 15 * math.sin(k)**3

def heart_y(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

def draw_amazing_heart():

    screen.tracer(1)
    
    for j in range(3): 
        t.penup()
       
        scale = 20 + (j * 2) 
        t.pensize(5 - j)
        
        for i in range(0, 630, 5):
            angle = i / 100
            
            if j == 0: t.pencolor("#ff0055")
            elif j == 1: t.pencolor("#ff77aa")
            else: t.pencolor("white")
            
            x = heart_x(angle) * scale
            y = heart_y(angle) * scale
            
            t.goto(x, y)
            t.pendown()
            
        t.penup()

    screen.tracer(5) 
    for i in range(400):
        color_hsv = colorsys.hsv_to_rgb(i/400, 0.8, 1)
        t.pencolor(color_hsv)
        
        angle = i * 0.1
        dist = (i / 400) * 20
        
        x = heart_x(angle) * dist
        y = heart_y(angle) * dist
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(t.towards(0,0))
        t.forward(2) 

    t.penup()
    t.goto(0, -50)
    t.color("white")
    t.write("i love you ❤️", align="center", font=("Verdana", 20, "bold italic"))

draw_amazing_heart()
screen.update()
turtle.done()
