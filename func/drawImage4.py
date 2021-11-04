"""
q浮点数
"""
import math
import numpy as np
import cv2 as cv
from numba import jit


@jit(nopython=True)
def get_h_set(q, s, w, xmin, ymin, mag, tp):
    pi = 3.1415927
    Q = round(q) + 1
    # Q = q + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    if 0 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 1 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(i * x * coslist[i] + i * y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 2 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + i * np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 3 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i] + i)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 4 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + i/8
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 5 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + 2 * np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 6 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q + 0.5)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 7 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(3.5 * x * coslist[i] + 1.5 * y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 8 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + 1
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 9 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(3.5 * x * coslist[i] + 1.5 * y * sinlist[i] + 0.5) + 1
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    return h_set


def draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point, tp=0):
    W = w + 1
    h_set = get_h_set(q, s, w, xmin, ymin, mag, tp)
    color_set = [[color_list[0] for col in range(w + 1)] for row in range(w + 1)]
    if len(color_set) == 0:
        print("No image to draw")
        return
    for i in range(W):
        for j in range(W):
            # color_set[i][j] = color_list[color_index[h_set[i][j]]]
            if h_set[i][j] <= split_point[0] * mag:
                color_set[i][j] = color_list[color_index[split_point[1] * 10]]
            elif h_set[i][j] > split_point[-1] * mag:
                color_set[i][j] = color_list[color_index[split_point[-1] * 10]]
            else:
                color_set[i][j] = color_list[color_index[h_set[i][j]]]
    img = np.array(color_set, dtype=np.uint8)

    cv.namedWindow(name)
    cv.moveWindow(name, 200, 50)
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()
    elif k == ord('s'):
        filename = 'images/' + name + '.png'
        cv.imwrite(filename, img)
        cv.destroyAllWindows()


def build_an_interval(a, b, k, mag):
    a = int(a * mag)
    b = int(b * mag)
    seq = np.arange(b, a, -1)
    interval = dict.fromkeys(seq, k)
    return interval


def build_color_index(color_index, split_point, k_list, mag):
    for i in range(len(k_list)):
        color_index.update(build_an_interval(split_point[i], split_point[i+1], k_list[i], mag))