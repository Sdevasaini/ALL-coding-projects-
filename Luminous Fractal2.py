import turtle
import colorsys

def draw_luminous_art():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Luminous Fractal Art")
    screen.setup(width=900, height=900)
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(5)
    t.hideturtle()
    start_hue = 0.1
    end_hue = 0.55

    for i in range(400):
        progress = i / 400
        current_hue = start_hue + (progress * (end_hue - start_hue))
        color = colorsys.hsv_to_rgb(current_hue, 0.9, 1)
        t.pencolor(color)
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 15) 
        t.pendown()
        t.forward(i * 0.8)
        t.right(45)
        t.circle(i * 0.3, 90)
        t.width(i // 100 + 1)
        t.left(90)
        t.circle(i * 0.3, 90)

        if i % 10 == 0:
            screen.update()
    screen.update()
    print(" ")
    screen.exitonclick()

if __name__ == "__main__":
    try:
        draw_luminous_art()
    except:
        pass