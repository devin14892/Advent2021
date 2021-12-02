import time

def read_input(filename):
    with open(filename, 'r') as fd:
        parsed = list(fd.readlines())
        parsed = [int(i) for i in parsed]
    return parsed

def measurementComparison(depths):
    totalGreaterDepths = 0

    for depthA,depthB in zip(depths,depths[1:]):
        #print ('The depths are', depthA, "&", depthB)
        #time.sleep(2)

        if depthA < depthB:
            #print(depthA, "Is greater")
            totalGreaterDepths += 1
        else:
            #print(depthA, "Is less")
            pass  
    return totalGreaterDepths


def main():
    depths = read_input('input.txt')
    #print(depths[0:4])
    print ("The total greater depths is", measurementComparison(depths))


if __name__ == '__main__':
    main()
