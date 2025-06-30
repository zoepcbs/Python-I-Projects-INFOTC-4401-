def make_number_list(fileName):
    numList = []
    file = None

    try:
        file = open(fileName, 'r')

        for i in file:
            numList.append(int(i))
    except Exceptopn as error:
        print(error)
    finally:
        if(file != None):
            file.close()
            
    return numList

def display_list(num, fileName):
    
    print("List of random numbers in", fileName)

    for i in num:
        print(i)
    print("\nRandom number count:", len(num))


def main():
    fileName = 'randomnum.txt'
    numList = make_number_list(fileName)
    display_list(numList, fileName)

main()
