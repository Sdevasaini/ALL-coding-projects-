import turtle
import colorsys
import math
import sys

screen = turtle.Screen()
screen.setup(width=950, height=950)
screen.bgcolor("#040008")
screen.title("Quantum Love")
turtle.tracer(3)
t = turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()
hud = turtle.Turtle()
hud.speed(0)
hud.hideturtle()
hud.penup()

is_paused = False
heart_beat_speed = 3.0 
num_rings = 18 
twist_factor = 1.2 
manifold_mode = 0 
palette_idx = 0 
camera_distance = 420.0 
master_time = 0.0 
rot_x = 0.0
rot_y = 0.0
rot_z = 0.0

def get_holographic_love_color(palette_index, z_depth, cycle_shift):
    depth_ratio = (z_depth + 160.0) / 320.0
    depth_ratio = max(0.15, min(1.0, depth_ratio))

    if palette_index == 0:
        h = (0.92 + depth_ratio * 0.14 - cycle_shift * 0.05) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.95, 1.0)
    elif palette_index == 1:
        h = (0.86 + depth_ratio * 0.22 + cycle_shift * 0.03) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.65, 1.0)
    elif palette_index == 2:
        h = (0.98 + depth_ratio * 0.30 + cycle_shift * 0.08) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.90, 1.0)
    else: 
        h = (0.76 + depth_ratio * 0.18 - cycle_shift * 0.04) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0) 
        
    intensity = min(1.0, depth_ratio * 1.35) 
    return r * intensity, g * intensity, b * intensity

def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if not is_paused:
        draw_loop()

def inc_speed():
    global heart_beat_speed
    heart_beat_speed = min(10.0, heart_beat_speed + 0.2)

def dec_speed():
    global heart_beat_speed
    heart_beat_speed = max(0.2, heart_beat_speed - 0.2)

def inc_rings():
    global num_rings
    num_rings = min(35, num_rings + 1)

def dec_rings():
    global num_rings
    num_rings = max(5, num_rings - 1)

def inc_twist():
    global twist_factor
    twist_factor = min(4.0, twist_factor + 0.1)

def dec_twist():
    global twist_factor
    twist_factor = max(0.0, twist_factor - 0.1)

def cycle_manifold():
    global manifold_mode
    manifold_mode = (manifold_mode + 1) % 4

def cycle_palette():
    global palette_idx
    palette_idx = (palette_idx + 1) % 4

def exit_program():
    turtle.bye()
    sys.exit()
screen.listen()
screen.onkey(toggle_pause, "space")
screen.onkey(inc_speed, "Up")
screen.onkey(dec_speed, "Down")
screen.onkey(inc_rings, "Right")
screen.onkey(dec_rings, "Left")
screen.onkey(inc_twist, "w")
screen.onkey(dec_twist, "s")
screen.onkey(cycle_manifold, "m")
screen.onkey(cycle_palette, "c")
screen.onkey(exit_program, "Escape")

def draw_hud():
    hud.clear()
    hud.color("#ff0a54")
    hud.goto(-440, 410)
    hud.write("QUANTUM LOVE", font=("Consolas", 15, "bold"))
    
    modes = [
        "Quantum Beat Tunnel (Concentric Depth Singularity)",
        "Double Heart Möbius Ring (Torus Knot Alignment)",
        "Hyper-Cardioid Vortex (Rotational Gravity Fields)",
        "Infinite Love Waveform (Transverse Spatial Propagation)"
    ]
    palettes = ["Valentine Neon", "Rose Quartz Aurora", "Cyber Cupid", "Amethyst Glow"]
    
    telemetry = (
        f"3D Geometry:      {modes[manifold_mode]}\n"
        f"Lattice Density:  {num_rings} Heart Strands\n"
        f"Resonance Pace:   {heart_beat_speed:.1f} Hz\n"
        f"Warp Twist Force: {twist_factor:.2f}\n"
        f"Aura Palette:     {palettes[palette_idx]}\n"
        f"3D Euler Planes:  Pitch:{math.degrees(rot_x):.1f}° | Yaw:{math.degrees(rot_y):.1f}° | Roll:{math.degrees(rot_z):.1f}°"
    )
    
    hud.color("#f72585")
    hud.goto(-440, 275)
    hud.write(telemetry, font=("Consolas", 10, "normal"))
    guide = (
        "Projector Engine Control Deck:\n"
        " [Up / Down Arrows]   - Accelerate / Decelerate Cosmic Heartbeat Speed\n"
        " [Left / Right Arrows] - Increase / Decrease Structural Heart Mesh Layers\n"
        " [W / S Keys]         - Increase / Decrease Spiral Twist Amplitude\n"
        " [M] Key              - Cycle Through Dimensional Projection Models\n"
        " [C] Key              - Shift Chromatic Depth Auric Profiles\n"
        " [Spacebar]           - Halt Quantum Equations  |  [Escape] - Core Shutdown"
    )
    hud.goto(-440, -425)
    hud.write(guide, font=("Consolas", 9, "italic"))

def calculate_3d_heart_point(theta, ring_idx, time_step):

    x_raw = 16.0 * (math.sin(theta) ** 3)
    y_raw = 13.0 * math.cos(theta) - 5.0 * math.cos(2 * theta) - 2.0 * math.cos(3 * theta) - math.cos(4 * theta)
    y_raw += 1.5
    x_norm = x_raw * 0.062
    y_norm = y_raw * 0.062

    if manifold_mode == 0:
        ratio = ring_idx / num_rings
        pulse = 1.0 + 0.16 * math.sin(time_step * 0.15)
        scale = (20.0 + ratio * 240.0) * pulse
        z = (ratio - 0.5) * 320.0
        twist = ratio * twist_factor * 1.6
        cos_t, sin_t = math.cos(twist), math.sin(twist)
        x = (x_norm * cos_t - y_norm * sin_t) * scale
        y = (x_norm * sin_t + y_norm * cos_t) * scale
        z_out = z
        
    elif manifold_mode == 1:
        major_radius = 145.0
        orbital_angle = (ring_idx / num_rings) * 2.0 * math.pi
        local_spin = orbital_angle * twist_factor + time_step * 0.02
        cos_s, sin_s = math.cos(local_spin), math.sin(local_spin)
        local_scale = 55.0 * (1.0 + 0.15 * math.sin(time_step * 0.1 + orbital_angle * 2.0))
        lx = (x_norm * cos_s - y_norm * sin_s) * local_scale
        ly = (x_norm * sin_s + y_norm * cos_s) * local_scale
        x = (major_radius + lx) * math.cos(orbital_angle)
        y = (major_radius + lx) * math.sin(orbital_angle)
        z_out = ly
        
    elif manifold_mode == 2:
        ratio = ring_idx / num_rings
        orbit_angle = ratio * 2.0 * math.pi * 3.0 + time_step * 0.04
        distance = 45.0 + ratio * 210.0
        h_scale = 12.0 + ratio * 45.0
        wave = 35.0 * math.sin(time_step * 0.08 + ratio * math.pi)
        x = distance * math.cos(orbit_angle) + x_norm * h_scale
        y = distance * math.sin(orbit_angle) + y_norm * h_scale
        z_out = wave + (ratio - 0.5) * 160.0
        
    else:
       
        ratio = ring_idx / num_rings
        wave_phase = ratio * 2.0 * math.pi * 1.8 - time_step * 0.08
        h_scale = 44.0 * (1.1 + 0.3 * math.sin(wave_phase))
        x = (ratio - 0.5) * 520.0
        y = 130.0 * math.sin(wave_phase) + y_norm * h_scale
        z_out = x_norm * h_scale

    return x, y, z_out

def rotate_and_project_3d(x, y, z, ax, ay, az):
    cos_y, sin_y = math.cos(ay), math.sin(ay)
    x1 = x * cos_y - z * sin_y
    z1 = x * sin_y + z * cos_y
    cos_x, sin_x = math.cos(ax), math.sin(ax)
    y2 = y * cos_x - z1 * sin_x
    z2 = y * sin_x + z1 * cos_x
    cos_z, sin_z = math.cos(az), math.sin(az)
    x3 = x1 * cos_z - y2 * sin_z
    y3 = x1 * sin_z + y2 * cos_z
    clip_plane = 320.0
    perspective_factor = camera_distance / (z2 + clip_plane)
    screen_x = x3 * perspective_factor
    screen_y = y3 * perspective_factor

    return screen_x, screen_y, z2

def draw_loop():

    global rot_x, rot_y, rot_z, master_time
    
    if is_paused:
        return

    t.clear()
    draw_hud()

    rot_x += 0.009
    rot_y += 0.013
    rot_z += 0.007
    trail_resolution = 36

    for ring_idx in range(num_rings):
        t.penup()
        
        last_screen_coord = None
        for i in range(trail_resolution + 1):
            theta = (i * 2.0 * math.pi) / trail_resolution
            rx, ry, rz = calculate_3d_heart_point(theta, ring_idx, master_time)
            sx, sy, depth_z = rotate_and_project_3d(rx, ry, rz, rot_x, rot_y, rot_z)
            if i > 0 and last_screen_coord is not None:
                lx, ly, ldepth = last_screen_coord
                
                if abs(sx) < 460 and abs(sy) < 460 and abs(lx) < 460 and abs(ly) < 460:
                    r, g, b = get_holographic_love_color(palette_idx, depth_z, master_time * 0.02)
                    t.pencolor(r, g, b)
                    normalized_depth = (depth_z + 160.0) / 320.0
                    thickness = max(1, int(normalized_depth * 4.5))
                    t.width(thickness)
                    t.goto(lx, ly)
                    t.pendown()
                    t.goto(sx, sy)
                    t.penup()
            
            last_screen_coord = (sx, sy, depth_z)
    turtle.update()
    master_time += heart_beat_speed
    screen.ontimer(draw_loop, 16)
draw_loop()
screen.mainloop()