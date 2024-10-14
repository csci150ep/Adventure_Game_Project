#gamefunctions.py
#Eric Pratt
#10/6/2024

#purchase_item displays how many items purchased and quantity of money remaing.
#new_random_monster, dictionary for a class of monster, returning health, power, and money for 3
#different named monsters.

import random



def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """
Takes and item price and starting money as float integers, and a quantity to purchase as an integer
and returns number of items bought and the remaining money
"""
    # Calculate how many items can be purchased
    max_items = int(startingMoney // itemPrice)
    
    # Determine the actual quantity that can be purchased
    items_bought = min(max_items, quantityToPurchase)
    
    # Calculate the remaining money after the purchase
    remaining_money = startingMoney - (items_bought * itemPrice)
    
    # Return the number of items bought and the remaining money
    return items_bought, remaining_money


def new_random_monster():
    """
Calls a random monster from a list of defined monsters from keys, and returns characteristics about
the monster including name, description, health range, and money range
"""    
    monsters = {
        'Ogre': {
            'description': 'This is a large and hideous being resembling a man which eats ordinary humans, especially fond of children',
            'health_range': (70, 100),
            'power_range': (10, 20),
            'money_range': (5.0, 15.0)
        },
        'Griffin': {
            'description': 'creature with the body, tail, and back legs of a lion, and the head and wings of an eagle',
            'health_range': (30, 60),
            'power_range': (15, 45),
            'money_range': (2.0, 10.0)
        },
        'Gnome': {
            'description': 'small human like creature with mystical power, cheerful guardian of flora and fauna',
            'health_range': (5, 15),
            'power_range': (30, 70),
            'money_range': (20.0, 40.0)
        }
    }     
    monster_name = random.choice(list(monsters.keys())) #randomly choose monster from list
    monster_info = monsters[monster_name]
    health = random.randint(*monster_info['health_range']) #randomly choose monster health and power
    power = random.randint(*monster_info['power_range']) 
    money = round(random.uniform(*monster_info['money_range']), 2) #radomly choose money as float
    monster = {
        'name': monster_name,
        'description': monster_info['description'],
        'health': health,
        'power': power,
        'money': money
    }
    return monster

def print_welcome(name: str, width: int=20): #creates welcome message centered at width 20(can be changed)
    """
Welcome Message creates a welcome message centered at width that can be adjusted
"""    
    message = f'Hello, {name}!'
    print(f'{message.center(width)}')


def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
Prints a sign that contains a list of two items and their corresponding prices
"""    
    item1Listing = f'{item1Name:<12}${item1Price:>7.2f}' #create listing name to the right and price to the left
    item2Listing = f'{item2Name:<12}${item2Price:>7.2f}'
    print('/-----------------------\\')
    print(f'| {item1Listing} |')
    print(f'| {item2Listing} |')
    print('\\-----------------------/')

#running each function 3 times to display functionality
print('---purchase_item---')
print('number purchased and leftover money for 2.25 price, 11 starting money, 2 quantity')
num_purchased, leftover_money = purchase_item(2.25, 11, 2)
print(num_purchased)
print(leftover_money)

print('number purchased and leftover money for 1.75 price, 8 starting money, 3 quantity')
num_purchased, leftover_money = purchase_item(1.75, 8, 3)    
print(num_purchased)
print(leftover_money)

print('number purchased and leftover money for 3.10 price, 9 starting money, 2 quantity')
num_purchased, leftover_money = purchase_item(3.10, 9, 2)
print(num_purchased)
print(leftover_money)

print('---random_monster---')
for _ in range(3):
    monster = new_random_monster()
    print(f"Monster: {monster['name']}")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}, Power: {monster['power']}, Money: ${monster['money']}")

print('---print_welcome---')
print_welcome('Jeff')
print_welcome('Eric')
print_welcome('Baxter')

print('---print_shop_menu---')
print_shop_menu('Banana', 2.00, 'Apple', 0.99)
print_shop_menu('Bread', 4.00, 'Milk', 5.50)
print_shop_menu('Cereal', 5.25, 'Butter', 2.25)

