import turtle
import math
import colorsys
import random
import time

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("#08020f")
screen.title("Rose Heart")
screen.tracer(5)
bg_pen = turtle.Turtle()
bg_pen.hideturtle()
petal_pen = turtle.Turtle()
petal_pen.hideturtle()
glow_pen = turtle.Turtle()
glow_pen.hideturtle()
text_pen = turtle.Turtle()
text_pen.hideturtle()

def get_heart_point(t, scale=15.0):

    x = scale * (16 * (math.sin(t) ** 3))
    y = scale * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
    return x, y

stars = []
for _ in range(110):
    sx = random.randint(-420, 420)
    sy = random.randint(-420, 420)
    if math.hypot(sx, sy) > 160:
        stars.append({
            'x': sx,
            'y': sy,
            'size': random.uniform(0.8, 2.6),
            'phase': random.uniform(0, math.pi * 2),
            'color': random.choice(["#ffb3de", "#e2b6ff", "#7bf0ff", "#ffffff", "#ffd700"])
        })

def draw_stars(frame):
    bg_pen.clear()
    for star in stars:
        twinkle = 0.5 + 0.5 * math.sin(frame * 0.08 + star['phase'])
        bg_pen.penup()
        bg_pen.goto(star['x'], star['y'])
        bg_pen.color(star['color'])
        bg_pen.dot(star['size'] * twinkle)

def draw_radiant_rays(frame, beat_scale):
    glow_pen.clear()
    num_rays = 24
    hue_base = (frame * 0.005) % 1.0
    
    for i in range(num_rays):
        angle = (i / num_rays) * (2 * math.pi) + frame * 0.015
        length = (140 + 35 * math.sin(frame * 0.1 + i)) * beat_scale
        tx = math.cos(angle) * length
        ty = math.sin(angle) * length + 20
        r, g, b = colorsys.hsv_to_rgb((hue_base + i * 0.03) % 1.0, 0.7, 0.25)
        glow_pen.color((r, g, b))
        glow_pen.width(1.5)
        glow_pen.penup()
        glow_pen.goto(0, 20)
        glow_pen.pendown()
        glow_pen.goto(tx, ty)

def draw_blooming_rose_heart(frame, beat_scale):
    petal_pen.clear()
    
    total_layers = 48
    hue_shift = (frame * 0.006) % 1.0
    
    for layer in range(total_layers, 0, -1):
        progress = layer / total_layers
        scale = (0.5 + progress * 15.0) * beat_scale
        spiral_angle = layer * 0.12 + math.sin(frame * 0.04) * 0.2
        layer_hue = (0.85 + hue_shift + progress * 0.22) % 1.0
        sat = 0.85 + 0.15 * math.sin(layer * 0.3)
        val = 0.25 + 0.75 * progress
        r, g, b = colorsys.hsv_to_rgb(layer_hue, sat, val)
        petal_pen.color((r, g, b))
        petal_pen.width(1.2 + progress * 2.2)
        points = []
        steps = 64
        for i in range(steps + 1):
            t = (i / steps) * (2 * math.pi)
            hx, hy = get_heart_point(t, scale=scale)
            
            cos_a = math.cos(spiral_angle)
            sin_a = math.sin(spiral_angle)
            rx = hx * cos_a - hy * sin_a
            ry = hx * sin_a + hy * cos_a + 20 
            points.append((rx, ry))
        
        if points:
            petal_pen.penup()
            petal_pen.goto(points[0][0], points[0][1])
            petal_pen.pendown()
            for px, py in points[1:]:
                petal_pen.goto(px, py)

def draw_typography(frame):
    text_pen.clear()
    
    pulse_val = 0.75 + 0.25 * math.sin(frame * 0.1)
    text_pen.penup()
    text_pen.goto(0, -342)
    text_pen.color("#ff007f")
    #text_pen.write("❖", align="center", font=("Georgia", 18, "bold"))
    text_pen.goto(0, -340)
    r, g, b = colorsys.hsv_to_rgb(0.92, 0.2, pulse_val)
    text_pen.color((r, g, b))
    text_pen.write("❖ ", align="center", font=("Georgia", 18, "bold"))
    text_pen.goto(0, -370)
    text_pen.color("#9ba8cb")

def main():
    print("")
    print("")
    
    frame = 0
    try:
        while True:
            beat_phase = (frame * 0.1) % (math.pi * 2)
            beat_scale = 1.0 + 0.07 * (math.sin(beat_phase) ** 3) + 0.03 * math.sin(beat_phase * 2)
            draw_stars(frame)
            draw_radiant_rays(frame, beat_scale)
            draw_blooming_rose_heart(frame, beat_scale)
            draw_typography(frame)
            screen.update()
            frame += 1
            time.sleep(0.016)
            
    except (turtle.Terminator, Exception):
        print("")

if __name__ == "__main__":
    main()