import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Interstellar Wormhole")
screen.tracer(0)
artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)

def draw_wormhole():
    steps = 1000
    hue = 0
    
    for i in range(steps):
        angle = i / 10
        radius = i * 0.5
        for arm in range(8):
            x = math.cos(angle + (arm * (2 * math.pi / 8))) * radius
            y = math.sin(angle + (arm * (2 * math.pi / 8))) * radius
            hue = (i / steps + arm / 8) % 1
            color = colorsys.hsv_to_rgb(hue, 0.8, 1)
            artist.pencolor(color)
            artist.penup()
            artist.goto(x, y)
            artist.pendown()
            artist.dot(2)
        
        if i % 2 == 0:
            screen.update()

def main():
    try:
        draw_wormhole()
        screen.exitonclick()
    except turtle.Terminator:
        print("Wormhole collapsed.")

if __name__ == "__main__":
    main()