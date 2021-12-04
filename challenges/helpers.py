import os

def read_input(filename, *, parse_int=False):
    lines = []
    workdir = os.getcwd()
    if "challenges" in workdir:
        workdir = "/".join(workdir.split("/")[:-1])  # get base path of project

    print("workdir: ", workdir)
    with open(os.path.join(workdir, "inputs", filename)) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line) if parse_int else line)
    return lines



'''
 for i in range(len_x):
        more_common = (abs_one_value[i] > len_y / 2) * 1  # Either 1 or 0
        temp = []  # new indices - will later be stored into possible indices
        for j in possible_indices:
            if j == 67:
                print(f"comparing 67: {more_common} & {flipped[i][j]}", type(str(more_common)), type(flipped[i][j]), str(more_common) == flipped[i][j])
            char = flipped[i][j]
            if char == str(more_common):
                if(len(possible_indices) < 10):
                    print("Debgu")
                temp.append(j)
        possible_indices = temp
        if len(possible_indices) == 1:
            print(possible_indices)
            oxygen_generator_value = "Yay"
            print(puzzle_input[67])  # This should be the value, or if they are cut off both of them seem fine
            print(puzzle_input[449])'''