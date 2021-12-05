
def read_input(filename):
    a_dictionary = {}
    with open(filename, 'r') as fd:
        for line in fd:
            key, value = line.split()
            a_dictionary[key] = value
    return a_dictionary


def main():
    print(read_input('input.txt'))



if __name__ == '__main__':
    main()