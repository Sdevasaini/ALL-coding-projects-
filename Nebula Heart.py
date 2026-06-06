import turtle
import math
import random
import colorsys

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#000000")
    screen.title("Nebula Heart")
    screen.tracer(300)
    swarm_size = 300
    particles = []
    
    for _ in range(swarm_size):
        p = turtle.Turtle(shape="circle")
        p.speed(0)
        p.penup()
        p.shapesize(0.2)
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(50, 300)
        p.goto(dist * math.cos(angle), dist * math.sin(angle))
        particles.append(p)

    for frame in range(500):
        for i, p in enumerate(particles):
            x, y = p.pos()
            
            t = (frame * 0.02) + (i * 0.1)
            target_x = 16 * (math.sin(t)**3) * 15
            target_y = (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * 15
            dx = (target_x - x) * 0.05
            dy = (target_y - y) * 0.05
            p.goto(x + dx, y + dy)
        
            energy = 1 - (math.sqrt(x**2 + y**2) / 400)
            hue = (0.7 + energy * 0.3) % 1.0
            r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
            p.color(r, g, b)
            p.pendown()
            p.pensize(1)
            
        screen.update()
        if frame % 10 == 0:
            p.pencolor(0, 0, 0)
            
    turtle.done()

if __name__ == "__main__":
    main()