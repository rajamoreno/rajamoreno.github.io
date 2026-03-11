import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# LaTeX-style rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "axes.labelsize": 14,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "figure.dpi": 200,
})

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "axes-of-control")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def make_base_plot():
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Draw axes as simple lines (no arrows — scale saturates at 100)
    ax.plot([0, 100], [0, 0], color="black", lw=0.8, clip_on=False)
    ax.plot([0, 0], [0, 100], color="black", lw=0.8, clip_on=False)

    # Ticks every 10, larger at 50 and 100
    for v in range(10, 110, 10):
        length = 2.5 if v in (50, 100) else 1.5
        lw = 1.0 if v in (50, 100) else 0.6
        ax.plot([v, v], [0, length], color="black", lw=lw, clip_on=False)
        ax.plot([0, length], [v, v], color="black", lw=lw, clip_on=False)

    # Label 100
    ax.text(100, -4, r"100", fontsize=9, ha="center", va="top")
    ax.text(-4, 100, r"100", fontsize=9, ha="right", va="center")

    ax.set_xlabel(r"harmful", fontsize=14)
    ax.set_ylabel(r"incriminating", fontsize=14)

    fig.tight_layout()
    return fig, ax


FOREST_GREEN = "#228B22"


def add_perfect_observer(ax, arrow=True):
    end = 100
    if arrow:
        ax.annotate(
            "", xy=(85, 85), xytext=(0, 0),
            arrowprops=dict(
                arrowstyle="->,head_width=0.25,head_length=0.2",
                color=FOREST_GREEN, lw=1.5,
            ),
        )
    else:
        ax.plot([0, end], [0, end], color=FOREST_GREEN, lw=1.5, zorder=2)
    ax.text(
        50, 46, r"perfect monitor",
        fontsize=12, color=FOREST_GREEN, rotation=45,
        ha="center", va="center",
    )


import numpy as np


BLOB_ALPHA = 0.12
BLOB_EDGE_ALPHA = 0.4


def _soft_blob(ax, cx, cy, radius, color, label, label_offset=(0, 0)):
    """Draw a soft circular blob with a label."""
    theta = np.linspace(0, 2 * np.pi, 200)
    # Slight randomness for an organic feel
    r = radius + 1.5 * np.sin(5 * theta) + 1.0 * np.sin(7 * theta + 1)
    x = cx + r * np.cos(theta)
    y = cy + r * np.sin(theta)
    ax.fill(x, y, color=color, alpha=BLOB_ALPHA, zorder=1)
    ax.plot(x, y, color=color, alpha=BLOB_EDGE_ALPHA, lw=1.0, zorder=1)
    ax.text(
        cx + label_offset[0], cy + label_offset[1], label,
        fontsize=12, color=color, ha="center", va="center", zorder=2,
    )


PASTEL_PURPLE = "#9B72CF"
PASTEL_ORANGE = "#E8913A"


def add_bands(ax):
    """Single continuous diagonal strip with gradient fill, corner to corner."""
    # Band starts at (10, 0)/(0, 10) — half-width of 10/sqrt(2) ≈ 7.07
    half_w = 10 / np.sqrt(2)  # so the band edges hit (10, 0) and (0, 10)
    dx = half_w
    n = 80

    # Extend beyond bounds so corners fill cleanly
    lo, hi = -12, 112

    purple = np.array([0.608, 0.447, 0.812])  # #9B72CF
    orange = np.array([0.910, 0.569, 0.227])  # #E8913A

    for i in range(n):
        t0 = i / n
        t1 = (i + 1) / n
        p0 = lo + t0 * (hi - lo)
        p1 = lo + t1 * (hi - lo)
        verts = [
            (p0 + dx, p0 - dx),
            (p1 + dx, p1 - dx),
            (p1 - dx, p1 + dx),
            (p0 - dx, p0 + dx),
        ]
        t_mid = (t0 + t1) / 2
        color = purple + t_mid * (orange - purple)
        poly = plt.Polygon(verts, closed=True, fc=color, ec="none",
                            alpha=0.18, zorder=1)
        ax.add_patch(poly)

    # Outer edge
    edge_verts = [
        (lo + dx, lo - dx), (hi + dx, hi - dx),
        (hi - dx, hi + dx), (lo - dx, lo + dx),
    ]
    ax.add_patch(plt.Polygon(edge_verts, closed=True, fc="none", ec="#999999",
                              alpha=0.2, linewidth=0.8, zorder=1))

    # Labels hugging the line, just above it (like "perfect monitor" sits below)
    ax.text(14, 18, r"low-stakes", fontsize=11, color=PASTEL_PURPLE,
            ha="center", va="center", rotation=45, zorder=2)
    ax.text(80, 84, r"high-stakes", fontsize=11, color=PASTEL_ORANGE,
            ha="center", va="center", rotation=45, zorder=2)


