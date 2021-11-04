"""
嵌套
for t in range(1, n+1)
h = h + Abs(Sin(x * Cos(2 * pi * i / q) + y * Sin(2 * pi * i / q)))
"""
from func import drawImage as di


def draw(q, s, w, xmin, ymin):
    split_point = [-9, -5, -4, -3, -2, -1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 3, 5, 7, 9, 11]
    k_list = [2, 7, 9, 15, 4, 2, 11, 6, 8, 1, 12, 10, 14, 5, 13, 2, 11, 10, 1]
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    mag = 10
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    name = '5_6_3_6 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point, 67)
