from input import input

max_counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_reveals(reveals):
    for turn in reveals:
        for balls in turn:
            count, color = tuple(balls.split())
            if int(count) > max_counts[color]:
                return False
    return True
    
def get_power(reveals):
    highest = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for turn in reveals:
        for balls in turn:
            count, color = tuple(balls.split())
            if int(count) > highest[color]:
                highest[color] = int(count)
    return highest["red"] * highest["blue"] * highest["green"]
    

def part_1(input):
    result = []
    lines = input.split('\n')
    for line in lines:
        splitted_line = line.split(': ')
        game_id = int(splitted_line[0].split()[1])
        reveals = [r.split(', ') for r in splitted_line[1].split('; ')]
        valid = check_reveals(reveals)
        result.append({"id": game_id, "valid": valid})
    return result
    
def part_2(input):
    result = []
    lines = input.split('\n')
    for line in lines:
        splitted_line = line.split(': ')
        game_id = int(splitted_line[0].split()[1])
        reveals = [r.split(', ') for r in splitted_line[1].split('; ')]
        power = get_power(reveals)
        result.append(power)
    return result

sum_1 = 0
part_1_reveals = part_1(input)
for i in part_1_reveals:
    if i["valid"]:
        sum_1 += i["id"]
print(sum_1)

part_2_powers = part_2(input)
print(sum(part_2_powers))
