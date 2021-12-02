list = [5, 10,15,4]

def compare(list):
    for x, y in zip(list,list[1:]):
        print(x, "compared to", y)
        if x > y:
            print (x , "is bigger")
        else:
            print(y, "is bigger")
    return

results = compare(list)
print (results)