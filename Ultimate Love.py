import turtle
import math
import random

def setup_environment():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Ultimate Love")
    screen.tracer(0)
    return screen

class VortexParticle:
    def __init__(self):
        self.reset()
        self.history = [(self.x, self.y)] * 5

    def reset(self):
        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color_base = random.random()
        self.target_angle = random.uniform(0, 2 * math.pi)

    def update(self, t, mouse_x, mouse_y):
        self.history.append((self.x, self.y))
        self.history.pop(0)
        scale = 15 + 3 * math.sin(t * 0.03)
        heart_x = 16 * math.sin(self.target_angle)**3 * scale
        heart_y = (13 * math.cos(self.target_angle) - 5 * math.cos(2*self.target_angle) - 
                   2 * math.cos(3*self.target_angle) - math.cos(4*self.target_angle)) * scale
        dx, dy = heart_x - self.x, heart_y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        self.vx += dx * 0.002
        self.vy += dy * 0.002
        self.vx += -dy * 0.001
        self.vy += dx * 0.001

        mdx, mdy = self.x - mouse_x, self.y - mouse_y
        dist_mouse = math.sqrt(mdx**2 + mdy**2)
        if dist_mouse < 150:
            self.vx += (mdx / (dist_mouse + 1)) * 3
            self.vy += (mdy / (dist_mouse + 1)) * 3

        self.vx *= 0.94
        self.vy *= 0.94
        self.x += self.vx
        self.y += self.vy

def main():
    screen = setup_environment()
    t = turtle.Turtle()
    t.hideturtle()
    t.width(2)
    
    particles = [VortexParticle() for _ in range(250)]
    mouse_pos = [1000, 1000]
    
    def update_mouse(x, y):
        mouse_pos[0], mouse_pos[1] = x, y
        
    screen.onscreenclick(update_mouse)
    screen.listen()
    
    time = 0
    try:
        while True:
            t.clear()
            for p in particles:
                p.update(time, mouse_pos[0], mouse_pos[1])
                
                for i in range(len(p.history) - 1):
                    intensity = 0.2 + (i / len(p.history)) * 0.8
                    t.pencolor(intensity, 0.2, 0.5 + 0.5 * math.sin(time * 0.02))
                    t.penup()
                    t.goto(p.history[i])
                    t.pendown()
                    t.goto(p.history[i+1])
            
            screen.update()
            time += 1
            
    except turtle.Terminator:
        pass

if __name__ == "__main__":
    main()