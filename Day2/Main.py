

def ReadFile(fileName):
    with open(fileName,'r') as f:
            courseData = f.read().split()
    return courseData


def justNumbers(courseData):
    lenght = len(courseData)
    courseNum = courseData[1:lenght:2]
    courseNumbers = [int(item) for item in courseNum]
    return tuple(courseNumbers)
    

def justDirection(courseData):
    lenght = len(courseData)
    courseDirection = courseData[0:lenght:2]
    return tuple(courseDirection)


def listofTuples(direction, numbers):
    merge_list = [(direction[i],numbers[i]) for i in range(0, len(direction))]
    return merge_list


def Solution1(merge_list):
    hor = 0
    vir = 0

    for command, value in merge_list:
        if command == 'down':
            vir += value
        elif command == 'up':
            vir -= value
        elif command == 'forward':
            hor += value
    Awn = hor * vir
    return Awn


def main():
    inputFile = 'input.txt' 
    courseData = ReadFile(inputFile)
    numbers =  justNumbers(courseData)
    direction = justDirection(courseData)
    sortedData = listofTuples(direction, numbers)
    result = Solution1(sortedData)

    #print('course data\n', courseData)
    #print('seperated', "\nNumbers",numbers, "\nDirection ",direction)
    #print('\nlist o tups', sortedData)
    print("\n THIS SHOULD BE IT", result)


if __name__=='__main__':
    main()
































