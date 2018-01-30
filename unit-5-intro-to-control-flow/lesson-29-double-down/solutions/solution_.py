def double_down(num, times_doubled):
    count = 0
    while count < times_doubled:
        num *= 2
        count += 1
    return num