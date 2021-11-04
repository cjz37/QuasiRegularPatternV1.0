"""
颜色映射
（QBColor，自定义RGB）
模型变换
"""
import math
import numpy as np
import cv2 as cv
from numba import jit


@jit(nopython=True)
def get_h_set(q, s, w, xmin, ymin, mag, tp):
    pi = 3.1415927
    Q = q + 1
    W = w + 1
    xmax = xmin + s * np.pi
    ymax = ymin + s * np.pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)
    if 0 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * np.pi * i / q)
            sinlist[i] = np.sin(2 * np.pi * i / q)
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
            coslist[i] = np.cos(2 * np.pi * i / q)
            sinlist[i] = np.sin(2 * np.pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 2 == tp:
        for i in range(1, Q):
            coslist[i] = np.abs(np.cos(2 * np.pi * i / q))
            sinlist[i] = np.abs(np.sin(2 * np.pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 3 == tp:
        for i in range(1, Q):
            coslist[i] = np.abs(np.cos(2 * np.pi * i / q))
            sinlist[i] = np.abs(np.sin(2 * np.pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 4 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * np.pi * i / q)
            sinlist[i] = np.sin(2 * np.pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(i * np.cos(x * coslist[i] + y * sinlist[i]))
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
                    h = h + np.sin(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 6 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.tan(x * coslist[i] + y * sinlist[i])
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
                    h = h + 1 / np.cos(x * coslist[i] + y * sinlist[i])
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
                    h = h + np.cos(np.cos(x * coslist[i] + y * sinlist[i]))
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
                    h = h + np.sin(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 10 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.tan(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 11 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 12 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.tan(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 13 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * sinlist[i] + y * coslist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 14 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x / coslist[i] + y / sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 15 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.sin(x * coslist[i]) + np.cos(y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 16 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                cosx = np.cos(x)
                siny = np.sin(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(cosx * coslist[i] + siny * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 17 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                tanx = np.tan(x)
                rtany = 1 / np.tan(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(tanx * coslist[i] + rtany * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 18 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(np.cos(np.sin(x * coslist[i]) + np.cos(y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 19 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.abs(np.sin(x * coslist[i]) + np.cos(y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 20 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                cosx = np.cos(x)
                siny = np.sin(y)
                for i in range(1, Q):
                    h = h + np.tan(cosx * coslist[i] + siny * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 21 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                cosx = np.cos(x)
                siny = np.sin(y)
                for i in range(1, Q):
                    h = h + np.abs(cosx * coslist[i] + siny * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 22 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                cosx = np.cos(x)
                siny = np.sin(y)
                for i in range(1, Q):
                    h = h + np.cos(np.tan(cosx * coslist[i]) + np.tan(siny * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 23 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 24 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 25 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 15)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 26 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 27 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.tan(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 2)), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 28 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.tan(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 29 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.sqrt(np.abs(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 30 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 31 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 3)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 3)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 32 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 15)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 15)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 33 == tp:
        for i in range(1, Q):
            coslist[i] = np.sqrt(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.sqrt(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 34 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 35 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.power(np.abs(x), 0.75)
                Y = np.power(np.abs(y), 0.75)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 36 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.power(np.abs(x), 1.25)
                Y = np.power(np.abs(y), 1.25)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 37 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sin(np.sqrt(np.abs(x)))
                Y = np.cos(np.sqrt(np.abs(y)))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 38 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 39 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(X * coslist[i] + Y * sinlist[i]), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 40 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 41 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(X * coslist[i] + Y * sinlist[i]), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 42 == tp:
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sin(np.sqrt(np.abs(x)))
                Y = np.cos(np.sqrt(np.abs(y)))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 43 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 44 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 45 == tp:
        for i in range(1, Q):
            coslist[i] = np.exp(np.cos(2 * pi * i / q))
            sinlist[i] = np.exp(np.sin(2 * pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 46 == tp:
        for i in range(1, Q):
            coslist[i] = np.exp(np.sqrt(np.abs(np.cos(2 * pi * i / q))))
            sinlist[i] = np.exp(np.sqrt(np.abs(np.sin(2 * pi * i / q))))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 47 == tp:
        for i in range(1, Q):
            coslist[i] = np.exp(np.cos(2 * pi * i / q))
            sinlist[i] = np.exp(np.sin(2 * pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 48 == tp:
        for i in range(1, Q):
            coslist[i] = np.exp(np.cos(2 * pi * i / q))
            sinlist[i] = np.exp(np.sin(2 * pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i]))))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 49 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 50 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.tan(np.cos(x * coslist[i] + y * sinlist[i]))))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 51 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.tan(np.cos(x * coslist[i] + y * sinlist[i]))))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 52 == tp:
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 53 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 53 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 54 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.cos(np.log(np.abs(x)))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(X * coslist[i] + Y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 55 == tp:
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 56 == tp:
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 57 == tp:
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(X * coslist[i] + Y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 58 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = (np.sin(x) + np.cos(y)) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 59 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.cos(np.sin(x) + y) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 60 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = (x + y) / 25
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 61 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = (x * x + y * y) / 200
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 62 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.cos(temp) + np.power(np.sin(temp), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 63 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.cos(temp)
                    h = h + temp2 + np.power(np.sin(temp), 2) + np.power(temp2, 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 64 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.tan(temp) + np.power(np.cos(temp), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 65 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.cos(temp)
                    h = h + temp2 + np.power(temp2, 100) + np.power(temp2, 101)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 66 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.cos(temp)
                    for t in range(1, 6):
                        h = h + np.power(temp2, t)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 67 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.sin(temp)
                    for t in range(1, 6):
                        h = h + np.abs(temp2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 68 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.exp(np.cos(x) + np.sin(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 69 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.log(x * x + y * y) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 70 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.log(np.abs(np.sin(x) + np.cos(y))) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 71 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.abs(np.cos(temp)) + np.power(np.sin(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 72 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.abs(np.cos(temp) + np.power(np.sin(temp), 2))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 73 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.cos(np.cos(temp)) + np.power(np.sin(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 74 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.sin(temp) + np.power(np.cos(np.cos(temp)), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 75 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.tan(np.sin(temp)) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 76 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.exp(np.cos(temp)) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 77 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.exp(np.sin(temp)) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 78 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.log(np.abs(np.cos(temp))) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 79 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.log(np.abs(np.sin(temp))) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 80 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.log(np.abs(np.sin(temp))) + np.power(np.cos(temp), 100)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 81 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.abs(np.cos(temp)) + np.log(np.abs(np.cos(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 82 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.sin(temp) + np.log(np.abs(np.sin(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 83 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.exp(np.cos(temp)) + np.log(np.abs(np.cos(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 84 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.sqrt(np.exp(np.sin(temp))) + np.log(np.abs(np.cos(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 85 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.cos(x) * np.cos(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 86 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.sin(x) * np.cos(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 87 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.sin(x - y) * np.cos(x + y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 88 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.exp(np.sin(x)) * np.exp(np.cos(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 89 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.exp(np.sin(x)) * np.exp(np.cos(y)) * np.exp(np.sin(y)) * np.exp(np.cos(x))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 90 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                sinx = np.sin(x)
                cosy = np.cos(y)
                p = np.exp(sinx) * np.exp(cosy) * np.log(np.abs(sinx * cosy))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 91 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.cos(x * np.sin(coslist[i]) + y * np.sin(sinlist[i]))) \
                        + np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 92 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.tan(np.sin(x * coslist[i] + y * sinlist[i]) *
                                            np.power(np.sin(y * sinlist[i] + x * coslist[i]), 3)), 4)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 93 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.power(np.cos(x * np.cos(coslist[i]) + y * np.sin(sinlist[i])), q))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 94 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.power(np.cos(x * np.cos(coslist[i]) + y * np.sin(sinlist[i])), i))
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
