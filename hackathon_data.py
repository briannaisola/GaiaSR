"""
Source: Cian Roche's processed Gaia DR3 6D kinematics catalogue,
https://doi.org/10.5281/zenodo.8088365, pipeline and column documentation at
https://github.com/CianMRoche/GAIA-DR3-6D-Kinematics. ~33 million stars with
full 6D phase-space information (position, proper motion, radial velocity)
and propagated uncertainties, in equatorial, galactic and galactocentric
frames.
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"

BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"

SERIES = [BLUE, ORANGE, AQUA]


def use_house_style() -> None:
    mpl.rcParams.update({
        "figure.dpi": 120,
        "savefig.dpi": 120,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "axes.titleweight": "medium",
        "axes.titlelocation": "left",
        "axes.titlepad": 9,
        "axes.labelcolor": INK_2,
        "axes.edgecolor": AXIS,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelcolor": INK_2,
        "ytick.labelcolor": INK_2,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.9,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "grid.linestyle": "-",
        "axes.grid": True,
        "axes.axisbelow": True,
        "legend.frameon": False,
        "lines.linewidth": 2.0,
        "lines.solid_capstyle": "round",
        "figure.constrained_layout.use": True,
    })


use_house_style()


def _finish(ax, title=None, xlabel=None, ylabel=None):
    if title:
        ax.set_title(title, color=INK)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return ax


def plot_cut(x, y, z, r_helio, r_cut, title=None):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 3.9))
    ax1.scatter(x, y, s=4, color=BLUE, alpha=0.25, lw=0)
    ax1.set_aspect("equal")
    _finish(ax1, title="galactocentric x-y of the cut", xlabel="x (kpc)", ylabel="y (kpc)")

    ax2.hist(r_helio, bins=60, color=MUTED, alpha=0.7)
    ax2.axvline(r_cut, color=ORANGE, lw=1.6, ls=(0, (5, 3)))
    _finish(ax2, title="heliocentric distance of everything read in",
            xlabel="r_helio (kpc)", ylabel="stars")
    if title:
        fig.suptitle(title, color=INK, x=0.005, ha="left", fontsize=12)
    return fig


def plot_phase_space(x, y, z, vx, vy, vz):

    fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.6))
    pairs = [(x, y, "x (kpc)", "y (kpc)"), (x, z, "x (kpc)", "z (kpc)"),
             (y, z, "y (kpc)", "z (kpc)")]
    for ax, (a, b, xl, yl) in zip(axes, pairs):
        ax.scatter(a, b, s=4, color=BLUE, alpha=0.25, lw=0)
        ax.set_aspect("equal")
        _finish(ax, xlabel=xl, ylabel=yl)
    axes[0].set_title("positions, relative to the sample centre", loc="left", color=INK)

    fig2, ax = plt.subplots(figsize=(7.4, 4.0))
    for v, label, colour in zip([vx, vy, vz], ["v_x", "v_y", "v_z"], SERIES):
        ax.hist(v, bins=80, histtype="step", color=colour, lw=1.8, label=label, density=True)
    ax.legend(loc="upper right")
    _finish(ax, title="local velocity distribution", xlabel="km/s", ylabel="density")
    return fig, fig2
