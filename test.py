# coding:utf-8
import os, sys
import time
from typing import List


def mk_dirs(dir_list=None):
    for each_path in dir_list:
        dir_path = os.path.dirname(os.path.abspath(each_path))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


def generate_times(month: int, daily: List[int]):
    ret = []
    # 每一个子项代表取哪个小时时间段，如8点到12点注意左闭右开
    day_time = [
        [8, 12],
        [13, 18],
        [19, 21],
        [22, 24],
    ]
    # N代表每隔几分钟取一个时间点
    N = 1
    for day in daily:
        for hours_interval in day_time:
            for hours in range(hours_interval[0], hours_interval[1]):
                for minutes in range(0, 60, N):
                    timestamp = time.mktime((2021, month, day, hours, minutes, 0, 0, 0, 0))
                    date_tuple = time.localtime(timestamp)
                    date = time.strftime("%Y_%m_%d_%H_%M_%S", date_tuple)
                    ret.append([int(timestamp), date])
                    print([int(timestamp), date])
    return ret


def parse_device_id(month: int, daily: List[int]):
    device_txt = r'D:\zyc-scripts\SuZhou_retrieve_data\IEF_Edge_Client\input_label\1.txt'
    dst_dir = r'D:\zyc-scripts\SuZhou_retrieve_data\IEF_Edge_Client\out\labels'
    times = generate_times(month, daily)
    with open(device_txt, 'r') as rf:
        for deviceID in rf:
            deviceID = deviceID.strip()
            name_index = 1
            for timestamp, date in times:
                name_index += 1
                file_name = date + '_' + str(name_index).zfill(4) + '_' + str(timestamp) + '_' + deviceID + '.txt'
                day = date[0:10]
                file_path = os.path.join(dst_dir, day, deviceID, file_name)
                mk_dirs([file_path])
                with open(file_path, 'w') as _:
                    pass


if __name__ == '__main__':
    parse_device_id(5, [1, 2, 3])
