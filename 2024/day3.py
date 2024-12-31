import re

# with open('test_data.txt') as puzzle_input:
with open('real_data.txt') as puzzle_input:
    data = puzzle_input.read()
    print(data)

    multiplier_regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    matches = re.findall(multiplier_regex, data)

    print(matches)

    total = 0
    do = True
    for match in matches:
        print(do, match)
        if match == "don't()":
            do = False
        elif match == "do()":
            do = True
        elif do:
            left, right = match[4:-1].split(',')
            total += int(left) * int(right)
    print(total)