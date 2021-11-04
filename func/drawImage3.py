"""
h控制RGB
"""
import numpy as np
import cv2 as cv
import random
from numba import jit


@jit(nopython=True)
def get_set(q, s, w, xmin, ymin, tp):
    Q = q + 1
    W = w + 1
    xmax = xmin + s * np.pi
    ymax = ymin + s * np.pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    color_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)
    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    kn = 0.05
    pw2kn = np.power(2, kn)

    # Se1 = int(random.random() * 255 + 1)
    # Se2 = int(random.random() * 255 + 1)
    # Se3 = int(random.random() * 255 + 1)
    Se1 = 239
    Se2 = 152
    Se3 = 16
    # Se1 = 253
    # Se2 = 24
    # Se3 = 11

    if 0 == tp:
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + (np.cos(x * coslist[i] + y * sinlist[i]))
                t = np.log(np.abs(100 * h + 1e-6)) * pw2kn
                R = 256 - int(np.abs(np.divmod(np.abs(Se1 - (1 * Se2 - 256) * t), 512)[1] - 256))
                G = 256 - int(np.abs(np.divmod(np.abs(Se2 - (2 * Se3 - 256) * t), 512)[1] - 256))
                B = 256 - int(np.abs(np.divmod(np.abs(Se3 - (3 * Se1 - 256) * t), 512)[1] - 256))
                if R > 255:
                    R = 255
                if G > 255:
                    G = 255
                if B > 255:
                    B = 255

                color_set[ny][nx] = B * 1e6 + G * 1e3 + R
    elif 1 == tp:
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + (np.cos(x * coslist[i] + y * sinlist[i]))
                Sinh = np.sin(h)
                Cosh = np.cos(h)
                R = 256 - int(np.abs(np.divmod(np.abs(Se1 - (1 * Se2 - 256) * np.exp(2 * Sinh + 1e-6) * kn), 512)[1]
                                     - 256))
                G = 256 - int(np.abs(np.divmod(np.abs(Se2 - (2 * Se3 - 256) * np.exp(3 * Cosh + 1e-6) * kn), 512)[1]
                                     - 256))
                B = 256 - int(np.abs(np.divmod(np.abs(Se3 - (3 * Se1 - 256) * np.exp(4 * Sinh + 1e-6) * kn), 512)[1]
                                     - 256))
                if R > 255:
                    R = 255
                if G > 255:
                    G = 255
                if B > 255:
                    B = 255

                color_set[ny][nx] = B * 1e6 + G * 1e3 + R

    return color_set


def draw_image(q, s, w, name, xmin, ymin, tp):
    color_set = get_set(q, s, w, xmin, ymin, tp)
    W = w + 1
    if len(color_set) == 0:
        print("No points to draw")
        return

    for i in range(W):
        for j in range(W):
            temp = color_set[i][j]
            B = int(temp / 1e6)
            G = int((temp - B * 1e6) / 1e3)
            R = int(temp - B * 1e6 - G * 1e3)
            color_set[i][j] = [B, G, R]

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
