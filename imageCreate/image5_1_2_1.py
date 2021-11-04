"""
 h = h + np.abs(i * np.cos(x * coslist[i] + y * sinlist[i]))
"""
from func import drawImage as di


if __name__ == '__main__':
    split_point = [-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 21]
    k_list = [2, 10, 8, 5, 6, 13, 15, 6, 10, 11, 6, 12, 6, 12, 15, 14, 6, 10, 1]
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    mag = 10
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    q = 5
    s = 12
    w = 900
    xmin = 1
    ymin = 1
    name = '5_1_4 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, 4)
