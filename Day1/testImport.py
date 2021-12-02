def read_input(filename):
    with open(filename, 'r') as fd:
        parsed = list(fd.readlines())
        parsed = [int(i) for i in parsed]
    return parsed

numberse = read_input("input.txt")
print(type(numberse[0]))
print(numberse[0:4])