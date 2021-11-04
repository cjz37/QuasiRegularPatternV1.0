from func import drawImage4 as di4


def draw(q, s, w, xmin, ymin):
    split_point = [-9, -5, -4, -3, -2.5, -2, -1.6, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.5, 1, 2.25, 3, 4, 5, 7, 11]
    k_list = [1, 9, 1, 14, 2, 15, 12, 14, 15, 13, 4, 14, 0, 5, 0, 11, 14, 1, 13, 10]
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    mag = 100
    color_index = {}
    di4.build_color_index(color_index, split_point, k_list, mag)
    name = '4_1 {} {}pi'.format(q, s)
    di4.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point)
