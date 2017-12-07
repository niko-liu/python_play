# encoding: utf-8

import numpy as np
import matplotlib.pyplot as pyt


def v_and_a():
    h = 0.1
    g = 9.81
    steps = 50
    x = np.zeros(steps)
    v = np.zeros(steps)
    t = np.zeros(steps)

    for i in range(steps):
        if (i + 1) == 50:
            break
        t[i + 1] = h * (i + 1)
        x[i + 1] = x[i] + h * v[i]
        v[i + 1] = v[i] - h * g

    pyt.figure("time--distance")
    pyt.plot(t, x)
    pyt.figure("time--vilocity")
    pyt.plot(t, v)
    pyt.show()


v_and_a()
