from helpers import read_input

class Day_Three:

    def __init__(self, useDemoInput=False):
        self.puzzle_input = read_input("day_three.txt")
        self.demo_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

        if useDemoInput:
            self.puzzle_input = self.demo_input

        self.prep = [self._split_by_char(puzzle_line) for puzzle_line in self.puzzle_input]
        self.len_x = len(self.prep[0])
        self.len_y = len(self.prep)

    # Splits the given word into a char array
    def _split_by_char(self, word):
        return [char for char in word]

    # Calculates the absolute number of one values in a given list
    def _calculate_abs_value(self, input_list):
        abs_value = []
        len_x = len(input_list[0])
        len_y = len(input_list)

        for i in range(len_x):
            count_one = 0
            for j in range(len_y):
                if input_list[j][i] == '1':
                    count_one += 1
            abs_value.append(count_one)
        return abs_value

    # Calculates the more value (0 or 1) of the given list at every index
    def _calculate_more_common(self, input_list):
        return [str((int(val) >= (len(input_list) / 2)) * 1) for val in self._calculate_abs_value(input_list)]

    def _helper_part_two(self, input_list, *, use_most_common):
        copy_list = input_list.copy()  # only mutate a copy
        for idx_x in range(self.len_x):
            most_common = self._calculate_more_common(copy_list)[idx_x]
            if use_most_common:
                desired_digit = most_common
            else:
                desired_digit = '0' if most_common == '1' else '1'  # flip 0 and 1

            temp = []
            for number in copy_list:
                if number[idx_x] == desired_digit:
                    temp.append(number)
            copy_list = temp
            if len(copy_list) == 1:
                return int("".join(copy_list[0]), 2)

    def part_one(self):
        more_common = self._calculate_more_common(self.prep)
        gamma_value = int("".join(more_common), 2)
        least_common = map(lambda x: '1' if x == '0' else '0', more_common)
        epsilon_value = int("".join(least_common), 2)
        return epsilon_value * gamma_value

    def part_two(self):
        oxygen = self._helper_part_two(self.prep, use_most_common=True)
        co2 = self._helper_part_two(self.prep, use_most_common=False)
        return oxygen * co2


if __name__ == '__main__':
    day_three = Day_Three()
    print("Day Three:")
    print(f'-- Part One: {day_three.part_one()}')
    print(f'-- Part Two: {day_three.part_two()}')


