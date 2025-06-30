def make_list_from_file(fileName):
    list = []

    with open(fileName, 'r') as file:
        numbers = file.readlines()

        for i in numbers:
            list.append(int(i))

    return list

def display_info(fileName):
    numList= []

    try:
        numList = make_list_from_file(fileName)
    except Exception as error:
        print(error)
        return

    total = sum(numList)
    count = len(numList)
    average = total / count
    maximum = max(numList)
    minimum = min(numList)
    numRange = maximum - minimum

    print("File name:", fileName)
    print("Sum:", total)
    print("Count:", count)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Range:", numRange)
    

def main():
    while True:
        fileName = input("Enter file name here: ")
        display_info(fileName)
        repeat = input("Would you like to evaluate another file? (y/n): ")

        if (repeat != 'y'):
            break
        else:
            print("\n")

main()
