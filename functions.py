def readfile(filename="input.txt", sep="\n"):
    with open(filename, 'r') as f:
        contents = f.read().split(sep=sep)
    return contents