from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_working = True

while is_working:
    choice = input(f"Welcome to our vending machine, what you would like to drink, please choose from the list below:\n{menu.get_items()}")
    if choice == "off":
        is_working = False
        break

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice) is not None:
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
            if money_machine.make_payment(menu.find_drink(choice).cost):
                coffee_maker.make_coffee(menu.find_drink(choice))
                print("Have a nice day!\n\n")
            else:
                print("What a poor man, you don't even have money to buy a drink? XD.\n\n")
        else:
            print("insufficient resources.\n\n")
    else:
        print("There's not such a drink!\n\n")






