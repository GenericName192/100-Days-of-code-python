totalCost = float(input("How much is the total bill? $"))
tipPercent = int(input("What percent would you like to tip? "))
numberOfPeople = int(input("How many people are splitting the bill? "))

tipAsNumber = tipPercent / 100 + 1
totalBill = totalCost * tipAsNumber
costPerPerson = round(totalBill / numberOfPeople, 2)
costPerPerson = "{:.2f}".format(costPerPerson)
print(f"Each person should pay: {costPerPerson}")