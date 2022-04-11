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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def resource_sufficiet(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    Total = int(input("Enter no of quarters")) * 0.25
    Total += int(input("Enter no of dimes")) * 0.1
    Total += int(input("Enter no of nickles")) * 0.05
    Total += int(input("Enter no of pennies")) * 0.01
    return round(Total, 2)


# pc=process_coins()
# rate=MENU[choice]['cost']
def transaction_successful(pc, rate):
    # pc=process_coins()
    rate = MENU[choice]['cost']
    if pc >= rate:
        change = pc - rate
        print(f" The remaing change is {change}")
        global profit
        profit += rate
        return True
    else:
        print(f"There is no enough money")
        return False


def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice}. Enjoy!")


# end_game=True
# while end_game:
#     choice=input(' What would you like? (espresso/latte/cappuccino):').lower()
#     if choice=="off":
#         end_game=False
#     elif choice=="report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${round(profit,2)}")

#     else:
#         drink = MENU[choice]
#         ingredients=MENU[choice]['ingredients']
#         if resource_sufficiet(ingredients)==True:
#             pc=process_coins()
#             if transaction_successful(pc,drink['cost'])==True:
#                 make_coffee(ingredients)

is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_sufficiet(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredients"])




