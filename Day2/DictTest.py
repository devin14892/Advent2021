import os

# def read_input(filename):
#     a_dictionary = {}
#     with open(filename):
#         for line in filename:
#             key, value = line.split()
#             print ('this is a KEY', key)
#             print ('this is a VALUE', value)
#             a_dictionary[key] = value
#             print (a_dictionary)

#     return a_dictionary

def online(input_dic):
    a_dictionary = {}
    a_file = open(input_dic, "r")
    for line in a_file:
        key, value = line.split()
        print('here is a key ',key)
        print('here is a value ',value)
        a_dictionary[key] = value


        print(a_dictionary)


def main():
    os.chdir('Day2')
    input_dic = online('DictTestinput.txt')
    #input_dic = read_input('DictTestinput.txt')
    print (input_dic)



if __name__ == '__main__':
    main()