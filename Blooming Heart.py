import turtle
import math
import random
import time

screen = turtle.Screen()
screen.setup(width=1000, height=850)
screen.bgcolor("#02010a")  # Polar arctic midnight void
screen.title("Aurora Borealis Celestial Heart — Python Arctic Masterpiece")
screen.tracer(0)  # Manual buffer for silky smooth 60 FPS animation

bg_pen = turtle.Turtle()          # Starfield and shooting meteors
mountain_pen = turtle.Turtle()    # Silhouetted polar ice mountains
aurora_pen = turtle.Turtle()      # Liquid flowing Northern Lights ribbons
constellation_pen = turtle.Turtle()# Shimmering starlight heart constellation
text_pen = turtle.Turtle()        # Typography banner overlay

all_pens = [bg_pen, mountain_pen, aurora_pen, constellation_pen, text_pen]
for pen in all_pens:
    pen.hideturtle()
    pen.speed(0)

STARS = []
for _ in range(180):
    STARS.append({
        "x": random.uniform(-490, 490),
        "y": random.uniform(-200, 410),
        "size": random.uniform(0.6, 2.2),
        "brightness": random.uniform(0.3, 1.0),
        "color": random.choice(["#ffffff", "#a7f3d0", "#bae6fd", "#fbcfe8", "#fef08a"])
    })

METEORS = []
def spawn_meteor():
    return {
        "x": random.uniform(-300, 450),
        "y": random.uniform(150, 380),
        "dx": random.uniform(-6, -3),
        "dy": random.uniform(-4, -2),
        "length": random.uniform(30, 70),
        "life": 1.0,
        "decay": random.uniform(0.02, 0.04)
    }

for _ in range(3):
    METEORS.append(spawn_meteor())

NUM_CONSTELLATION_STARS = 42
HEART_NODES = []

for i in range(NUM_CONSTELLATION_STARS):
    t = (i / NUM_CONSTELLATION_STARS) * 2 * math.pi
    scale = 13.0
    # Parametric heart coordinate
    hx = scale * (16 * (math.sin(t) ** 3))
    hy = scale * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)) + 90
    HEART_NODES.append({
        "x": hx,
        "y": hy,
        "base_x": hx,
        "base_y": hy,
        "pulse_offset": random.uniform(0, math.pi * 2)
    })

def draw_mountains():
    mountain_pen.clear()
    
    # Far mountain range
    mountain_pen.penup()
    mountain_pen.goto(-500, -420)
    mountain_pen.color("#0a0f24")
    mountain_pen.begin_fill()
    
    mountain_peaks = [
        (-500, -180), (-380, -110), (-260, -190), (-140, -120), 
        (0, -210), (120, -100), (250, -180), (380, -130), (500, -220), (500, -420)
    ]
    for x, y in mountain_peaks:
        mountain_pen.goto(x, y)
    mountain_pen.end_fill()

    # Foreground dark ridge
    mountain_pen.penup()
    mountain_pen.goto(-500, -420)
    mountain_pen.color("#050714")
    mountain_pen.begin_fill()
    
    fore_peaks = [
        (-500, -260), (-320, -190), (-180, -270), (-30, -180), 
        (110, -250), (280, -170), (420, -240), (500, -200), (500, -420)
    ]
    for x, y in fore_peaks:
        mountain_pen.goto(x, y)
    mountain_pen.end_fill()

draw_mountains()

def render_sky(frame):
    bg_pen.clear()
    
    # 1. Draw twinkling ambient stars
    for idx, star in enumerate(STARS):
        twinkle = (math.sin(frame * 0.08 + idx * 0.5) + 1) / 2
        sz = star["size"] * (0.6 + 0.4 * twinkle)
        bg_pen.penup()
        bg_pen.goto(star["x"], star["y"])
        bg_pen.color(star["color"])
        bg_pen.dot(sz)

    # 2. Update and draw shooting meteors
    for m in METEORS:
        if m["life"] > 0:
            bg_pen.penup()
            bg_pen.goto(m["x"], m["y"])
            bg_pen.pendown()
            
            # Tail glow
            tail_x = m["x"] - m["dx"] * (m["length"] / 10)
            tail_y = m["y"] - m["dy"] * (m["length"] / 10)
            
            bg_pen.pensize(2)
            bg_pen.color("#ffffff")
            bg_pen.goto(tail_x, tail_y)
            
            # Move meteor forward
            m["x"] += m["dx"]
            m["y"] += m["dy"]
            m["life"] -= m["decay"]
        else:
            # Respawn meteor
            if random.random() < 0.03:
                m.update(spawn_meteor())

