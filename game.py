""" Interactive game where a users character has an adventure managing health and money to purchase items and fight monsters """
import random
import gamefunctions #import functions from gamefunctions used in game.py

def main():
    player_name = input('Please enter your name: ')
    gamefunctions.print_welcome(player_name) #prints a basic welcome message
    current_hp = 100 #starts the players health at 100
    current_money = 20 #players starting with an arbitrary amount of money set to 20
    is_playing = True #when is playing is false the game ends
    while is_playing: 
        print(f"\nCurrent HP: {current_hp}, Current Money: {current_money}") #Display current stats
        print("What would you like to do?")
        print("1) Fight Monster")
        print("2) Sleep (Restore 20 HP for 5 Money)")
        print("3) Quit")

        decision = input('Enter your decision (1-3): ') #prompts user to choose an action

        if decision == '1':
            monster = gamefunctions.new_random_monster() 
            current_hp = gamefunctions.fight_monster(current_hp, monster) #initiates fight from gamefunctions
            if current_hp <= 0:
                print('You have been slain!')
                is_playing = False # exits game if health falls below 0
        elif decision == '2':
            current_hp, current_money = gamefunctions.sleep(current_hp, current_money) # updates health and money with sleep function from gamefunctions
        elif decision == '3':
            print('Thank you for playing!')
            is_playing = False # exits the game
        else:
            print("Invalid entry, please choose (1-3)")
    
if __name__=='__main__':
    main()
