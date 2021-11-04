from func import drawImage as di


if __name__ == '__main__':
    split_point = [-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11]
    k_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    color_list = [[180, 10, 160], [200, 100, 10], [150, 50, 50], [190, 0, 250],
                  [100, 180, 0], [250, 250, 250], [0, 0, 250], [0, 0, 0],
                  [90, 90, 90], [220, 150, 50], [0, 50, 0], [70, 0, 0],
                  [150, 0, 0], [180, 180, 0], [100, 100, 0], [160, 0, 160],
                  [250, 5, 250], [180, 20, 200], [180, 10, 160]]
    mag = 10
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    q = 5
    s = 24
    w = 900
    xmin = 1
    ymin = 1
    name = '3_8 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list)
