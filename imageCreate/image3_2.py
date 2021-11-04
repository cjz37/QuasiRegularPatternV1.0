from func import drawImage as di


if __name__ == '__main__':
    split_point = [-9, -5, -4, -3, -2, -1.5, -1.45, -1.4, -1.35, -1.3, -1.25, -1.2, -1.15, -1.1, -1.05, -1, -0.95, -0.7, -0.5, -0.2,
                   -0.1, 0, 0.04, 0.2, 0.3, 0.5, 1.5, 3, 5, 7, 9, 11]
    k_list = [11, 14, 12, 5, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 10, 10, 1, 15, 15, 0, 15, 15, 15, 13, 15, 15, 1,
              10, 9]
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    mag = 100
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    q = 5
    s = 5
    w = 900
    xmin = 1
    ymin = 1
    name = '3_2 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list)