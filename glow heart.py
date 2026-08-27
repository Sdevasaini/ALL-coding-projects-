import turtle
import math
import random

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.title("Glow heart")
screen.bgcolor("#030305")
screen.tracer(1)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
vortex_t = turtle.Turtle()
vortex_t.hideturtle()
vortex_t.speed(0)
particles = []
for _ in range(150):
    particles.append({
        'angle': random.uniform(0, 2 * math.pi),
        'radius': random.uniform(50, 400),
        'speed': random.uniform(0.01, 0.03),
        'size': random.randint(1, 3),
        'color': random.choice(["#ff0055", "#00f0ff",
         "#7000ff", "#00ffcc", "#ffcc00"])
    })

color_palettes = [
    ["#ff0055", "#ff3399", "#ff66cc", "#ff99ee"],
    ["#00f0ff", "#0088ff", "#7000ff", "#cc00ff"],
    ["#00ffcc", "#33ff33", "#ffff00", "#ff9900"],
    ["#ff2a6d", "#d1f7ff", "#05d9e8", "#ff007f"] 
]
current_palette_idx = 0

def heart_coords(t_val, scale=1.0):
    x = 16 * (math.sin(t_val) ** 3)
    y = (13 * math.cos(t_val) - 
         5 * math.cos(2 * t_val) - 
         2 * math.cos(3 * t_val) - 
         math.cos(4 * t_val))
    return x * scale, y * scale

def draw_vortex():
    vortex_t.clear()
    for p in particles:
        p['angle'] += p['speed']
        x = p['radius'] * math.cos(p['angle'])
        y = p['radius'] * math.sin(p['angle'])
        vortex_t.penup()
        vortex_t.goto(x, y)
        vortex_t.pendown()
        vortex_t.color(p['color'])
        vortex_t.dot(p['size'])

def draw_neon_tunnel(pulse_offset=0):
    draw_vortex()
    palette = color_palettes[current_palette_idx]
    layers = 12
    for i in range(layers, 0, -1):
        scale_factor = (i * 2.2) + (math.sin(pulse_offset + i * 0.4) * 1.5)
        color_idx = i % len(palette)
        t.penup()
        t.color(palette[color_idx])
        t.pensize(max(1, 4 - (i // 3)))
        first = True
        theta = 0
        while theta <= 2 * math.pi + 0.1:
            hx, hy = heart_coords(theta, scale=scale_factor)
            twist = i * 0.05
            rx = hx * math.cos(twist) - hy * math.sin(twist)
            ry = hx * math.sin(twist) + hy * math.cos(twist)
            
            if first:
                t.goto(rx, ry)
                t.pendown()
                first = False
            else:
                t.goto(rx, ry)
            theta += 0.08
        t.penup()

   
    t.color("#ffffff")
    t.pensize(2)
    first = True
    theta = 0
    while theta <= 2 * math.pi + 0.1:
        hx, hy = heart_coords(theta, scale=3.0)
        if first:
            t.goto(hx, hy)
            t.pendown()
            first = False
        else:
            t.goto(hx, hy)
        theta += 0.05
    t.penup()
    screen.update()

def render_hud():
    t.penup()
    t.goto(0, 370)
    t.color("#00f0ff")
    t.write("", align="center", font=("Courier", 18, "bold"))
    t.goto(0, -385)
    t.color("#ff0055")
    t.write("", align="center", font=("Courier", 12, "normal"))

anim_step = 0
def handle_click(x, y):
    global current_palette_idx, anim_step
    current_palette_idx = (current_palette_idx + 1) % len(color_palettes)
    anim_step += 0.8
    t.clear()
    draw_neon_tunnel(pulse_offset=anim_step)
    render_hud()

if __name__ == "__main__":
    t.hideturtle()
    draw_neon_tunnel(pulse_offset=0)
    render_hud()
    screen.onclick(handle_click)
    screen.mainloop()