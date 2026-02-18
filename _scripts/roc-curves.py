"""Generate ROC curve plot for the 'why roc curves?' bog post."""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["mathtext.fontset"] = "cm"

# ROC points from the worked example (FPR, TPR), ordered for plotting
points = [
    (0.0, 0.0),   # threshold 0.95
    (0.0, 0.5),   # threshold 0.8
    (1/3, 0.5),   # threshold 0.55
    (1/3, 1.0),   # threshold 0.3
    (2/3, 1.0),   # threshold 0.15
    (1.0, 1.0),   # threshold 0.05
]

fpr = [p[0] for p in points]
tpr = [p[1] for p in points]

KLEIN_BLUE = "#002FA7"

fig, ax = plt.subplots(figsize=(5, 5))

# Compute AUC via trapezoidal rule
auc = np.trapezoid(tpr, fpr)

# Diagonal (random classifier baseline)
ax.plot([0, 1], [0, 1], color="black", linestyle="--", linewidth=0.8,
        label=f"Random (AUC = 0.50)")

# ROC curve
ax.plot(fpr, tpr, color=KLEIN_BLUE, linewidth=2, zorder=3,
        label=f"Toy Classifier (AUC = {auc:.2f})")
ax.scatter(fpr, tpr, color=KLEIN_BLUE, s=30, zorder=4)

# Unit square
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
ax.set_aspect("equal")
ax.spines["top"].set_color("black")
ax.spines["right"].set_color("black")
ax.spines["bottom"].set_color("black")
ax.spines["left"].set_color("black")

# Labels
ax.set_xlabel("False Positive Rate", fontsize=12)
ax.set_ylabel("True Positive Rate", fontsize=12)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.tick_params(labelsize=10)

# Legend in lower right
ax.legend(loc="lower right", fontsize=10, framealpha=0.9)

fig.tight_layout()

out_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "why-roc-curves")
fig.savefig(os.path.join(out_dir, "roc-curve.svg"), bbox_inches="tight")
fig.savefig(os.path.join(out_dir, "roc-curve.png"), bbox_inches="tight", dpi=200)
print("Saved to assets/images/why-roc-curves/")