def save(fig, name):
    out = os.path.join(OUTPUT_DIR, name)
    fig.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"Saved to {out}")
    plt.close(fig)


BERMUDA_RED = "#B22222"


def add_danger_cluster(ax, faded=False):
    """Cluster of bright red dots in the lower-right: harmful but not incriminating."""
    rng = np.random.RandomState(42)
    n_dots = 10
    cx, cy = 80, 20
    ddx = rng.normal(0, 6, n_dots)
    ddy = rng.normal(0, 6, n_dots)

    # When faded, exclude dots near the CMFT label
    if faded:
        cmft_zone = (80, 20, 8, 6)  # (cx, cy, half_w, half_h)
        mask = [not (abs(cx + x - cmft_zone[0]) < cmft_zone[2]
                     and abs(cy + y - cmft_zone[1]) < cmft_zone[3])
                for x, y in zip(ddx, ddy)]
        ddx, ddy = ddx[mask], ddy[mask]

    alpha = 0.25 if faded else 0.7
    ax.scatter(cx + ddx, cy + ddy, color=BERMUDA_RED, alpha=alpha, s=35,
               edgecolors="none", zorder=3)

    bbox = (dict(facecolor="white", edgecolor="none", alpha=0.85, pad=2)
            if faded else None)
    ax.text(cx, 25, "harmful actions that are not very" "\n"
            "incriminating to current monitors",
            fontsize=8.5, color=BERMUDA_RED, ha="center", va="bottom",
            zorder=6, bbox=bbox)


OCEAN_BLUE = "#1F3085"


def add_lattice_labels(ax):
    ax.text(25, 75, r"looks scarier" "\n" r"than it is",
            fontsize=11, color=OCEAN_BLUE, ha="center", va="center",
            alpha=0.7, zorder=4)
    ax.text(75, 25, r"is scarier" "\n" r"than it looks",
            fontsize=11, color=BERMUDA_RED, ha="center", va="center",
            alpha=0.7, zorder=4)


def add_lattice_dots(ax):
    """Dots on every 10-unit lattice point, colored by distance from y=x."""
    max_dist = 90 / np.sqrt(2)  # max possible distance from the line
    for x in range(10, 110, 10):
        for y in range(10, 110, 10):
            if x == y:
                continue
            # Signed distance from y=x: positive = above line, negative = below
            signed_dist = (y - x) / np.sqrt(2)
            t = abs(signed_dist) / max_dist
            if signed_dist > 0:
                # Above line: blue, half max saturation
                color = OCEAN_BLUE
                alpha = t * 0.45
            else:
                # Below line: red, full saturation
                color = BERMUDA_RED
                alpha = t * 0.9
            alpha = max(alpha, 0.05)  # minimum visibility
            ax.plot(x, y, "o", color=color, alpha=alpha, markersize=5,
                    markeredgecolor=color, markeredgewidth=0, zorder=3,
                    clip_on=False)


SKITTISH_PINK = "#D4607A"
PANGLOSSIAN_BLUE = "#5B7FA5"


