"""Kinematics of the declared 7-DoF arm (modified DH, vectorised FK + DLS IK)."""
from __future__ import annotations

import numpy as np

from kernel.rulebook import ARM

BASE = np.array(ARM["base_xyz"])
Q_LO, Q_HI = np.array(ARM["q_lower"]), np.array(ARM["q_upper"])
QD_MAX = np.array(ARM["qd_max"])
Q_READY = np.array([0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785])


def _mdh(a: float, d: float, alpha: float, theta: np.ndarray) -> np.ndarray:
    ct, st, ca, sa = np.cos(theta), np.sin(theta), np.cos(alpha), np.sin(alpha)
    T = np.zeros((theta.shape[0], 4, 4))
    T[:, 0, 0], T[:, 0, 1], T[:, 0, 3] = ct, -st, a
    T[:, 1, 0], T[:, 1, 1], T[:, 1, 2], T[:, 1, 3] = st * ca, ct * ca, -sa, -sa * d
    T[:, 2, 0], T[:, 2, 1], T[:, 2, 2], T[:, 2, 3] = st * sa, ct * sa, ca, ca * d
    T[:, 3, 3] = 1.0
    return T


def _tcp_const() -> np.ndarray:
    c, s = np.cos(-np.pi / 4), np.sin(-np.pi / 4)
    T = np.eye(4)
    T[:2, :2] = [[c, -s], [s, c]]
    T[2, 3] = ARM["flange_d"] + ARM["tcp_offset"]
    return T


TCP_CONST = _tcp_const()


def fk(q: np.ndarray, frames: bool = False):
    """World pose of the TCP for joint vectors q (N,7) -> (N,4,4)."""
    q = np.atleast_2d(np.asarray(q, dtype=float))
    T = np.tile(np.eye(4), (q.shape[0], 1, 1))
    T[:, :3, 3] = BASE
    joint_frames = []
    for i, (a, d, alpha) in enumerate(ARM["dh"]):
        T = T @ _mdh(a, d, alpha, q[:, i])
        joint_frames.append(T)
    Tt = T @ TCP_CONST
    return (Tt, joint_frames) if frames else Tt


def tcp_yaw(T: np.ndarray) -> np.ndarray:
    return np.arctan2(T[..., 1, 0], T[..., 0, 0])


def rot_to_quat(R: np.ndarray) -> np.ndarray:
    """(N,3,3) rotation matrices -> (N,4) quaternions (w,x,y,z)."""
    w = np.sqrt(np.clip(1 + R[:, 0, 0] + R[:, 1, 1] + R[:, 2, 2], 1e-12, None)) / 2
    x = np.sqrt(np.clip(1 + R[:, 0, 0] - R[:, 1, 1] - R[:, 2, 2], 0, None)) / 2
    y = np.sqrt(np.clip(1 - R[:, 0, 0] + R[:, 1, 1] - R[:, 2, 2], 0, None)) / 2
    z = np.sqrt(np.clip(1 - R[:, 0, 0] - R[:, 1, 1] + R[:, 2, 2], 0, None)) / 2
    x = np.copysign(x, R[:, 2, 1] - R[:, 1, 2])
    y = np.copysign(y, R[:, 0, 2] - R[:, 2, 0])
    z = np.copysign(z, R[:, 1, 0] - R[:, 0, 1])
    return np.stack([w, x, y, z], axis=1)


def topdown_rotation(yaw: float) -> np.ndarray:
    """TCP pointing straight down, finger-closing axis rotated by yaw."""
    c, s = np.cos(yaw), np.sin(yaw)
    return np.array([[c, s, 0.0], [s, -c, 0.0], [0.0, 0.0, -1.0]])


def ik(p_target, R_target, q0, iters: int = 200, margin: float = 0.05, tol: float = 2e-5):
    """Damped-least-squares IK with null-space pull toward Q_READY.

    Returns (q, residual_norm)."""
    q = np.array(q0, dtype=float)
    lo, hi = Q_LO + margin, Q_HI - margin
    err = np.inf
    for _ in range(iters):
        T, jf = fk(q, frames=True)
        T = T[0]
        p, R = T[:3, 3], T[:3, :3]
        e_p = p_target - p
        e_o = 0.5 * sum(np.cross(R[:, k], R_target[:, k]) for k in range(3))
        e = np.concatenate([e_p, e_o])
        err = float(np.linalg.norm(e))
        if err < tol:
            break
        J = np.zeros((6, 7))
        for i, F in enumerate(jf):
            z, o = F[0, :3, 2], F[0, :3, 3]
            J[:3, i], J[3:, i] = np.cross(z, p - o), z
        JJt = J @ J.T + 1e-6 * np.eye(6)
        J_pinv = J.T @ np.linalg.inv(JJt)
        dq = J_pinv @ e + (np.eye(7) - J_pinv @ J) @ (0.02 * (Q_READY - q))
        q = np.clip(q + dq, lo, hi)
    return q, err
