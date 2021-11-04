from func import drawImage as di


if __name__ == '__main__':
    split_point = [-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11]
    k_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    color_list = [[30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60],
                  [60, 60, 70], [80, 80, 80], [90, 90, 90], [105, 105, 105],
                  [120, 120, 120], [135, 135, 135], [150, 150, 150], [165, 165, 165],
                  [180, 180, 180], [195, 195, 195], [210, 210, 210], [225, 225, 225],
                  [235, 235, 235], [245, 245, 245], [255, 255, 255]]
    mag = 10
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    q = 3
    s = 8
    w = 900
    xmin = 1
    ymin = 1
    name = '3_9 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list)
