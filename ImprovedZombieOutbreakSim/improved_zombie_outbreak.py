def get_valid_infection_rate():
    while True:
        try:
            rate = float(input("Enter the daily infection rate (in %): " ))

            if rate < 0:
                print("Infection rate cannot be negative. Please re-enter your number.")
            else:
                return rate
        except ValueError:
                print("Invalid input. Please enter a valid number.")

def get_valid_initial_infected():
    while True:
        try:
            initial = float(input("Enter the initial number of infected (Day 0): "))

            if initial < 0:
                print("Initial number cannot be negative. Please enter another number.")
            else:
                return initial
        except ValueError:
                print("Invalid input. Please enter a valid number.")

def get_valid_num_days():
    while True:
        try:
            numDays = float(input("Enter the number of days to simulate: "))

            if numDays <=0:
                print("Number of days must be greater than 0. Please try again.")
            else:
                return numDays
        except ValueError:
                print("Invalid input. Please enter a valid number.")


def run_sim():

    initial = get_valid_initial_infected()
    rate = get_valid_infection_rate()
    days = get_valid_num_days()

    percentage = rate / 100

    expGrowthFormula = initial * ((1 + percentage) ** days)

    finalNumInfected = round(expGrowthFormula)
    
    print("After " + str(round(days)) + " days, the total number of infected is approximately " + str(finalNumInfected) + ".")


def main():
    print("This is the Improved Zombie Outbreak Simulator!")

    while True:
        run_sim()

        playAgain = input("Would you like to perform another simulation? (y/n)")

        if playAgain != 'y':
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()


