import turtle
import math

class MercedesLogo:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=700, height=700)
        self.screen.bgcolor("white")
        self.screen.title("Mercedes-Benz")
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(1)
        self.t.pensize(2)
        self.outer_radius = 200
        self.ring_thickness = 18
        self.inner_star_ratio = 0.18
        
    def draw_thick_ring(self):
        self.t.penup()
        self.t.goto(0, -self.outer_radius)
        self.t.setheading(0)
        self.t.pendown()
        self.t.color("black")
        self.t.begin_fill()
        self.t.circle(self.outer_radius)
        self.t.penup()
        self.t.goto(0, -(self.outer_radius - self.ring_thickness))
        self.t.pendown()
        self.t.circle(self.outer_radius - self.ring_thickness)
        self.t.end_fill()

    def draw_star(self):
        self.t.penup()
        self.t.goto(0, 0)
        self.t.color("black")
        self.t.begin_fill()
        tip_radius = self.outer_radius - (self.ring_thickness / 2)
        waist_radius = tip_radius * self.inner_star_ratio
        
        points = []
        for i in range(3):
            angle_tip = math.radians(90 + i * 120)
            angle_waist = math.radians(90 + i * 120 + 60)
            points.append((tip_radius * math.cos(angle_tip), tip_radius * math.sin(angle_tip)))
            points.append((waist_radius * math.cos(angle_waist), waist_radius * math.sin(angle_waist)))
            
        self.t.goto(points[0])
        self.t.pendown()
        for point in points[1:]:
            self.t.goto(point)
        self.t.goto(points[0])
        
        self.t.end_fill()

    def render(self):
        self.draw_thick_ring()
        self.draw_star()
        self.t.penup()
        self.t.goto(0, -260)
        self.t.write("Mercedes-Benz", align="center", font=("Arial", 24, "bold"))
        self.screen.exitonclick()

if __name__ == "__main__":
    logo = MercedesLogo()
    logo.render()