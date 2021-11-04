from func import drawImage as di
import random

if __name__ == '__main__':
    z = int((15 * random.random()) + 1)
    z1 = int((1500 * random.random()) / 100 + 1)
    z2 = int((60 * random.random()) / 4 + 0)
    z3 = int((45 * random.random()) / 3 + 0)
    z4 = int((30 * random.random()) / 2 + 0)
    z4 = int((150 * random.random()) / 10 + 0)
    z5 = int((15 * random.random()) + 0)
    split_point = [-7.5, -4, -3.5, -1, -2.5, -2, -1.5, -1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.25, 1.5, 2,
                   2.5, 3, 5, 7, 9, 11, 14]
    k_list = [z, z1, z2, z1, z3, z, z5+1, z2, z5, z5, z1, z4, z1, z1, z2, z4, z, z2, z1, z3, z5, z4, z2, z1, z4, z3, z5]
    mag = 100
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    q = 5
    s = 12
    w = 900
    xmin = 1
    ymin = 1
    name = '3_5 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag)