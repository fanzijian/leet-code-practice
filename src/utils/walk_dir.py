#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

# all_target = os.walk("./src")

# for path, dir_list, file_list in all_target:
#     print file_list, dir_list
#     for dir_path in dir_list:
#         for file_path in file_list:
#             print(os.path.join(path, file_path))


def walk_dir(file_path):
    # 获取路径下所有的文件/文件夹名称
    file_list = os.listdir(file_path)
    rst = []
    for file in file_list:
        new_file_path = os.path.join(file_path, file)
        if os.path.isdir(new_file_path):
            rst.extend(walk_dir(new_file_path))
        else:
            rst.append(new_file_path)
            print new_file_path
    return rst


print walk_dir('./')
