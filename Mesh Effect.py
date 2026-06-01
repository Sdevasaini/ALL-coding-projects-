import turtle
import colorsys
import math
import sys

screen = turtle.Screen()
screen.setup(width=950, height=950)
screen.bgcolor("#040008")
screen.title("Quantum Love")

# Turn off automatic updates to implement manual double-buffered 60 FPS frame updates
turtle.tracer(3)

# Main vector pen for drawing the 3D heart cords
t = turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()

# Secondary telemetry pen to draw high-tech instrument panels
hud = turtle.Turtle()
hud.speed(0)
hud.hideturtle()
hud.penup()

is_paused = False
heart_beat_speed = 3.0    # Speed factor of coordinate expansion/contraction
num_rings = 18            # Structural heart layers tracing depth (lattice density)
twist_factor = 1.2        # Dynamic rotational twisting factor across the tunnel
manifold_mode = 0         # 0: Quantum Tunnel, 1: Möbius Ring, 2: Vortex Storm, 3: Waveform
palette_idx = 0           # Active color gradient theme
camera_distance = 420.0   # Focal camera lens perspective scale
master_time = 0.0         # Absolute clock tracking rotation and pulse phases

# Rotational vectors tracking angular momentum across 3D planes
rot_x = 0.0
rot_y = 0.0
rot_z = 0.0

def get_holographic_love_color(palette_index, z_depth, cycle_shift):
    """
    Computes precise RGB color vectors using dynamic depth attenuation.
    Coordinates close to the viewport (high Z) glow brighter; deep coordinates fade.
    """
    # Normalize z_depth from -160 to 160 range onto 0.0 -> 1.0 interval
    depth_ratio = (z_depth + 160.0) / 320.0
    depth_ratio = max(0.15, min(1.0, depth_ratio))

    if palette_index == 0:
        # Valentine Neon (Hot Pink -> Magenta -> Incandescent Ruby Red)
        h = (0.92 + depth_ratio * 0.14 - cycle_shift * 0.05) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.95, 1.0)
    elif palette_index == 1:
        # Rose Quartz Aurora (Soft Pastel Pink -> Peach Cream -> Mystic Aqua Blue)
        h = (0.86 + depth_ratio * 0.22 + cycle_shift * 0.03) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.65, 1.0)
    elif palette_index == 2:
        # Cyber Cupid (Laser Scarlet -> Royal Purple -> Cyber Cyan)
        h = (0.98 + depth_ratio * 0.30 + cycle_shift * 0.08) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.90, 1.0)
    else:
        # Amethyst Glow (Deep Amethyst Purple -> Velvet Lavender -> Solar Violet)
        h = (0.76 + depth_ratio * 0.18 - cycle_shift * 0.04) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)

    # Apply 3D volumetric depth shading (gradual falloff to black in distance)
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

# Configure listeners
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
    """Generates detailed 3D coordinate mathematics telemetry across workspace boundaries."""
    hud.clear()
    
    # Header Title
    hud.color("#ff0a54")
    hud.goto(-440, 410)
    hud.write("QUANTUM LOVE RESONANCE ENGINE", font=("Consolas", 15, "bold"))
    
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

    # Guide Instructions
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
    """
    Evaluates 3D spatial coordinate vectors on a mathematically perfect heart.
    Utilizes classic algebraic cardioid parametrics and applies custom warp matrices.
    """
    # Base parametric heart curve in a 2D plane (scaled and centered)
    # x = 16 * sin^3(t)
    # y = 13 * cos(t) - 5 * cos(2t) - 2 * cos(3t) - cos(4t)
    x_raw = 16.0 * (math.sin(theta) ** 3)
    y_raw = 13.0 * math.cos(theta) - 5.0 * math.cos(2 * theta) - 2.0 * math.cos(3 * theta) - math.cos(4 * theta)
    
    # Re-align center of gravity of heart coordinate to preserve origin rotations
    y_raw += 1.5
    
    # Scale raw coordinates onto standardized unit sizes (~1.0 factor)
    x_norm = x_raw * 0.062
    y_norm = y_raw * 0.062

    # Compute different 3D layouts based on active engine mode
    if manifold_mode == 0:
        # Quantum Beat Tunnel: Nested depth layers with breathing heartbeat pulse
        ratio = ring_idx / num_rings
        pulse = 1.0 + 0.16 * math.sin(time_step * 0.15)
        
        # Scaling scales up exponentially toward screen limits
        scale = (20.0 + ratio * 240.0) * pulse
        z = (ratio - 0.5) * 320.0
        
        # Twist individual layers along their axis to weave a double-helix tunnel
        twist = ratio * twist_factor * 1.6
        cos_t, sin_t = math.cos(twist), math.sin(twist)
        
        x = (x_norm * cos_t - y_norm * sin_t) * scale
        y = (x_norm * sin_t + y_norm * cos_t) * scale
        z_out = z
        
    elif manifold_mode == 1:
        # Double Heart Möbius Ring: Weaving hearts around a major spatial orbital circle
        major_radius = 145.0
        orbital_angle = (ring_idx / num_rings) * 2.0 * math.pi
        
        # Spin individual heart nodes around their local axes
        local_spin = orbital_angle * twist_factor + time_step * 0.02
        cos_s, sin_s = math.cos(local_spin), math.sin(local_spin)
        
        # Local heart shape scale
        local_scale = 55.0 * (1.0 + 0.15 * math.sin(time_step * 0.1 + orbital_angle * 2.0))
        
        lx = (x_norm * cos_s - y_norm * sin_s) * local_scale
        ly = (x_norm * sin_s + y_norm * cos_s) * local_scale
        
        # Map localized 2D heart vectors onto the 3D rotating toroidal perimeter
        x = (major_radius + lx) * math.cos(orbital_angle)
        y = (major_radius + lx) * math.sin(orbital_angle)
        z_out = ly
        
    elif manifold_mode == 2:
        # Hyper-Cardioid Vortex: Multi-sized hearts swarming around gravitational singularity
        ratio = ring_idx / num_rings
        orbit_angle = ratio * 2.0 * math.pi * 3.0 + time_step * 0.04
        distance = 45.0 + ratio * 210.0
        
        # Heart sizing based on radial distance
        h_scale = 12.0 + ratio * 45.0
        
        # Orbital distortion waves
        wave = 35.0 * math.sin(time_step * 0.08 + ratio * math.pi)
        
        x = distance * math.cos(orbit_angle) + x_norm * h_scale
        y = distance * math.sin(orbit_angle) + y_norm * h_scale
        z_out = wave + (ratio - 0.5) * 160.0
        
    else:
        # Infinite Love Waveform: Transverse wave pulsing along the X axis
        ratio = ring_idx / num_rings
        wave_phase = ratio * 2.0 * math.pi * 1.8 - time_step * 0.08
        
        # Breathe the scale of the hearts sequentially down the wave path
        h_scale = 44.0 * (1.1 + 0.3 * math.sin(wave_phase))
        
        x = (ratio - 0.5) * 520.0
        y = 130.0 * math.sin(wave_phase) + y_norm * h_scale
        z_out = x_norm * h_scale

    return x, y, z_out

def rotate_and_project_3d(x, y, z, ax, ay, az):
    """
    Applies Pitch, Yaw, and Roll Euler rotation matrices to 3D coordinates.
    Then projects the resulting points onto a 2D viewport using depth-focal scaling.
    """
    # 1. Yaw Rotation (around Y axis)
    cos_y, sin_y = math.cos(ay), math.sin(ay)
    x1 = x * cos_y - z * sin_y
    z1 = x * sin_y + z * cos_y

    # 2. Pitch Rotation (around X axis)
    cos_x, sin_x = math.cos(ax), math.sin(ax)
    y2 = y * cos_x - z1 * sin_x
    z2 = y * sin_x + z1 * cos_x

    # 3. Roll Rotation (around Z axis)
    cos_z, sin_z = math.cos(az), math.sin(az)
    x3 = x1 * cos_z - y2 * sin_z
    y3 = x1 * sin_z + y2 * cos_z

    # Perspective projection mapping (prevent division-by-zero with coordinate clipping)
    clip_plane = 320.0
    perspective_factor = camera_distance / (z2 + clip_plane)
    
    screen_x = x3 * perspective_factor
    screen_y = y3 * perspective_factor

    return screen_x, screen_y, z2

def draw_loop():
    """Main rendering loop executing continuous vector projection redraws."""
    global rot_x, rot_y, rot_z, master_time
    
    if is_paused:
        return

    t.clear()
    draw_hud()

    # Progress angular velocities to animate yaw, pitch, and roll
    rot_x += 0.009
    rot_y += 0.013
    rot_z += 0.007

    # Number of coordinate subdivisions to represent a single continuous loop path
    trail_resolution = 36

    # Iterate through all configured nested heart rings (cords)
    for ring_idx in range(num_rings):
        t.penup()
        
        last_screen_coord = None
        
        # Generate the parametric loop (0 to 2*pi)
        for i in range(trail_resolution + 1):
            theta = (i * 2.0 * math.pi) / trail_resolution
            
            # 1. Calculate raw 3D position
            rx, ry, rz = calculate_3d_heart_point(theta, ring_idx, master_time)
            
            # 2. Project coordinates into 2D camera viewport
            sx, sy, depth_z = rotate_and_project_3d(rx, ry, rz, rot_x, rot_y, rot_z)
            
            # 3. Handle drawing vectors
            if i > 0 and last_screen_coord is not None:
                lx, ly, ldepth = last_screen_coord
                
                # Check for canvas wrapping limits
                if abs(sx) < 460 and abs(sy) < 460 and abs(lx) < 460 and abs(ly) < 460:
                    # Dynamically compute gradient values linked to coordinate depth
                    r, g, b = get_holographic_love_color(palette_idx, depth_z, master_time * 0.02)
                    t.pencolor(r, g, b)
                    
                    # Thicken paths closer to viewport (creates structural depth)
                    normalized_depth = (depth_z + 160.0) / 320.0
                    thickness = max(1, int(normalized_depth * 4.5))
                    t.width(thickness)
                    
                    # Connect points
                    t.goto(lx, ly)
                    t.pendown()
                    t.goto(sx, sy)
                    t.penup()
            
            last_screen_coord = (sx, sy, depth_z)

    # Push buffer directly to Turtle graphics canvas
    turtle.update()

    # Time step advancement linked to speed mechanics
    master_time += heart_beat_speed

    # Re-queue next frame targetting roughly 60 FPS
    screen.ontimer(draw_loop, 16)

# Start the interactive volumetric simulation
draw_loop()
screen.mainloop()
