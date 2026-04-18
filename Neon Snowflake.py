import turtle
import colorsys

def draw_fractal(t, length, depth, hue):
    if depth == 0:
        return
    
    color = colorsys.hsv_to_rgb(hue % 1.0, 0.8, 1.0)
    t.pencolor(color)
    t.width(depth)
    t.forward(length)
    
    for angle in [-45, 0, 45]:
        t.left(angle)
        draw_fractal(t, length * 0.6, depth - 1, hue + 0.1)
        t.right(angle)
    t.penup()
    t.backward(length)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("#000000")
    screen.title("Fractal Neon Snowflake - Click to Exit")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.tracer(5)

    arms = 8
    
    for i in range(arms):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * (360 / arms))
        t.pendown()
        draw_fractal(t, 150, 5, 0.6)
        
    t.penup()
    t.goto(0, 0)
    t.dot(20, "white")
    
    turtle.update()
    print("Fractal Crystal Stabilized. Click screen to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Captured Error: {e}")