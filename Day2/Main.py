import os

def read_input(filename):
    a_dictionary = {}
    with open(filename, 'r') as fd:
        for line in fd:
            print (a_dictionary)
            key, value = line.split()
            a_dictionary[key] = value
    return a_dictionary


def main():
    os.chdir('Day2')
    input_dic = read_input('input.txt')
    print (input_dic)



if __name__ == '__main__':
    main()
