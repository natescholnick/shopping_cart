import os

# The call stack goes multiList >> shoppingCart >> displayCart

cart = {}
op = ''

def multiList(shopping = True):
    '''
    This outer function will navigate multiple lists (dictionary values).
    Once a list is selected (a dictionary key), it will run shoppingCart with that list.
    The list items are tuples of the form (item, quantity).
    '''
    while shopping:
        os.system('cls' if os.name == 'nt' else 'clear')
        if cart != {}:
            print('Here are all your current shopping lists:\n')
            viewAllLists()
        current_list = input("Enter the name of a list you'd like to create or edit, or 'QUIT' to leave. ").lower()

        if current_list == 'quit':
            shopping = False
            continue

        elif current_list not in cart:
            cart[current_list] = []

        shoppingCart(current_list, op)


def shoppingCart(current_list, op):
    while op != 'switch':
        os.system('cls' if os.name == 'nt' else 'clear')
        displayCart(current_list, cart[current_list])
        op = input("What would you like to do? ('ADD' item, 'REMOVE' item, or 'SWITCH' lists) ").lower()

        if op == 'switch':
            displayCart(current_list, cart[current_list])
            continue

        elif op == 'add':
            addItem(current_list)

        elif op == 'remove':
            removeItem(current_list)

        else:
            displayCart(current_list, cart[current_list])
            print("I'm sorry. Your request was not recognized. ")


def addItem(current_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    displayCart(current_list, cart[current_list])
    item = input('Which item would you like to get? ').title()
    quantity = int(input(f'How many {item} will you be getting? '))
    cart[current_list].append((item, quantity))

def removeItem(current_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    displayCart(current_list, cart[current_list])
    item = input('Which item would you like to remove? ').title()
    item_names = [x[0] for x in cart[current_list]]
    if item not in item_names:
        print(f'You had no {item} on the list. ')
    else:
        quantity = int(input(f'How many {item} would you like to remove? '))
        if quantity > cart[current_list][item_names.index(item)][1]:
            print(f'There aren\'t that many {item} on the list.')
        elif quantity == cart[current_list][item_names.index(item)][1]:
            cart[current_list].pop(item_names.index(item))
        else:
            # Overwriting the tuple with the updated quantity: tuple = (tuple[0], tuple[1] - quantity)
            cart[current_list][item_names.index(item)] = (item, cart[current_list][item_names.index(item)][1] - quantity)


def viewAllLists():
    for k, v in cart.items():
        displayCart(k,v)
        print('\n')

# How the cart will be displayed

def displayCart(list_name, item_list):
    if item_list == []:
        print("The cart is empty right now.")
    else:
        list_title = list_name.upper() + ' LIST'
        print('{:^40}'.format( list_title))
        print('=' * 40)
        print('{:^15}{:10}{:^15}'.format("ITEM", " ", "QUANTITY"))
        print('\u2014'*40)
        for item in item_list:
            print('{:<19}{:>19}'.format(item[0], item[1]))

multiList()
