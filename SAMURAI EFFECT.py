import turtle
import math
import colorsys
import time
import random

screen = turtle.Screen()
screen.setup(width=1100, height=850)
screen.bgcolor("#02010a")
screen.title("SAMURAI EFFECT")
screen.tracer(4)
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
tip = turtle.Turtle()
tip.shape("circle")
tip.shapesize(0.5, 0.5)
tip.color("#ffffff")
tip.penup()
hud = turtle.Turtle()
hud.hideturtle()
hud.penup()

hue_offset = 0.0
draw_delay = 0.005
is_paused = False
draw_speed_multiplier = 1
total_lines_drawn = 0
should_reset = False

def get_neon_color(hue, sat=1.0, val=1.0):
    rgb = colorsys.hsv_to_rgb(hue % 1.0, sat, val)
    return f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"

def render_hud(progress_percent, phase_name):
    hud.clear()
    hud.goto(0, 370)
    hud.pencolor("#00ffcc")
    hud.write("", align="center", font=("Courier", 15, "bold"))
    hud.goto(0, -370)
    hud.pencolor("#ff007f")
    hud.write(f": {phase_name} | : {progress_percent}% | : {total_lines_drawn}", 
              align="center", font=("Courier", 10, "bold"))
    hud.goto(0, -395)
    hud.pencolor("#ffffff")
    hud.write("", 
              align="center", font=("Courier", 9, "normal"))

def toggle_pause():
    global is_paused
    is_paused = not is_paused

def speed_up():
    global draw_speed_multiplier
    draw_speed_multiplier = min(10, draw_speed_multiplier + 1)

def speed_down():
    global draw_speed_multiplier
    draw_speed_multiplier = max(1, draw_speed_multiplier - 1)

def request_reset():
    global should_reset
    should_reset = True

screen.listen()
screen.onkey(toggle_pause, "space")
screen.onkey(speed_up, "Up")
screen.onkey(speed_down, "Down")
screen.onkey(request_reset, "r")
screen.onkey(request_reset, "R")

def draw_line_slowly(x1, y1, x2, y2, color, thickness=2, dot_size=0):
    global total_lines_drawn
    
    if is_paused:
        while is_paused:
            screen.update()
            time.sleep(0.05)
            
    drawer.pensize(thickness)
    drawer.pencolor(color)
    drawer.penup()
    drawer.goto(x1, y1)
    drawer.pendown()
    drawer.goto(x2, y2)
    
    if dot_size > 0:
        drawer.dot(dot_size, color)
        
    tip.goto(x2, y2)
    tip.color(color)
    total_lines_drawn += 1
    if total_lines_drawn % draw_speed_multiplier == 0:
        screen.update()
        if draw_delay > 0:
            time.sleep(draw_delay)

def draw_horns_and_crest(hue_base):
    render_hud(0, "")
    horn_sides = [-1, 1]
    steps = 22
    for side in horn_sides:
        if should_reset: return
        prev_x, prev_y = side * 50, 130
        for s in range(1, steps + 1):
            if should_reset: return
            t = s / steps
            x = side * (50 + t * 140 + math.sin(t * math.pi) * 35)
            y = 130 + t * 190 - math.pow(t, 2) * 40
            hue = hue_base + 0.03 * s + (0.05 if side > 0 else 0)
            color = get_neon_color(hue)
            draw_line_slowly(prev_x, prev_y, x, y, color, thickness=max(1, 4 - int(s / 6)), dot_size=4 if s == steps else 0)
            prev_x, prev_y = x, y
            
        for r in range(1, 9):
            if should_reset: return
            t1 = r / 10
            t2 = (r + 1) / 10
            x1 = side * (50 + t1 * 140 + math.sin(t1 * math.pi) * 35)
            y1 = 130 + t1 * 190 - math.pow(t1, 2) * 40
            x2 = side * (30 + t2 * 90)
            y2 = 120 + t2 * 120
            
            color = get_neon_color(hue_base + 0.1 + r * 0.02)
            draw_line_slowly(x1, y1, x2, y2, color, thickness=1, dot_size=3)
            
    crest_pts = []
    num_crest_rays = 12
    for i in range(num_crest_rays + 1):
        if should_reset: return
        a = (2 * math.pi / num_crest_rays) * i
        r = 35 + (18 if i % 2 == 0 else 0)
        cx = r * math.cos(a)
        cy = 160 + r * math.sin(a)
        hue = hue_base + 0.15 + i * 0.01
        color = get_neon_color(hue)
        
        if i == 0:
            prev_cx, prev_cy = cx, cy
        else:
            draw_line_slowly(prev_cx, prev_cy, cx, cy, color, thickness=2, dot_size=4 if i % 2 == 0 else 0)
            draw_line_slowly(0, 160, cx, cy, color, thickness=1)
            prev_cx, prev_cy = cx, cy

    render_hud(20, "")

