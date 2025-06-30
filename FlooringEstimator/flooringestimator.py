import math

def get_positive_number(prompt):
    while True:
        try:
            num = float(input(prompt))

            if num <= 0:
                print("The number must be greater than 0. Please enter another number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please try again")

def get_non_negative_number(prompt):
    while True:
        try:
            num = float(input(prompt))

            if num < 0:
                print("Number must be greater than or equal to 0. Please enter another number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please try again.")



def main():
    while True:
        print("\nFlooring Estimator Challenge\n")

        length = get_positive_number("Enter length of room (ft): ")
        width = get_positive_number("Enter width of room (ft): ")
        price = get_non_negative_number("Enter the price ber box of tile: ")
        laborRate = get_non_negative_number("Enter labor rate per hour: ")

        area = length * width
        numBoxes = math.ceil(area / 25)
        laborHours = round(((area / 50) * 1.5), 1)
        tileCost = numBoxes * price
        laborCost = laborHours * laborRate
        total = tileCost + laborCost

        print(f"/nBoxes of tiles required: {numBoxes}")
        print(f"Hours of labor required: {laborHours}")
        print(f"Cost of tiles: ${tileCost:.2f}")
        print(f"Labor charges: ${laborCost:.2f}")
        print(f"Total cost: ${total:.2f}\n")

        repeat = input("Would you like to perform another estimate? (y/n): ")
        if repeat.lower() != 'y':
            break

if __name__=="__main__":
    main()
