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
