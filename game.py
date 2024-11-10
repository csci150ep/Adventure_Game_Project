""" Interactive game where a users character has an adventure managing health and money to purchase items and fight monsters """
import random
import gamefunctions #import functions from gamefunctions used in game.py
import json

def main():

    choice = input("Would you like to (1) start a new game or (2) load a previously saved game? ")
    if choice == '2':
        game_state = gamefunctions.load_game()
        if game_state:
            player_name = game_state["player_name"]
            inventory = game_state["inventory"]
            current_money = game_state["current_money"]
            current_hp = game_state["current_hp"]
            equipped_item = game_state["equipped_item"]
        else:
            player_name = input("Please enter your name: ")
            inventory = []
            current_money = 20
            current_hp = 100
            equipped_item = None
    else:
            player_name = input("Please enter your name: ")
            inventory = []
            current_money = 20
            current_hp = 100
            equipped_item = None

    

                                                    
    gamefunctions.print_welcome(player_name)  # Prints a basic welcome message
    is_playing = True


    while is_playing: 
        print(f"\nCurrent HP: {current_hp}, Current Money: {current_money}")  # Display current stats
        print("What would you like to do?")
        print("1) Fight Monster")
        print("2) Sleep (Restore HP for 5 Money)")
        print("3) Equip Weapon")
        print("4) Go to Shop")
        print("5) Save and Quit")
        print("6) Quit without Saving")

        decision = input('Enter your decision (1-6): ')  # Prompt user to choose an action

        if decision == '1':
            monster = gamefunctions.new_random_monster() 
            current_hp = gamefunctions.fight_monster(current_hp, monster)  # Initiates fight
            if current_hp <= 0:
                is_playing = False  # Exits game if health falls below 0
        elif decision == '2':
            current_hp, current_money = gamefunctions.sleep(current_hp, current_money)  # Updates health and money with sleep function
        elif decision == '3':
            equipped_item = gamefunctions.equip_item(inventory)
            if equipped_item:
                print(f"You equipped {equipped_item['name']}.")
            else:
                print("No item equipped.")
        elif decision == '4':
            inventory, current_money = gamefunctions.shop(inventory, current_money)
        elif decision == '5':
            gamefunctions.save_game(player_name, inventory, current_money, current_hp, equipped_item)
            print("Thank you for playing!")
            is_playing = False
        elif decision == '6':
            print("Exiting without saving, thanks for playing!")
            is_playing = False
        else:
            print("Invalid entry, please choose (1-6)")


if __name__ == '__main__':
    main()
