import sys
import numpy as np
import matplotlib
if "--save" in sys.argv:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation, PillowWriter

TEXT = "" 
FPS = 20
SAVE = "--save" in sys.argv
rng = np.random.default_rng(11)
T_OUTLINE = (0.6, 7.0)
T_FILL = (5.5, 11.5)
T_TEXT = (11.0, 13.5)
T_BEAT = 13.0 
TOTAL = 18.0

def ease(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)
def prog(t, span):
    return ease((t - span[0]) / (span[1] - span[0]))
def heart(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

_t = np.linspace(0, 2 * np.pi, 60)
_hx, _hy = heart(_t)
HEART_MARKER = Path(np.column_stack([_hx / 17, _hy / 17 + 0.05]))
cmap = LinearSegmentedColormap.from_list(
    "love", ["#ff0a54", "#ff477e", "#ff85a1", "#fbb1bd", "#ffe3ea"])
N = 4500
outline = Path(np.column_stack(heart(np.linspace(0, 2 * np.pi, 400))))
px, py = [], []
while len(px) < N:
    c = np.column_stack([rng.uniform(-16, 16, 4000), rng.uniform(-17, 13, 4000)])
    c = c[outline.contains_points(c)]
    px.extend(c[:, 0]); py.extend(c[:, 1])
px, py = np.array(px[:N]), np.array(py[:N])
dist = np.clip(np.sqrt((px / 16) ** 2 + ((py + 2) / 14) ** 2), 0, 1)
pt_size = rng.uniform(2, 24, N) * (1.25 - dist)
pt_phase = rng.uniform(0, 2 * np.pi, N)
pt_rgba = cmap(1 - dist * 0.9)

NS = 200
st_xy = np.column_stack([rng.uniform(-26, 26, NS), rng.uniform(-24, 26, NS)])
st_size = rng.uniform(1, 12, NS)
st_phase = rng.uniform(0, 2 * np.pi, NS)

NF = 40
fl_x0 = rng.uniform(-25, 25, NF)
fl_y0 = rng.uniform(-24, 26, NF)
fl_speed = rng.uniform(0.5, 1.6, NF)
fl_size = rng.uniform(30, 240, NF)
fl_rgb = np.array([matplotlib.colors.to_rgb(c) for c in
                   rng.choice(["#ff85a1", "#ff477e", "#fbb1bd", "#c77dff"], NF)])

M = 46
S_STEPS = np.linspace(0, 1, M)

fig, ax = plt.subplots(figsize=(7, 7), dpi=64 if SAVE else 100)
fig.patch.set_facecolor("#0b0413")
fig.subplots_adjust(0, 0, 1, 1)
ax.set_facecolor("#0b0413")
ax.set_xlim(-26, 26); ax.set_ylim(-24, 26)
ax.set_aspect("equal"); ax.axis("off")

stars = ax.scatter(st_xy[:, 0], st_xy[:, 1], s=st_size, c="white",
                   alpha=0.4, linewidths=0, zorder=0)
floaters = ax.scatter(fl_x0, fl_y0, s=fl_size, marker=HEART_MARKER,
                      c=np.c_[fl_rgb, np.zeros(NF)], linewidths=0, zorder=1)

glow_layers = [(38, 0.035), (26, 0.06), (16, 0.10), (8, 0.18)]
glow_lines = [ax.plot([], [], color="#ff2e63", lw=w, alpha=a,
                      solid_capstyle="round", zorder=2)[0] for w, a in glow_layers]
core_line, = ax.plot([], [], color="#ffd6e0", lw=1.6, alpha=0.95, zorder=5)

fill = ax.scatter(px, py, s=pt_size, c=pt_rgba, linewidths=0, zorder=3)
tiny = ax.scatter([], [], s=95, marker=HEART_MARKER, c="#fff0f3",
                  alpha=0.95, linewidths=0, zorder=4)
tiny_glow = ax.scatter([], [], s=260, marker=HEART_MARKER, c="#ff4d6d",
                       alpha=0.18, linewidths=0, zorder=3.5)
spark_glow = ax.scatter([], [], s=900, c="#ff8fab", alpha=0.25, linewidths=0, zorder=6)
spark = ax.scatter([], [], s=140, c="white", alpha=0.95, linewidths=0, zorder=7)
label = ax.text(0, -1.5, "", ha="center", va="center", color="white",
                fontsize=26 if SAVE else 30, fontweight="bold", family="serif",
                style="italic", zorder=8)


def beat_scale(t):
    if t < T_BEAT:
        return 1.0
    amp = min(1, (t - T_BEAT) / 1.5)
    ph = (t - T_BEAT) % 1.15
    lub = np.exp(-((ph - 0.12) / 0.07) ** 2)
    dub = 0.6 * np.exp(-((ph - 0.40) / 0.08) ** 2)
    return 1 + 0.06 * amp * (lub + dub)


def sides(s, b):
    tr = np.pi - s * np.pi
    tl = np.pi + s * np.pi
    xr, yr = heart(tr); xl, yl = heart(tl)
    return (np.c_[xr, yr] * b), (np.c_[xl, yl] * b)


def update(frame):
    t = frame / FPS
    b = beat_scale(t)
    o = prog(t, T_OUTLINE)
    f = prog(t, T_FILL)
    stars.set_sizes(st_size * (0.6 + 0.4 * np.sin(2 * np.pi * (0.4 * t) + st_phase)))
    ramp = prog(t, (3.0, 8.0))
    fy = ((fl_y0 + fl_speed * t + 24) % 50) - 24
    fx = fl_x0 + 0.9 * np.sin(0.6 * t + fl_x0)
    floaters.set_offsets(np.c_[fx, fy])
    floaters.set_facecolor(np.c_[fl_rgb, np.full(NF, 0.42 * ramp)])

    if o > 0:
        ss = np.linspace(0, o, 220)
        R, L = sides(ss, b)
        sep = np.array([[np.nan, np.nan]])
        both = np.vstack([R, sep, L])
        g = (0.5 + 0.5 * f) * (1 + 4 * (b - 1))
        for line, (w, a) in zip(glow_lines, glow_layers):
            line.set_data(both[:, 0], both[:, 1]); line.set_alpha(min(1, a * g))
        core_line.set_data(both[:, 0], both[:, 1])
        core_line.set_alpha(0.95 if o < 1 else 0.0)

        k = int(np.sum(S_STEPS <= o))
        if k > 0:
            Rk, Lk = sides(S_STEPS[:k], b)
            pts = np.vstack([Rk, Lk])
            tiny.set_offsets(pts); tiny_glow.set_offsets(pts)

        if o < 1:
            heads = np.vstack([R[-1:], L[-1:]])
            spark.set_offsets(heads); spark_glow.set_offsets(heads)
            spark.set_sizes([140 + 60 * np.sin(t * 12)] * 2)
        else:
            spark.set_offsets(np.empty((0, 2))); spark_glow.set_offsets(np.empty((0, 2)))

    if f > 0:
        a_i = np.clip((f * 1.35 - dist) / 0.35, 0, 1)
        twinkle = 0.75 + 0.25 * np.sin(2 * np.pi * 0.7 * t + pt_phase)
        rgba = pt_rgba.copy()
        rgba[:, 3] = 0.9 * a_i
        fill.set_facecolor(rgba)
        fill.set_offsets(np.c_[px * b, py * b])
        fill.set_sizes(pt_size * twinkle * (0.5 + 0.5 * a_i))
    else:
        fill.set_facecolor(np.c_[pt_rgba[:, :3], np.zeros(N)])

    k = int(round(len(TEXT) * prog(t, T_TEXT)))
    label.set_text(TEXT[:k])
    label.set_fontsize((26 if SAVE else 30) * b)
    return []

frames = int(TOTAL * FPS)
ani = FuncAnimation(fig, update, frames=frames, interval=1000 / FPS,
                    blit=False, repeat=True)

if __name__ == "__main__":
    if SAVE:
        ani.save("", writer=PillowWriter(fps=FPS))
        print("")
    else:
        plt.show()