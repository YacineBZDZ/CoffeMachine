MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machineWork = True
Money = 0

# TODO 4 : check the resources sufficient
def checkresource(choice):
    global ThreIsIngredients
    menu = MENU[choice]["ingredients"]
    for item in menu:
        if resources[item] < menu[item]:
            print(f"sorry there isn't enough {item}.")
            ThreIsIngredients = False
        else:
            ThreIsIngredients = True


# TODO 5 :  Process coins
def chekcoins(choice):
    global Money
    global noCoins
    cost = MENU[choice]["cost"]
    """This function have the mission to check coins"""
    print("please isert Coins ")
    quaters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    """ Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01"""
    total = quaters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    # TODO 6 :  Check transaction successful?
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        noCoins = True
    else:
        total -= cost
        print(f"Here is {total} in change.")
        Money += cost
        noCoins = False


# TODO 7 :  Make Coffee.
def makingCofee(choice):
    """this function recalculate the new resources that there is"""
    menu = MENU[choice]["ingredients"]
    for item in menu:
        resources[item] -= menu[item]
    print("Here is your cappuccino ☕️. Enjoy!")
def game():
    global machineWork
    global Money
    global noIngredients
    # TODO 1 : Asking the User what type of drink to take:
    userChoice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 3 : print report when user enter "report"
    if userChoice == "report":
        print(f"Water: {resources["water"]} \nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]} \nMoney: {Money} ")
    # TODO 2 : Turn off the Coffe Machine By entering "off" put it withe loop
    elif userChoice == "off":
        machineWork = False
    else:
      checkresource(userChoice)
      if(ThreIsIngredients):
       chekcoins(userChoice)
      if(not noCoins):
       makingCofee(userChoice)


while(machineWork):
    ThreIsIngredients = True
    noCoins = True
    game()
