from data import MENU, resources, COINVAULE
import os
os.system("cls")


def coffeeMachine():
    running = True
    while running:
        print("Welcome to Davids Coffee Machine! \n")
        order = input("What would you like to order? (espresso), (latte) or (cappuccino) \n").lower()
        if order == "off":
            running = False
        elif order == "report":
            printReport()
        elif order in MENU:
            order = MENU[order]
            if enoughResources(order):
                print(f"That will be: {order['cost']}")
                moneyIn = 0
                for coin in COINVAULE:
                    moneyIn += countCoins(coin, int(input(f"How many {coin}s do you want to put in \n")))
                if moneyIn < order["cost"]:
                    print(f"Sorry but the total value of your coins {moneyIn} is less then the cost of the drink {order['cost']}")
                else:
                    reduceResources(MENU[order])
                    change = round(moneyIn - order['cost'], 2)
                    resources["money"] += order['cost']
                    print(f"Thank you for your order, that is ${change} change.")
            else:
                print("Sorry there are not enough resources to make that drink :( \n")
        else:
            print("Sorry, we didnt quite catch that, please try again")


def printReport():
    print(f'Water: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]} \nProfit: {resources["money"]} \n')


def countCoins(coinType, coinCount):
    return COINVAULE[coinType] * coinCount


def reduceResources(drink):
    global resources
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]


def enoughResources(drink):
    global resources
    for ingredient, amountUsed in drink["ingredients"].items():
        if resources[ingredient] < amountUsed:
            return False
    return True

coffeeMachine()

