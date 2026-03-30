import turtle
import colorsys

def draw_fractal_crystal():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=800)
    screen.title("Ultra-Lajawab Python Fractal Effect")
    screen.tracer(50)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.up()
    t.goto(0, -250)
    t.down()

    def draw_branch(branch_len, angle, hue):
        if branch_len < 5:
            return
        
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(color)
        t.width(branch_len / 10)
        
        t.forward(branch_len)
        
        new_len = branch_len * 0.75
        new_hue = (hue + 0.1) % 1.0
        
        t.right(angle)
        draw_branch(new_len, angle, new_hue)
        
        t.left(angle * 2)
        draw_branch(new_len, angle, new_hue)
        
        t.right(angle)
        t.up()
        t.backward(branch_len)
        t.down()

    print("Drawing the Neon Fractal Crystal...")
    draw_branch(120, 25, 0.0)
    
    t.up()
    t.goto(0, 0)
    t.setheading(0)
    for i in range(36):
        t.pencolor(colorsys.hsv_to_rgb(i/36, 1, 1))
        t.circle(200, 10)
        t.dot(10)

    print("Complete! Click the window to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    draw_fractal_crystal()