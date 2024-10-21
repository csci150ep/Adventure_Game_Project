import gamefunctions

def main():
    player_name = input('Please enter your name: ')
    gamefunctions.print_welcome(player_name)

    print('\nWelcome to the shop, here are the available items:')
    gamefunctions.print_shop_menu('Bread', 4.50, 'Gloves', 7.25)

    print('\nLet me help you manage your purchases:')
    item_price = float(input('Enter the price of your desired item: '))
    money = float(input('How much money do you have? '))
    quantity = int(input('How many items do you want to purchase? '))

    items_bought, remaining_money = gamefunctions.purchase_item(item_price, money, quantity)
    print(f"\nYou bought {items_bought} item(s), and you have ${remaining_money:.2f} left.")

    print('\nThe new random monster is...')
    monster = gamefunctions.new_random_monster()
    print(f"Monster: {monster['name']}, Description: {monster['description']}, "
          f"Health: {monster['health']}, Power: {monster['power']}, Money: ${monster['money']}")

if __name__=='__main__':
    main()
