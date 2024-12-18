"""Module for gamefunctions.

Game functions including print_welcome which prints a welcome message, print_shop_menu which displays
a menu for 2 items with prices, purchase_item which returns number of items purchased and remaining
funds from a starting bankroll, and random_monster which allocates attribute values for a monster chosen
from a list."""

import random
import json

def save_game(player_name, inventory, current_money, current_hp, equipped_item, filename = "savegame.json"):
    """Saves the game state to a JSON file."""
    game_state = {
        "player_name": player_name,
        "inventory": inventory,
        "current_money": current_money,
        "current_hp": current_hp,
        "equipped_item": equipped_item
    }
    with open(filename, 'w') as file:
        json.dump(game_state, file)
    print(f"Game saved successfully to {filename}.")

def load_game(filename="savegame.json"):
    """Loads the game state from a JSON file."""
    try:
        with open(filename, 'r') as file:
            game_state = json.load(file)
        print(f"Game loaded successfully from {filename}.")
        return game_state
    except FileNotFoundError:
        print(f"No save file found at {filename}. Starting a new game.")
        return None
    


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



def print_shop_menu(shop_items):
    """
Prints a sign that contains a list of two items and their corresponding prices

Parameters:
    items (str)
    prices (float)
Returns both items and prices centered on a bordered menu
"""
    print('/-----------------------\\')
    for item in shop_items:
        print(f"| {item['name']:<12} ${item['price']:>7.2f} |")
    print('\\-----------------------/')



def test_functions():
    """
Function to test all the game functions
"""
    print_welcome('Jeff', width=20)
    print_shop_menu([{'name': 'Bagel', 'price': 4.99}, {'name': 'Utensils', 'price': 11.00}])
    items_bought, remaining_money = purchase_item(4.0, 20.0, 3)
    print(f'Items bought: {items_bought}, Remaining money: ${remaining_money:.2f}')
    monster = new_random_monster()
    print(f"Monster: {monster['name']}, Description: {monster['description']}, "
          f"Health: {monster['health']}, Power: {monster['power']}, Money: ${monster['money']}")


def fight_monster(current_hp, monster, equipped_item=None):
    """
interactive fight with user and random monster
"""
    monster_hp = monster['health']
    print(f"\nA {monster['name']}!")
    print(f"Description: {monster['description']}")
    print(f"Monster HP: {monster_hp}, Power: {monster['power']}")

    while current_hp > 0 and monster_hp > 0:
        player_dmg = random.randint(10, 50) if equipped_item is None else random.randint(10, 50) + (equipped_item.get('power', 0)) #player damage dealt set arbitrarily

        if equipped_item and equipped_item['currentDurability'] > 0:
            equipped_item['currentDurability'] -= 1
        else:
            equipped_item = None

        monster_hp -= player_dmg
        print(f"You dealt {player_dmg} damage to the {monster['name']}")

        current_hp -= monster['power']
        print(f"The {monster['name']} dealt {monster['power']} damage to you.")
              
        if monster_hp <= 0:
              print(f"You defeated the {monster['name']}!")
              return current_hp   
        elif current_hp <= 0:
            print("You have been slain!")
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

def equip_item(inventory):
    print("Available weapons to equip:")
    for idx, item in enumerate(inventory):
        if item['type'] == 'weapon' and item['currentDurability'] > 0:
            print(f"{idx + 1}: {item['name']} (Durability: {item['currentDurability']}")
    choice = input("Select an item to equip (number) or '0' to cancel: ")
    if choice.isdigit() and 1 <= int(choice) <= len(inventory):
        return inventory[int(choice) - 1]
    return None

    
def shop(inventory, current_money):
    shop_items = [
        {"name": "sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10, "price": 15.00},
        {"name": "buckler", "type": "shield", "maxDurability": 6, "currentDurability": 6, "price": 10.00},
        {"name": "potion", "type": "consumable", "note": "restores hp", "price": 5.00}
    ]

    print_shop_menu(shop_items)

    item_name = input("Enter the name of the item you wish to buy: ").strip().lower()
    quantity = int(input("How many would you like to buy?").strip())

    item_found = False #check to see if item was found in shop


    for item in shop_items:
        if item['name'].lower() == item_name:
            total_cost = item['price'] * quantity
            if current_money >= total_cost:
                current_money -= total_cost
                inventory.append({**item, 'quantity': quantity}) #add item to inventory for quantity purchased
                print(f"You purchased {quantity} {item_name}(s).")
                item_found = True
            else:
                print("You do not have enough money.")
            break
    if not item_found:
        print("Item not found in shop.")
    return inventory, current_money
        
        
def main():
    player_name = input('Please enter your name: ')
    gamefunctions.print_welcome(player_name)  # Prints a basic welcome message
    current_hp = 100  # Starts the player's health at 100
    current_money = 20  # Player's starting money
    is_playing = True  # When is_playing is False, the game ends

    inventory = [] #initialize initial empty inventory
    equipped_item = None

    while is_playing: 
        print(f"\nCurrent HP: {current_hp}, Current Money: {current_money}")  # Display current stats
        print("What would you like to do?")
        print("1) Fight Monster")
        print("2) Sleep (Restore HP for 5 Money)")
        print("3) Equip Weapon")
        print("4) Go to Shop")
        print("5) Quit")

        decision = input('Enter your decision (1-5): ')  # Prompt user to choose an action

        if decision == '1':
            monster = gamefunctions.new_random_monster() 
            current_hp = fight_monster(current_hp, monster)  # Initiates fight
            if current_hp <= 0:
                is_playing = False  # Exits game if health falls below 0
        elif decision == '2':
            current_hp, current_money = sleep(current_hp, current_money)  # Updates health and money with sleep function
        elif decision == '3':
            equipped_item = gamefunctions.equip_item(inventory)
            if equipped_item:
                print(f"You equipped {equipped_item['name']}.")
            else:
                print("No item equipped.")
        elif decision == '4':
            inventory, current_money = gamefunctions.shop(inventory, current_money)
        elif decision == '5':
            print("Thank you for playing!")
            is_playing = False
        else:
            print("Invalid entry, please choose (1-5)")


if __name__ == '__main__':
    main()       
        
