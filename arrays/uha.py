import numpy as np
import math


def uha(N, d):
    rows = int(math.floor(math.sqrt(N)))
    cols = int(math.ceil(N / rows))
    xs, ys = [], []
    count = 0

    for r in range(rows):
        y = (r - (rows - 1) / 2) * (np.sqrt(3) / 2 * d)
        offset = (r % 2) * (d / 2)

        for c in range(cols):
            if count >= N:
                break
            x = (c - (cols - 1) / 2) * d + offset
            xs.append(x)
            ys.append(y)
            count += 1

    xs = np.array(xs)
    ys = np.array(ys)

    xs -= np.mean(xs)
    ys -= np.mean(ys)

    return np.vstack((xs, ys, np.zeros(len(xs)))).T
