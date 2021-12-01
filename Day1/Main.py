

def read_input(filename):
    with open(filename, 'r') as fd:
        parsed = list(fd.read())
    return parsed

def main():
    depths = read_input('input.txt')
    print (depths)


if __name__ == '__main__':
    main()
