from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class SEIRParameters:
    beta: float = 3.0
    sigma: float = 0.5
    gamma: float = 0.5


@dataclass(frozen=True)
class SEIRInitialConditions:
    s0: float = 9999.0
    e0: float = 1.0
    i0: float = 0.0
    r0: float = 0.0


def simulate_seir(
    parameters: SEIRParameters = SEIRParameters(),
    init_conditions: SEIRInitialConditions = SEIRInitialConditions(),
    days: int = 51,
) -> Tuple[FloatArray, FloatArray, FloatArray, FloatArray]:
    """Simulate an SEIR model and return (S, E, I, R) arrays."""
    if days <= 0:
        raise ValueError("days must be a positive integer")

    beta, sigma, gamma = parameters.beta, parameters.sigma, parameters.gamma
    s0, e0, i0, r0 = init_conditions.s0, init_conditions.e0, init_conditions.i0, init_conditions.r0

    n = s0 + e0 + i0 + r0
    if n <= 0:
        raise ValueError("Total population must be positive")

    s: FloatArray = np.empty(days, dtype=np.float64)
    e: FloatArray = np.empty(days, dtype=np.float64)
    i: FloatArray = np.empty(days, dtype=np.float64)
    r: FloatArray = np.empty(days, dtype=np.float64)

    s[0], e[0], i[0], r[0] = s0, e0, i0, r0

    for t in range(1, days):
        e_new = (beta * s[t - 1] * i[t - 1]) / n
        i_new = sigma * e[t - 1]
        r_new = gamma * i[t - 1]

        s[t] = s[t - 1] - e_new
        e[t] = e[t - 1] + e_new - i_new
        i[t] = i[t - 1] + i_new - r_new
        r[t] = r[t - 1] + r_new

    return s, e, i, r

