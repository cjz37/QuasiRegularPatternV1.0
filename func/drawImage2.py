"""
h变换
"""
import numpy as np
import cv2 as cv
from numba import jit


@jit(nopython=True)
def get_h_set(q, s, w, xmin, ymin, tp):
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
    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    if 0 == tp:
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + 5 * (np.cos(x * coslist[i] + y * sinlist[i]))
                k = abs(h)
                k = np.divmod(k, 16)[1]
                h_set[ny][nx] = k
    elif 1 == tp:
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                if h < 0:
                    h1 = np.abs(h)
                if h >= 0:
                    h1 = h + h1
                k = np.divmod(h1, 16)[1]
                h_set[ny][nx] = k
    return h_set


def draw_image(q, s, w, name, xmin, ymin, tp):
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    W = w + 1
    h_set = get_h_set(q, s, w, xmin, ymin, tp)
    color_set = [[color_list[0] for col in range(W)] for row in range(W)]
    if len(color_set) == 0:
        print("No image to draw")
        return
    for i in range(W):
        for j in range(W):
            color_set[i][j] = color_list[h_set[i][j]]
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
