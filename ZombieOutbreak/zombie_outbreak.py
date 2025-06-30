# user inputs: initial infected (day 0), daily infection rate (%), number of simulation days

initial = float(input("Enter the initial number of infected (Day 0): "))
rate = float(input("Enter the daily infection rate (in %): " ))
numDays = float(input("Enter the number of days to simulate: "))

# test code to check user input is collected correctly
# print(initial,rate,numDays)

# converting daily rate to a decimal for the formula
percentage = rate / 100

expGrowthFormula = initial * ((1 + percentage) ** numDays)

# rounding to nearest whole number
finalNumInfected = round(expGrowthFormula)

# concatenating to make an output statement
print("After " + str(round(numDays)) + " days, the total number of infected is approximately " + str(finalNumInfected) + ".")
