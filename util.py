from datetime import time


def is_within_time_ranges(current_time):
    # 定义时间段
    range1_start = time(9, 15)
    range1_end = time(11, 30)
    range2_start = time(13, 0)
    range2_end = time(15, 0)

    # 检查当前时间是否在任一时间段内
    return (range1_start <= current_time <= range1_end) or (range2_start <= current_time <= range2_end)