AURORA_PALETTE = ["#10b981", "#06b6d4", "#8b5cf6", "#ec4899", "#34d399"]

def render_aurora(elapsed):
    aurora_pen.clear()
    
    # Draw multiple wavy aurora ribbon bands across the heart canopy
    num_ribbons = 5
    for band in range(num_ribbons):
        color = AURORA_PALETTE[band % len(AURORA_PALETTE)]
        aurora_pen.color(color)
        aurora_pen.pensize(4 + band * 2)
        
        y_center = 90 + (band - 2) * 22
        
        aurora_pen.penup()
        first_point = True
        
        # Calculate sine wave along the parametric heart outline
        for i in range(70):
            t = (i / 70) * 2 * math.pi
            scale = 13.0 + 1.2 * math.sin(elapsed * 1.5 + band)
            
            # Parametric base heart coordinates
            base_x = scale * (16 * (math.sin(t) ** 3))
            base_y = scale * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)) + y_center - 20
            
            # Harmonic sine wave distortion for liquid Northern Lights flow
            wave1 = 14 * math.sin(elapsed * 2.2 + base_x * 0.02 + band)
            wave2 = 8 * math.cos(elapsed * 3.1 + base_y * 0.03 + band * 0.5)
            
            ax = base_x + wave1
            ay = base_y + wave2
            
            if first_point:
                aurora_pen.goto(ax, ay)
                aurora_pen.pendown()
                first_point = False
            else:
                aurora_pen.goto(ax, ay)

def render_constellation(elapsed):
    constellation_pen.clear()
    
    # Double heartbeat pulse calculation ("Lub-Dub" rhythm)
    heartbeat = 1.0 + 0.04 * math.sin(elapsed * 3.8) + 0.02 * math.sin(elapsed * 7.6)
    
    # Updated heart nodes positions based on pulse
    current_coords = []
    for node in HEART_NODES:
        nx = node["base_x"] * heartbeat
        ny = (node["base_y"] - 90) * heartbeat + 90
        
        # Add subtle shimmering floating motion
        nx += 1.8 * math.sin(elapsed * 2.0 + node["pulse_offset"])
        ny += 1.8 * math.cos(elapsed * 2.5 + node["pulse_offset"])
        
        current_coords.append((nx, ny))

    # 1. Connect constellation stars with shimmering light beams
    constellation_pen.pensize(1.5)
    for idx in range(len(current_coords)):
        next_idx = (idx + 1) % len(current_coords)
        x1, y1 = current_coords[idx]
        x2, y2 = current_coords[next_idx]
        
        # Color shifting along starlight webs
        beam_color = "#38bdf8" if idx % 2 == 0 else "#f472b6"
        constellation_pen.color(beam_color)
        
        constellation_pen.penup()
        constellation_pen.goto(x1, y1)
        constellation_pen.pendown()
        constellation_pen.goto(x2, y2)

    # 2. Draw glowing constellation star nodes
    for idx, (cx, cy) in enumerate(current_coords):
        glow_size = 5.0 + 2.5 * math.sin(elapsed * 4.0 + idx)
        node_color = "#ffffff" if idx % 3 == 0 else ("#f0abfc" if idx % 3 == 1 else "#7dd3fc")
        
        constellation_pen.penup()
        constellation_pen.goto(cx, cy)
        constellation_pen.color(node_color)
        constellation_pen.dot(glow_size)

text_pen.penup()
text_pen.goto(0, -320)
text_pen.color("#38bdf8")
text_pen.write("🌌 AURORA BOREALIS CELESTIAL HEART 🌌", align="center", font=("Courier", 15, "bold"))

text_pen.goto(0, -355)
text_pen.color("#f472b6")
text_pen.write("Arctic Northern Lights • Shimmering Constellation • Shooting Meteors", align="center", font=("Georgia", 11, "italic"))

frame = 0
try:
    while True:
        frame += 1
        elapsed = frame * 0.03
        
        # 1. Render cosmic sky & meteors
        render_sky(frame)
        
        # 2. Render flowing liquid Aurora Borealis waves
        render_aurora(elapsed)
        
        # 3. Render heart constellation lines and star nodes
        render_constellation(elapsed)
        
        # Update canvas buffer
        screen.update()
        time.sleep(0.016)  # Maintain smooth ~60 FPS

except turtle.TerminatorError:
    pass