def add_monitors(ax):
    """Scatter dots for skittish (y~90) and panglossian (y~10) monitors."""
    rng = np.random.RandomState(17)
    n_dots = 45

    # Label exclusion zones (x_center, y_center, half_width, half_height)
    labels = [
        (50, 96, 28, 4),  # skittish label
        (50, 4, 28, 4),   # panglossian label
    ]

    def in_label_zone(x, y):
        for cx, cy, hw, hh in labels:
            if abs(x - cx) < hw and abs(y - cy) < hh:
                return True
        return False

    # Skittish monitor: x spread across full range, y clustered near 90
    sx = rng.uniform(5, 95, n_dots)
    sy = rng.normal(90, 4, n_dots)
    sy = np.clip(sy, 75, 99)
    mask = [not in_label_zone(x, y) for x, y in zip(sx, sy)]
    ax.scatter(sx[mask], sy[mask], color=SKITTISH_PINK, alpha=0.5, s=25,
               edgecolors="none", zorder=3)

    # Stoic monitor: x spread across full range, y clustered near 10
    stx = rng.uniform(5, 95, n_dots)
    sty = rng.normal(10, 4, n_dots)
    sty = np.clip(sty, 1, 25)
    mask = [not in_label_zone(x, y) for x, y in zip(stx, sty)]
    ax.scatter(stx[mask], sty[mask], color=PANGLOSSIAN_BLUE, alpha=0.5, s=25,
               edgecolors="none", zorder=3)

    # Labels
    ax.text(50, 96, r"skittish monitor: always scared",
            fontsize=9, color=SKITTISH_PINK, ha="center", va="center", zorder=4)
    ax.text(50, 4, r"panglossian monitor: not scared enough",
            fontsize=9, color=PANGLOSSIAN_BLUE, ha="center", va="center", zorder=4)


def add_lift_arrow(ax):
    """Show a red CMFT dot in the danger zone being lifted to the green line."""
    cmft_x = 80
    cmft_y = 20
    # Saturated CMFT dot
    ax.scatter([cmft_x], [cmft_y], color=BERMUDA_RED, s=60, zorder=7,
               edgecolors="none")
    ax.text(cmft_x, cmft_y - 3, "CMFT", fontsize=9, color=BERMUDA_RED,
            ha="center", va="top", zorder=7)
    # Dashed blue arrow from the red dot up to the green line
    from matplotlib.patches import FancyArrowPatch
    arrow = FancyArrowPatch(
        (cmft_x, cmft_y), (cmft_x, cmft_x),
        arrowstyle="->,head_width=5,head_length=4",
        color=OCEAN_BLUE, lw=1.5, linestyle="--", zorder=5,
    )
    ax.add_patch(arrow)
    # Saturated green dot at destination
    ax.scatter([cmft_x], [cmft_x], color=OCEAN_BLUE, s=60, alpha=0.85,
               zorder=7, edgecolors="none")
    # Label along the dashed line
    ax.text(cmft_x - 3, (cmft_y + cmft_x) / 2 - 10,
            "applying elbow grease" "\n" "makes CMFT look" "\n"
            "as harmful as it is",
            fontsize=7, color=OCEAN_BLUE, ha="right", va="center",
            zorder=6)


def make_cost_plot():
    """New axes: x = harmful (0-100), y = cost to prevent (log scale)."""
    import matplotlib.transforms as transforms

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.set_xlim(0, 100)
    ax.set_ylim(1e-5, 1e14)
    ax.set_yscale("log")

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Blended transform: x in data coords, y in axes fraction
    trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)

    # X-axis line (at bottom) and Y-axis line
    ax.plot([0, 100], [0, 0], color="black", lw=0.8, clip_on=False,
            transform=trans)
    ax.plot([0, 0], [1e-5, 1e14], color="black", lw=0.8, clip_on=False)

    # X-axis ticks
    for v in range(10, 110, 10):
        length = 0.025 if v in (50, 100) else 0.015
        lw_t = 1.0 if v in (50, 100) else 0.6
        ax.plot([v, v], [0, length], color="black", lw=lw_t, clip_on=False,
                transform=trans)

    # Label 100 on x-axis (offset below axis, won't overlap y-label)
    ax.text(100, -0.04, r"100", fontsize=9, ha="center", va="top",
            transform=trans)

    # Y-axis ticks at every decade, no labels except endpoints
    for exp in range(-5, 15):
        val = 10.0 ** exp
        is_endpoint = exp in (-5, 14)
        tick_len = 2.5 if is_endpoint else 1.5
        lw_t = 1.0 if is_endpoint else 0.6
        ax.plot([0, tick_len], [val, val], color="black", lw=lw_t,
                clip_on=False)

    # Endpoint labels only
    ax.text(-3, 1e-5, r"\$1e-5", fontsize=8, ha="right", va="center")
    ax.text(-3, 1e14, r"\$1e14", fontsize=8, ha="right", va="center")

    # Arrow at top of y-axis extending beyond plot
    ax.annotate(
        "", xy=(0, 1.06), xytext=(0, 0.92),
        arrowprops=dict(
            arrowstyle="->,head_width=0.2,head_length=0.15",
            color="black", lw=0.8,
        ),
        xycoords=("data", "axes fraction"),
        textcoords=("data", "axes fraction"),
        clip_on=False,
    )

    ax.set_xlabel(r"harmful", fontsize=14)
    ax.set_ylabel(r"cost to prevent", fontsize=14)

    fig.tight_layout()
    return fig, ax


