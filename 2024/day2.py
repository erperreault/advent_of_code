from collections import defaultdict, Counter

test_data = [line for line in open('test_data.txt')]
data = [line for line in open('real_data.txt')]

# data = test_data

data = [[int(value) for value in row] for row in [x.split() for x in data]]


def check_leap_size(current, next):
    return 0 < abs(current - next) < 4


def row_in_order(row):
    in_order = (row == sorted(row)) or (row == sorted(row, reverse=True))
    return in_order


def row_is_safe(row):
    for i in range(len(row)-1):
        if not check_leap_size(row[i], row[i+1]):
            return False
    return True


def row_is_valid(row):
    return row_in_order(row) and row_is_safe(row)


safe_reports = 0
for row in data:
    if row_is_valid(row):
        safe_reports += 1

print(safe_reports)


###


def row_is_valid_part_two(row):
    safe = True
    safe_for_part_one = row_is_valid(row)
    if not safe_for_part_one:
        safe = False
        for i in range(len(row)):
            new_row = row[:i] + row[i+1:]
            if row_is_valid(new_row):
                safe = True
                break
    return safe


safe_reports = 0
for row in data:
    if row_is_valid_part_two(row):
        safe_reports += 1

print(safe_reports)