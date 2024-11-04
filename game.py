""" Interactive game where a users character has an adventure managing health and money to purchase items and fight monsters """
import random
import gamefunctions #import functions from gamefunctions used in game.py

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
            gamefunctions.shop(inventory, current_money)
        elif decision == '5':
            print("Thank you for playing!")
            is_playing = False
        else:
            print("Invalid entry, please choose (1-5)")


if __name__ == '__main__':
    main()
