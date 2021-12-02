from helpers import read_input
import pandas as pd

def day_one_part_one(puzzle_input):
    incr = 0
    for i in range(1, len(puzzle_input)):
        if puzzle_input[i] > puzzle_input[i - 1]:
            incr += 1
    return incr

def day_one_part_one_pandas(puzzle_input):
    df = pd.DataFrame(puzzle_input)
    df['incr'] = df[0].rolling(2).apply(lambda arr: arr[0] < arr[1], raw=True)
    return int(df['incr'].sum())

def day_one_part_two(puzzle_input):
    result = 0
    for i in range(1, len(puzzle_input)-2):
        prev_sum = puzzle_input[i-1] + puzzle_input[i] + puzzle_input[i+1]
        current_sum = puzzle_input[i] + puzzle_input[i+1] + puzzle_input[i+2]
        if current_sum > prev_sum:
            result += 1
    return result

def day_one_part_two_pandas(puzzle_input):
    df = pd.DataFrame(puzzle_input)
    df['rolling'] = df[0].rolling(3).sum()
    df['incr'] = df['rolling'].rolling(2).apply(lambda arr: arr[0] < arr[1], raw=True)
    return int(df['incr'].sum())

if __name__ == '__main__':

    items = read_input('day_one.txt', parse_int=True)
    print('Day One:')
    print(f'-- Part One: {day_one_part_one(items)}')
    print(f'-- Part Two: {day_one_part_two(items)}')
