import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(900, 900)
screen.title("HEAVY Spirograph 🔥")

screen.tracer(10) 

t = turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()

colors = ["#FFD700", "#FFA500", "#FFFF00", "#FFCC00"]

# Base parameters
R = 220
r = 65
d = 140

for layer in range(8):  
    t.color(colors[layer % len(colors)])
    
    t.penup()
    t.goto(R - r + d, 0)
    t.pendown()
    
    for i in range(3000):  
        angle = i * 0.03
        
        x = (R - r) * math.cos(angle) + (d + layer*5) * math.cos((R - r) / r * angle)
        y = (R - r) * math.sin(angle) - (d + layer*5) * math.sin((R - r) / r * angle)
        
        t.goto(x, y)
    
    t.right(10) 

screen.update()
turtle.done()