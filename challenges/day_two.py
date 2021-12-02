from helpers import read_input

def day_two_part_one(puzzle_input):
    horizontal = 0
    depth = 0
    for line in puzzle_input:
        split = line.split()
        if split[0] == 'forward':
            horizontal += int(split[1])
        elif split[0] == 'up':
            depth -= int(split[1])
        elif split[0] == 'down':
            depth += int(split[1])
    return horizontal * depth

def day_two_part_two(puzzle_input):
    horizontal = 0
    depth = 0
    aim = 0
    for line in puzzle_input:
        split = line.split()
        if split[0] == 'forward':
            horizontal += int(split[1])
            depth += aim * int(split[1])
        elif split[0] == 'up':
            aim -= int(split[1])
        elif split[0] == 'down':
            aim += int(split[1])
    return horizontal * depth

if __name__ == '__main__':
    items = read_input('day_two.txt')
    print("Day Two:")
    print(f'-- Part One: {day_two_part_one(items)}')
    print(f'-- Part Two: {day_two_part_two(items)}')