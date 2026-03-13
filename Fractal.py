import turtle
import colorsys

def draw_amazing_fractal():

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Amazing Neon Fractal Design")
    
    t = turtle.Turtle()
    t.speed(12)
    t.width(1)
    t.hideturtle()
    
    turtle.tracer(23332, 33333)
    
    hue = 0.0
    
    for i in range(400):
        color = colorsys.hsv_to_rgb(hue, 0.8, 1)
        t.pencolor(color)
        hue += 0.003
        
        t.forward(i)
        t.right(100) 
        
        if i % 2 == 0:
            t.circle(i * 0.5, 90) 
            t.right(70)
        else:
            t.circle(i * 0.2, -90)
            t.left(70)
            
        if i % 2 == 0:
            screen.update()

    screen.update()
    print("Amazing Design Complete!")
    screen.exitonclick()

if __name__ == "__main__":
    draw_amazing_fractal()
