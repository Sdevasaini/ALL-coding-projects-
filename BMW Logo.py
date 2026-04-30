import turtle
import math

def draw_digital_bmw():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#050505")
    screen.title("BMW")
    screen.tracer(1)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    COLORS = {
        "blue": "#0066AD",
        "white": "#FFFFFF",
        "chrome": "#E0E0E0",
        "grid": "#222222"
    }
        
    def draw_tech_ring(radius, width, color, segments=120):
        t.penup()
        t.pencolor(color)
        t.width(width)
        for i in range(segments + 1):
            angle = (i / segments) * 360
            rad = math.radians(angle)
            x = radius * math.cos(rad)
            y = radius * math.sin(rad)
            if i == 0:
                t.goto(x, y)
                t.pendown()
            else:
                t.goto(x, y)
    t.width(1)
    t.pencolor(COLORS["grid"])
    for i in range(-400, 401, 40):
        t.penup(); t.goto(i, -400); t.pendown(); t.goto(i, 400)
        t.penup(); t.goto(-400, i); t.pendown(); t.goto(400, i)

    for r in range(200, 215, 3):
        draw_tech_ring(r, 1, COLORS["chrome"])

    line_spacing = 4
    quad_r = 140
    for i in range(4):
        start_angle = i * 90
        color = COLORS["white"] if i % 2 == 0 else COLORS["blue"]
        t.pencolor(color)
        t.width(2)
        
        for step in range(0, 91, 1):
            angle = math.radians(start_angle + step)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.goto(quad_r * math.cos(angle), quad_r * math.sin(angle))
        screen.update()

    letters = [("B", 130), ("M", 90), ("W", 50)]
    for char, angle in letters:
        rad = math.radians(angle)
        x = 172 * math.cos(rad)
        y = 172 * math.sin(rad)
        
        for offset in range(3, 0, -1):
            t.penup()
            t.goto(x, y - 25)
            alpha = 1 - (offset / 4)
            t.pencolor((alpha, alpha, alpha)) 
            t.write(char, align="center", font=("Courier", 45, "bold"))
    draw_tech_ring(140, 5, COLORS["chrome"])

    screen.update()
    print("Digital BMW Loop Complete.")
    screen.mainloop()

if __name__ == "__main__":
    draw_digital_bmw()