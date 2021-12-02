import os

def read_input(path):
    lines = []
    with open(path) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line))
    return lines

def day_one_part_one(puzzle_input):
    incr = 0
    for i in range(1, len(puzzle_input)):
        if puzzle_input[i] > puzzle_input[i - 1]:
            incr += 1
    return incr

def day_one_part_two(puzzle_input):
    result = 0
    for i in range(1, len(puzzle_input)-2):
        prev_sum = puzzle_input[i-1] + puzzle_input[i] + puzzle_input[i+1]
        current_sum = puzzle_input[i] + puzzle_input[i+1] + puzzle_input[i+2]
        if current_sum > prev_sum:
            result += 1
    return result

if __name__ == '__main__':
    path = os.path.join('inputs', 'day_one')
    items = read_input(path)
    print('Day 1:')
    print(f'-- Part One: {day_one_part_one(items)}')
    print(f'-- Part Two: {day_one_part_two(items)}')