def draw_cyber_visor_and_eyes(hue_base):
    render_hud(20, "")
    rim_pts = [(-160, 110), (-90, 130), (0, 140), (90, 130), (160, 110), 
               (140, 90), (0, 100), (-140, 90), (-160, 110)]
    
    for i in range(len(rim_pts) - 1):
        if should_reset: return
        p1, p2 = rim_pts[i], rim_pts[i+1]
        color = get_neon_color(hue_base + 0.25 + i * 0.02)
        draw_line_slowly(p1[0], p1[1], p2[0], p2[1], color, thickness=3)

    visor_outer = [(-130, 85), (-50, 45), (0, 40), (50, 45), (130, 85),
                   (110, 20), (0, 15), (-110, 20), (-130, 85)]
    
    for i in range(len(visor_outer) - 1):
        if should_reset: return
        p1, p2 = visor_outer[i], visor_outer[i+1]
        color = get_neon_color(hue_base + 0.3 + i * 0.02)
        draw_line_slowly(p1[0], p1[1], p2[0], p2[1], color, thickness=2)
        
    eye_centers = [(-50, 55), (50, 55)]
    for side_idx, (ex, ey) in enumerate(eye_centers):
        if should_reset: return
        
        hex_pts = []
        for h in range(7):
            ha = (math.pi / 3) * h
            hx = ex + 28 * math.cos(ha)
            hy = ey + 18 * math.sin(ha)
            hex_pts.append((hx, hy))
            
        for h in range(6):
            if should_reset: return
            color = get_neon_color(hue_base + 0.38 + h * 0.02)
            draw_line_slowly(hex_pts[h][0], hex_pts[h][1], hex_pts[h+1][0], hex_pts[h+1][1], color, thickness=2)
            draw_line_slowly(ex, ey, hex_pts[h][0], hex_pts[h][1], color, thickness=1, dot_size=3)
        draw_line_slowly(ex - 40, ey, ex + 40, ey, "#ff0055", thickness=1)
        draw_line_slowly(ex, ey - 25, ex, ey + 25, "#ff0055", thickness=1, dot_size=5)
    render_hud(40, "")

def draw_oni_face_and_grill(hue_base):
    render_hud(40, "")
    
    jaw_contour = [(-110, 20), (-120, -40), (-80, -110), (0, -145), (80, -110), (120, -40), (110, 20)]
    for i in range(len(jaw_contour) - 1):
        if should_reset: return
        p1, p2 = jaw_contour[i], jaw_contour[i+1]
        color = get_neon_color(hue_base + 0.45 + i * 0.03)
        draw_line_slowly(p1[0], p1[1], p2[0], p2[1], color, thickness=3, dot_size=4)
    nose_pts = [(0, 40), (-22, 5), (0, -15), (22, 5), (0, 40)]
    for i in range(4):
        if should_reset: return
        p1, p2 = nose_pts[i], nose_pts[i+1]
        color = get_neon_color(hue_base + 0.5)
        draw_line_slowly(p1[0], p1[1], p2[0], p2[1], color, thickness=2)
  
    num_teeth = 10
    teeth_width = 120
    for t in range(num_teeth + 1):
        if should_reset: return
        x = -teeth_width / 2 + (teeth_width / num_teeth) * t
        y_top = -40 - math.pow(abs(x) / 70, 2) * 10
        y_bottom = -80 + math.pow(abs(x) / 70, 2) * 8
        color = get_neon_color(hue_base + 0.55 + t * 0.02)
        draw_line_slowly(x, y_top, x, y_bottom, color, thickness=2, dot_size=3)
        
    draw_line_slowly(-65, -40, 65, -40, "#ffffff", thickness=2)
    draw_line_slowly(-60, -80, 60, -80, "#ffffff", thickness=2)
    render_hud(60, "")

