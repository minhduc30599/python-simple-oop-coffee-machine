from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_items = Menu()
ingredients_resources = CoffeeMaker()
money_resources = MoneyMachine()
is_on = True

while is_on:
    order = input(f'What would you like? ({menu_items.get_items()})')
    if order == 'off':
        is_on = False
    elif order == 'report':
        ingredients_resources.report()
        money_resources.report()
    else:
        drink = menu_items.find_drink(order)
        if ingredients_resources.is_resource_sufficient(drink) and money_resources.make_payment(drink.cost):
                ingredients_resources.make_coffee(drink)
