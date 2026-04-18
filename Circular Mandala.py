import turtle

def draw_satisfying_pattern():
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Simple & Satisfying Art")
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(1)
    t.pencolor("#00f2ff")
    for i in range(60):
        t.circle(100) 
        t.left(6)    
        
    t.hideturtle()
    print("Done! Click on the window to close.")
    screen.exitonclick()

if __name__ == "__main__":
    draw_satisfying_pattern()