def add_cost_dots_with_arrows(ax):
    """Scatter red dots with arrows pointing down to lighter dots."""
    rng = np.random.RandomState(2008)

    # X: nicely but not perfectly spaced
    x_base = np.linspace(5, 95, 10)
    xs = x_base + rng.uniform(-4, 4, size=len(x_base))
    xs = np.clip(xs, 1, 99)

    # Y: broadly increasing up and to the right on a log scale
    log_y_base = np.linspace(3, 12, len(xs))
    log_y_noise = rng.normal(0, 2.5, size=len(xs))
    ys = 10 ** (log_y_base + log_y_noise)
    ys = np.clip(ys, 1e-5, 1e14)

    # Dramatic reductions: factor of 1000-1_000_000_000x
    reductions = 10 ** rng.uniform(3, 10, len(xs))
    ys_new = ys / reductions
    ys_new = np.clip(ys_new, 2e-5, None)

    for x, y_old, y_new in zip(xs, ys, ys_new):
        # Red dot at original cost
        ax.scatter([x], [y_old], color=BERMUDA_RED, s=40, zorder=5,
                   edgecolors="none")
        # Arrow pointing down
        ax.annotate(
            "", xy=(x, y_new), xytext=(x, y_old),
            arrowprops=dict(
                arrowstyle="->,head_width=0.2,head_length=0.15",
                color=BERMUDA_RED, lw=1.2, alpha=0.5,
            ),
            zorder=4,
        )
        # Lighter dot at reduced cost
        ax.scatter([x], [y_new], color=BERMUDA_RED, s=40, alpha=0.3,
                   zorder=5, edgecolors="none")


if __name__ == "__main__":
    fig, ax = make_base_plot()
    save(fig, "axes_of_control.png")

    fig, ax = make_base_plot()
    add_perfect_observer(ax, arrow=False)
    save(fig, "perfect_monitor.png")

    fig, ax = make_base_plot()
    add_perfect_observer(ax, arrow=False)
    add_monitors(ax)
    save(fig, "monitors.png")

    fig, ax = make_base_plot()
    add_perfect_observer(ax, arrow=False)
    add_bands(ax)
    save(fig, "bands.png")

    fig, ax = make_base_plot()
    add_perfect_observer(ax, arrow=False)
    add_bands(ax)
    add_danger_cluster(ax)
    save(fig, "danger_cluster.png")

    # Plot 7: Lift CMFT dot to the green line
    fig, ax = make_base_plot()
    add_perfect_observer(ax, arrow=False)
    add_bands(ax)
    add_danger_cluster(ax, faded=True)
    add_lift_arrow(ax)
    save(fig, "lift.png")

    # Plot 8: Cost axes (empty)
    fig, ax = make_cost_plot()
    save(fig, "cost_axes.png")

    # Plot 9: Cost axes with dots and reduction arrows
    fig, ax = make_cost_plot()
    add_cost_dots_with_arrows(ax)
    save(fig, "cost_reduction.png")
