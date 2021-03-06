"""
h = h + np.cos(np.abs(x) ^ 1.25 * coslist[i] + np.abs(y) ^ 1.25 * sinlist[i])
"""
from func import drawImage as di


def draw(q, s, w, xmin, ymin):
    split_point = [-28, -22, -18, -15, -12, -9, -5, -4, -3, -2.5, -2, -1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.5,
                   0.8, 1.25, 1.5, 2, 3, 5, 7, 9, 11, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
                   42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62]
    k_list = [0, 5, 3, 14, 15, 5, 13, 9, 3, 11, 0, 11, 12, 13, 14, 15, 11, 14, 14, 13, 15, 1, 12, 0, 12, 11, 10, 1, 13,
              14, 12, 14, 0, 11, 3, 0, 1, 13, 9, 14, 12, 0, 9, 1, 15, 14, 4, 9, 13, 3, 2, 9, 0, 1, 12]
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    mag = 100
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    name = '5_8_3 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point, 36)
