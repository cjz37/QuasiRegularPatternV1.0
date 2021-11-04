from func import drawImage as di


# if __name__ == '__main__':
#     split_point = [-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11]
#     k_list = [2, 10, 8, 5, 6, 13, 15, 6, 10, 11, 6, 12, 6, 12, 15, 14, 6, 10, 1]
#     color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
#                   [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
#                   [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
#                   [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
#     mag = 10
#     color_index = {}
#     di.build_color_index(color_index, split_point, k_list, mag)
#     # q = 3
#     # s = 24
#     # w = 900
#     # xmin = 1
#     # ymin = 1
#     # name = '2_2 {} {}pi'.format(q, s)
#     # di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point)
#
#     q_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     s_list = [24, 24, 24, 24, 36, 24, 36, 36, 36, 36]
#     w = 900
#     xmin = 1
#     ymin = 1
#     for i in range(len(q_list)):
#         q = q_list[i]
#         s = s_list[i]
#         name = '2_2 {} {}pi'.format(q, s)
#         di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point)


def draw(q, s, w, xmin, ymin):
    split_point = [-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11]
    k_list = [2, 10, 8, 5, 6, 13, 15, 6, 10, 11, 6, 12, 6, 12, 15, 14, 6, 10, 1]
    color_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                  [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                  [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                  [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    mag = 10
    color_index = {}
    di.build_color_index(color_index, split_point, k_list, mag)
    name = '5_2_1 {} {}pi'.format(q, s)
    di.draw_image(q, s, w, color_index, name, xmin, ymin, mag, color_list, split_point)
