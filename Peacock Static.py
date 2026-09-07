import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(width=1000, height=750)
screen.bgcolor("#020108")
screen.title("Peacock Static")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

def get_hsv_color(h, s=0.9, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(
        h % 1.0,
        max(0.0, min(1.0, s)),
        max(0.0, min(1.0, v))
    )
    return (r, g, b)

def draw_ocellus_eye(x, y, scale, hue_base):
    pen.goto(x, y - 12 * scale)
    pen.dot(int(26 * scale),
            get_hsv_color(hue_base + 0.1, 0.85, 0.5))
    pen.dot(int(20 * scale),
            get_hsv_color(0.12, 0.95, 0.95))
    pen.dot(int(14 * scale),
            get_hsv_color(0.48, 0.9, 0.9))
    pen.dot(int(8 * scale),
            get_hsv_color(0.68, 0.95, 1.0))
    pen.dot(int(3 * scale),
            get_hsv_color(0.15, 0.2, 1.0))
      
def draw_feather_plume(cx, cy, angle_rad, length, bend, hue, tier):
    steps = 14
    dx = math.cos(angle_rad)
    dy = math.sin(angle_rad)
    perp_x = -dy
    perp_y = dx
    shaft_pts = []
    pen.goto(cx, cy)
    pen.pendown()

    for i in range(steps + 1):
        frac = i / steps
        curve_off = math.sin(frac * math.pi) * bend
        px = cx + dx * length * frac + perp_x * curve_off
        py = cy + dy * length * frac + perp_y * curve_off
        pen.pencolor(
            get_hsv_color(
                hue + frac * 0.1,
                0.8,
                0.7 + frac * 0.3
            )
        )

        pen.width(max(1, int(3 * (1.0 - frac * 0.5))))
        pen.goto(px, py)
        shaft_pts.append((px, py))

    pen.penup()
    for b in range(2, steps - 1, 2):
        bx, by = shaft_pts[b]
        b_frac = b / steps
        barb_len = (
            1.0 - abs(b_frac - 0.6) * 1.5
        ) * 18.0 * (length / 180.0)

        for side in (-1, 1):
            barb_ang = angle_rad + 0.6 * side
            ex = bx + math.cos(barb_ang) * barb_len
            ey = by + math.sin(barb_ang) * barb_len
            pen.goto(bx, by)
            pen.pendown()
            pen.pencolor(
                get_hsv_color(
                    hue + b_frac * 0.15,
                    0.85,
                    0.85
                )
            )

            pen.width(1)
            pen.goto(ex, ey)
            pen.penup()

    tip_x, tip_y = shaft_pts[-1]
    eye_scale = (
        0.7 + tier * 0.25
    ) * (length / 200.0)
    draw_ocellus_eye(
        tip_x,
        tip_y,
        eye_scale,
        hue
    )

def draw_peacock_canopy(cx, cy):
    tiers = [
        {
            "count": 13,
            "length": 250,
            "hue": 0.45,
            "lift": -40
        },
        {
            "count": 11,
            "length": 190,
            "hue": 0.52,
            "lift": -35
        },
        {
            "count": 9,
            "length": 130,
            "hue": 0.60,
            "lift": -30
        }
    ]

    for tier_index, tier in enumerate(tiers):
        count = tier["count"]
        start_angle = math.radians(-25)
        end_angle = math.radians(205)

        for i in range(count):
            frac = i / (count - 1)
            angle = (
                start_angle
                + (end_angle - start_angle) * frac
            )

            bend = (
                math.sin(frac * math.pi * 2) * 12
                + (frac - 0.5) * 35
            )

            draw_feather_plume(
                cx,
                cy + tier["lift"],
                angle,
                tier["length"],
                bend,
                tier["hue"] + frac * 0.1,
                tier_index
            )

def draw_peacock_body(cx, cy):

    body_x = cx
    body_y = cy - 100
    pen.goto(body_x, body_y)
    pen.pencolor(
        get_hsv_color(0.62, 0.95, 0.8)
    )

    pen.dot(65)
    neck_pts = []
    neck_steps = 10
    for i in range(neck_steps + 1):
        n_frac = i / neck_steps
        nx = (
            body_x
            + math.sin(n_frac * math.pi) * 15
        )

        ny = body_y + n_frac * 85
        neck_pts.append((nx, ny))
        pen.goto(nx, ny)
        pen.pencolor(
            get_hsv_color(
                0.58 - n_frac * 0.1,
                0.95,
                0.85 + n_frac * 0.15
            )
        )

        pen.dot(
            int(28 * (1.0 - n_frac * 0.45))
        )

    head_x, head_y = neck_pts[-1]
    pen.goto(head_x, head_y)
    pen.pencolor(
        get_hsv_color(0.52, 0.95, 1.0)
    )

    pen.dot(18)
    pen.goto(head_x + 3, head_y + 2)
    pen.pencolor(
        get_hsv_color(0.12, 0.2, 1.0)
    )

    pen.dot(5)
    pen.pencolor("#000000")
    pen.dot(2)
    pen.goto(head_x + 7, head_y - 1)
    pen.pendown()
    pen.pencolor(
        get_hsv_color(0.12, 0.8, 0.95)
    )

    pen.width(3)
    pen.goto(head_x + 18, head_y - 5)
    pen.penup()

    for c in range(5):
        c_frac = (c - 2) / 2.0
        c_angle = math.radians(
            90 + c_frac * 28
        )

        c_len = 28 - abs(c_frac) * 4
        cx_tip = (
            head_x
            + math.cos(c_angle) * c_len
        )

        cy_tip = (
            head_y
            + math.sin(c_angle) * c_len
        )

        pen.goto(head_x, head_y + 6)
        pen.pendown()
        pen.pencolor(
            get_hsv_color(0.48, 0.9, 1.0)
        )

        pen.width(1)
        pen.goto(cx_tip, cy_tip)
        pen.penup()
        pen.goto(cx_tip, cy_tip)
        pen.pencolor(
            get_hsv_color(0.14, 0.95, 1.0)
        )

        pen.dot(6)

def main():
    draw_peacock_canopy(0, -60)
    draw_peacock_body(0, -60)
    screen.update()
    screen.mainloop()
if __name__ == "__main__":
    main()