def draw_neck_armor_plates(hue_base):
    render_hud(60, "")
    
    num_tiers = 5
    for tier in range(num_tiers):
        if should_reset: return
        y_offset = -120 - tier * 25
        width = 170 + tier * 20
        arch = 30 + tier * 5
        hue = hue_base + 0.65 + tier * 0.04
        color = get_neon_color(hue)
        steps = 16
        for s in range(steps):
            if should_reset: return
            t1 = s / steps
            t2 = (s + 1) / steps
            x1 = -width / 2 + t1 * width
            y1 = y_offset - math.cos((t1 - 0.5) * math.pi) * arch
            x2 = -width / 2 + t2 * width
            y2 = y_offset - math.cos((t2 - 0.5) * math.pi) * arch
            draw_line_slowly(x1, y1, x2, y2, color, thickness=3)
            
            if s % 2 == 1 and tier < num_tiers - 1:
                next_y = (y_offset - 25) - math.cos((t1 - 0.5) * math.pi) * (arch + 5)
                draw_line_slowly(x1, y1, x1, next_y, "#00ffff", thickness=1, dot_size=3)

    render_hud(80, "")

def draw_celestial_halo_aura(hue_base):
    render_hud(80, "")
    
    num_rays = 32
    radius_inner = 180
    radius_outer = 320
    
    for r in range(num_rays):
        if should_reset: return
        angle = (2 * math.pi / num_rays) * r
        x1 = radius_inner * math.cos(angle)
        y1 = 20 + radius_inner * math.sin(angle) * 0.85
        x2 = radius_outer * math.cos(angle)
        y2 = 20 + radius_outer * math.sin(angle) * 0.85
        hue = hue_base + 0.85 + r * 0.015
        color = get_neon_color(hue)
        draw_line_slowly(x1, y1, x2, y2, color, thickness=1, dot_size=4 if r % 2 == 0 else 0)

    frame_pts = []
    for f in range(7):
        fa = (math.pi / 3) * f + math.pi / 6
        fx = 380 * math.cos(fa)
        fy = 20 + 380 * math.sin(fa)
        frame_pts.append((fx, fy))
        
    for f in range(6):
        if should_reset: return
        color = get_neon_color(hue_base + 0.95 + f * 0.02)
        draw_line_slowly(frame_pts[f][0], frame_pts[f][1], frame_pts[f+1][0], frame_pts[f+1][1], color, thickness=2, dot_size=6)

    render_hud(100, "")
    tip.goto(0, 0)
    screen.update()

def plot_sacred_samurai():
    global total_lines_drawn, hue_offset, should_reset
    
    drawer.clear()
    total_lines_drawn = 0
    hue_offset = random.random()
    draw_horns_and_crest(hue_offset)
    if should_reset: return
    draw_cyber_visor_and_eyes(hue_offset)
    if should_reset: return
    draw_oni_face_and_grill(hue_offset)
    if should_reset: return
    draw_neck_armor_plates(hue_offset)
    if should_reset: return
    draw_celestial_halo_aura(hue_offset)

def main():
    global should_reset
    
    while True:
        try:
            should_reset = False
            plot_sacred_samurai()
            hold_start = time.time()
            while time.time() - hold_start < 8.0 and not should_reset:
                screen.update()
                time.sleep(0.05)
                
        except turtle.TerminatedError:
            print("")
            break
        except Exception as e:
            print(f"Error in plotting loop: {e}")
            break

if __name__ == "__main__":
    main()