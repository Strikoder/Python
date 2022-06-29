from random import randint
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
    "water": randint(300,600),
    "milk": randint(200,400),
    "coffee": randint(100,250),
}

available_money = randint(50,200)



while True:
    choice = input("\nGood morning, tell me what do you want to drink, please!\nOur today's menu: espresso, latte, cappuccino\n  ").lower()
    if choice == "report":
        print(resources, f"and you have {available_money}$")
    elif choice == "off":
        print("The machine is turned off.")
        break
    else:
        pennies = int(input("Insert the number of pennies please: \n"))
        nickles = int(input("Insert the number of nickles please: \n"))
        dimes = int(input("Insert the number of dimes please: \n"))
        quarters = int(input("Insert the number of quarters please: \n"))
        total = 0.01*pennies+nickles*0.05+dimes*0.10+quarters*0.25
        money_change=0

        if choice == "espresso":
            if resources["water"] >= MENU[choice]["ingredients"]["water"] and resources["coffee"] >= MENU[choice]["ingredients"]["coffee"] and total >= MENU[choice]["cost"]:
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                money_change = total-MENU[choice]["cost"]
                available_money += MENU[choice]["cost"]
                print(f"Here is your {choice}, and here is your change {round(money_change,2)}")

            elif total < MENU[choice]["cost"]:
                print("Sorry, you don't have enough money to buy this. Money refunded")

            else:
                print("Insufficient resources, sorry for the inconvenience.\n")
                if resources["water"] < MENU[choice]["ingredients"]["water"]:
                    print("There isn't enough water.")
                else:
                    print("There isn't enough coffee.")

        elif choice == "latte":
            if resources["water"] >= MENU[choice]["ingredients"]["water"] and resources["coffee"] >= MENU[choice]["ingredients"]["coffee"] and resources["milk"] >= MENU[choice]["ingredients"]["milk"] and total >= MENU[choice]["cost"] :
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                money_change = total - MENU[choice]["cost"]
                available_money += MENU[choice]["cost"]
                print(f"Here is your {choice}, and here is your change {round(money_change,2)}")

            elif total < MENU[choice]["cost"]:
                print("Sorry, you don't have enough money to buy this. Money refunded")

            else:
                print("Insufficient resources, sorry for the inconvenience.\n")
                if resources["water"] < MENU[choice]["ingredients"]["water"]:
                    print("There isn't enough water.")
                elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
                    print("There isn't enough milk.")
                else:
                    print("There isn't enough coffee.")

        elif choice == "cappuccino":
            if resources["water"] >= MENU[choice]["ingredients"]["water"] and resources["coffee"] >= MENU[choice]["ingredients"]["coffee"] and resources["milk"] >= MENU[choice]["ingredients"]["milk"] and total >= MENU[choice]["cost"] :
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                money_change = total - MENU[choice]["cost"]
                available_money += MENU[choice]["cost"]
                print(f"Here is your {choice}, and here is your change {round(money_change,2)}")

            elif total < MENU[choice]["cost"]:
                print("Sorry, you don't have enough money to buy this. Money refunded")

            else:
                print("Insufficient resources, sorry for the inconvenience.\n")
                if resources["water"] < MENU[choice]["ingredients"]["water"]:
                    print("There isn't enough water.")
                elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
                    print("There isn't enough milk.")
                else:
                    print("There isn't enough coffee.")

        if resources["water"] < MENU["espresso"]["ingredients"]["water"] and resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, we are out of resources!")
            break
