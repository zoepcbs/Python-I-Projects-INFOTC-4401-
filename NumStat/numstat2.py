def make_list_from_file(fileName):
    list = []

    with open(fileName, 'r') as file:
        numbers = file.readlines()

        for i in numbers:
            list.append(int(i))

    return list

def calc_median(numList):
    
    sortedList = numList.copy()
    sortedList.sort()

    count = len(sortedList)

    if count == 0:
        return None

    if count % 2 == 1: # odd length
        return sortedList[count // 2]

    else: # even length
        midRight = count // 2
        midLeft = midRight - 1
        result = (sortedList[midLeft] + sortedList[midRight]) / 2
        return result

def calc_mode(numList):
    if not numList:
        return None

    numCounts = {}

    for num in numList:
        if num in numCounts:
            numCounts[num] += 1
        else:
            numCounts[num] = 1

    maxCount = 0

    for num in numCounts:
        count = numCounts[num]

        if count > maxCount:
            maxCount = count

    modes = []

    for num in numCounts:
        if numCounts[num] == maxCount:
            modes.append(num)

    return modes

def display_info(fileName):
    numList = make_list_from_file(fileName)
    
    if not numList:
        print(f"There are no numbers in {fileName}")
        return

    total = sum(numList)
    count = len(numList)
    average = total / count
    maximum = max(numList)
    minimum = min(numList)
    numRange = maximum - minimum
    median = calc_median(numList)
    mode = calc_mode(numList)

    print("File name:", fileName)
    print("Sum:", total)
    print("Count:", count)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Range:", numRange)
    print("Median:", median)
    print("Mode:", mode)

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
