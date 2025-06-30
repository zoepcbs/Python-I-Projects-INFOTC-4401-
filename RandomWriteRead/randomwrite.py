import random

def get_positive_number(prompt):
    while True:
        num = None

        try:
            num = int(input(prompt))

            if (num <= 0):
                print("The number must be positive.")
                continue
        except:
            print("Invalid input. The number must be positive.")
            continue
        else:
            break

    return num

def write_random_numbers(fileName, quantity, lowerBound, upperBound):

    file = None

    try:
        file = open(fileName, "w")

        for i in range(quantity):
            randomNum = random.randint(lowerBound, upperBound)
            file.write(str(randomNum))
            file.write('\n')
        print("The random numbers were written to", fileName)
    except:
        print("An error occured.")
    finally:
        if (file != None):
            file.close()

def main():
    fileName = 'randomnum.txt'
    quantity = get_positive_number("How many random numbers do you want? ")
    lowerBound = get_positive_number("What is the lowest the random number should be? ")
    upperBound = get_positive_number("What is the highest the random number should be? ")

    write_random_numbers(fileName, quantity, lowerBound, upperBound)

main()
