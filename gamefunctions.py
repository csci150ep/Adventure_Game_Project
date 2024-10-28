"""Module for gamefunctions.

Game functions including print_welcome which prints a welcome message, print_shop_menu which displays
a menu for 2 items with prices, purchase_item which returns number of items purchased and remaining
funds from a starting bankroll, and random_monster which allocates attribute values for a monster chosen
from a list."""

import random


def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """
Takes and item price and starting money as float integers, and a quantity to purchase as an integer
and returns number of items bought and the remaining money

Parameters:
    itemPrice and startingMoney (float): the cost of the item and available funds
    quantityToPurchase (int): number of items desired to be purchased
Returns:
    the number of items bought and the money that is remaining 
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

Parameters:
    Monster name from list
Returns
    Random attributes within a range for the chosen monster
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

Parameters:
    name (str)
Returns welcome message for the user input (str)
"""    
    message = f'Hello, {name}!'
    print(f'{message.center(width)}')


def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
Prints a sign that contains a list of two items and their corresponding prices

Parameters:
    items (str)
    prices (float)
Returns both items and prices centered on a bordered menu
"""    
    item1Listing = f'{item1Name:<12}${item1Price:>7.2f}' #create listing name to the right and price to the left
    item2Listing = f'{item2Name:<12}${item2Price:>7.2f}'
    print('/-----------------------\\')
    print(f'| {item1Listing} |')
    print(f'| {item2Listing} |')
    print('\\-----------------------/')


def test_functions():
    """
Function to test all the game functions
"""
    print_welcome('Jeff', width=20)
    print_shop_menu('Bagel', 4.99, 'Utensils', 11.00)
    items_bought, remaining_money = purchase_item(4.0, 20.0, 3)
    print(f'Items bought: {items_bought}, Remaining money: ${remaining_money:.2f}')
    monster = new_random_monster()
    print(f"Monster: {monster['name']}, Description: {monster['description']}, "
          f"Health: {monster['health']}, Power: {monster['power']}, Money: ${monster['money']}")
    
if __name__=='__main__':   #Ensure test_functions() runs only if the script is executed from main
    test_functions()


def fight_monster(current_hp, monster):
    """
interactive fight with user and random monster
"""
    monster_hp = monster['health']
    print(f"\nA {monster['name']}!")
    print(f"Description: {monster['description']}")
    print(f"Monster HP: {monster_hp}, Power: {monster['power']}")

    while current_hp > 0 and monster_hp > 0:
        player_dmg = random.randint(10, 50) #player damage dealt set arbitrarily
        
        monster_dmg = monster['power']
        monster_hp -= player_dmg
        
        print(f"You dealt {player_dmg} damage to the {monster['name']}")
              
        current_hp -= monster_dmg
              
        print(f"The {monster['name']} dealt {monster_dmg} damage to you")
              
        if monster_hp <= 0:
              print(f"You defeated the {monster['name']}!")
              return current_hp
            
        elif current_hp <= 0:
            return current_hp

        choice = input("Do you want to continue to fight (1) or run (2)? ")
        if choice != '1':
            print("You ran away")
            return current_hp

    return current_hp #return the remaing health of player



def sleep(current_hp, current_money):
    """
restores health if funds are available
"""
    if current_money >= 5:
        current_hp += 20 # restores some health if enough funds are available
        current_money -= 5
        print("You have rested and restored 20 HP")
    else:
        print("You do not have enough money to rest in the tavern")
    return current_hp, current_money

if __name__=='__main__':   #Ensure script is executed from main
    main()

        
def main():
    player_name = input('Please enter your name: ')
    gamefunctions.print_welcome(player_name)  # Prints a basic welcome message
    current_hp = 100  # Starts the player's health at 100
    current_money = 20  # Player's starting money
    is_playing = True  # When is_playing is False, the game ends

    while is_playing: 
        print(f"\nCurrent HP: {current_hp}, Current Money: {current_money}")  # Display current stats
        print("What would you like to do?")
        print("1) Fight Monster")
        print("2) Sleep (Restore HP for 5 Money)")
        print("3) Quit")

        decision = input('Enter your decision (1-3): ')  # Prompt user to choose an action

        if decision == '1':
            monster = gamefunctions.new_random_monster() 
            current_hp = fight_monster(current_hp, monster)  # Initiates fight
            if current_hp <= 0:
                is_playing = False  # Exits game if health falls below 0
        elif decision == '2':
            current_hp, current_money = sleep(current_hp, current_money)  # Updates health and money with sleep function
        elif decision == '3':
            print('Thank you for playing!')
            is_playing = False  # Exits the game
        else:
            print("Invalid entry, please choose (1-3)")

if __name__ == '__main__':
    main()       
        
