"""Geometry helpers for yaw-only oriented boxes (vectorised over frames)."""
from __future__ import annotations

import numpy as np


def box_penetration(pa, da, pb, db):
    """Penetration depth between two yaw-rotated boxes (separating-axis test).

    pa, pb: (N,4) arrays of [x, y, z_centroid, yaw]; da, db: (length, width, height).
    Returns (N,) depth in meters; <= 0 means the boxes are separated.
    """
    pa, pb = np.atleast_2d(pa), np.atleast_2d(pb)
    d = pb[:, :2] - pa[:, :2]
    axes = []
    for yaw in (pa[:, 3], pb[:, 3]):
        axes.append(np.stack([np.cos(yaw), np.sin(yaw)], 1))
        axes.append(np.stack([-np.sin(yaw), np.cos(yaw)], 1))

    def half_extent(p, dims, n):
        u = np.stack([np.cos(p[:, 3]), np.sin(p[:, 3])], 1)
        v = np.stack([-np.sin(p[:, 3]), np.cos(p[:, 3])], 1)
        return dims[0] / 2 * np.abs((u * n).sum(1)) + dims[1] / 2 * np.abs((v * n).sum(1))

    xy = np.full(len(pa), np.inf)
    for n in axes:
        ov = half_extent(pa, da, n) + half_extent(pb, db, n) - np.abs((d * n).sum(1))
        xy = np.minimum(xy, ov)
    z = np.minimum(pa[:, 2] + da[2] / 2, pb[:, 2] + db[2] / 2) - np.maximum(pa[:, 2] - da[2] / 2, pb[:, 2] - db[2] / 2)
    return np.minimum(xy, z)


def footprint_overlap(pa, da, pb, db):
    """Horizontal (xy) SAT overlap only; > 0 means footprints overlap."""
    big = (da[0], da[1], 1e3)
    pa2, pb2 = np.array(pa, float), np.array(pb, float)
    pa2[:, 2] = 0.0
    pb2[:, 2] = 0.0
    return box_penetration(pa2, big, pb2, (db[0], db[1], 1e3))
