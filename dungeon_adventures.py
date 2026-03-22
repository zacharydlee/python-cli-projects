import random

# -- main gameplay loop function --
def dungeon_adventure():
    print("Welcome adventurer! Thank you for answering our summons. The guild needs you!") 
    name = get_player_name()
    hp = 10
    gold = 5

    while True:
        choice = get_player_choice(name)
        if choice == "a":
            hp, gold = player_exploration(hp, gold)
            print(f"Back in town: HP = {hp} | gold = {gold}")
            if hp <= 0:
                print("You did not survive your injuries. Death claimed you. Game Over")
                break
        elif choice == "b":
            hp, gold = player_shopping(hp, gold)
            print(f"Back in town: HP = {hp} | gold = {gold}")
        elif choice == "c":
            hp, gold = player_rest(hp, gold)
            print(f"Back in town: HP = {hp} | gold = {gold}")
        elif choice == "d":
            break
    print("Thank you for playing Dungeon Adventure! Hope you had fun!")

# -- get player name, helper function --
def get_player_name():
    player_name = input("Can I get your name, to register you in our records?\n>").strip()
    if player_name == "":
        player_name = "Adventurer"
    return player_name

# -- get player choice --
def get_player_choice(name):
    while True:
        choice = input(f"Hello, {name}! What would you like to do?\n"
                   " [A] Accept a quest, and explore the dungeon\n"
                   " [B] Purchase a potion\n"
                   " [C] Rent a room to rest\n"
                   " [D] Quit adventure\n> ").strip().lower()
        if choice in ["a", "b", "c", "d"]:
            return choice
        else:
            player_redirect(name)
    
# -- explore dungeon loop --
def player_exploration(hp, gold):
    
    while True:
        push_forward = input("The dark of the dungeon calls you, whispering within the silence. Do you continue?\n"
                             " [A] Yes\n"
                             " [B] No\n> "
                             ).strip().lower()
        if push_forward == "b":
            return hp, gold
        elif push_forward == "a":
            exploration = random.randint(1, 4)
            if exploration == 1:
                print("Oh, no! You were jumped by a rabid beast, and were wounded! Lose 4 HP!")
                hp -= 4
                if hp <= 0:
                    player_white_out()
                    return hp, gold
                print(f"Player status: HP = {hp} | gold = {gold}")
            elif exploration == 2:
                print("You scavenged scraps from an abandoned post, and found nothing")
                print(f"Player status: HP = {hp} | gold = {gold}")
            elif exploration == 3:
                print("Ah! You were beaten and robbed by bandits crouched in the shadows. Lose 3 HP and 4 gold!")
                hp -= 3
                gold -= 4
                if hp <= 0:
                    player_white_out()
                    return hp, gold
                if gold < 0:
                    gold = 0
                print(f"Player status: HP = {hp} | gold = {gold}")
            elif exploration == 4:
                print("Searched a hidden alcove, and found riches. Gain 5 gold!")
                gold += 5
                if gold > 10:
                    gold = 10
                print(f"Player status: HP = {hp} | gold = {gold}")
        else:
            print("You stumbled in the dark. Try again! [A] or [B]")

# -- player shop loop --
def player_shopping(hp, gold):
    print ("Welcome to Lupin's Loopy Liquids!")
                          
    while True:
        buying = input("Care to buy a potion for 2 gold?\n"
                       " [A] Yes\n"
                       " [B] No \n> ").strip().lower()
        if buying == "a":
            if gold >= 2:
                hp += 2
                gold -= 2
                if hp > 10:
                    hp = 10
                print(f"Player status: HP = {hp} | gold = {gold}")
            else:
                print("Sorry, you do not have enough funds. Please try again later!")
        elif buying == "b":
            return hp, gold
        else:
            print("Sorry! Didn't catch that! [A] or [B]")

# -- player rest loop --
def player_rest(hp, gold):
    print("Evening! Welcome to Tired Eyes Inn.")

    while True:
        sleep = input("Care to rest your weary head, for the night? It will be 5 gold.\n"
                      " [A] Yes\n"
                      " [B] No\n> "
                      ).strip().lower()
        if sleep == "a":
            if gold >= 5:
                hp += 5
                gold -= 5
                if hp > 10:
                    hp = 10
                print(f"Player status: HP = {hp} | gold = {gold}")
            else:
                print("Sorry. Ain't got the coin. You don't have to go home, but you can't stay here.")
        elif sleep == "b":
            return hp, gold
        else:
            print("Sorry! Didn't hear ya, there! Try again. [A] or [B]")
            
# -- player white-out message --
def player_white_out():
    print("Oh, no! You sustained too many injuries, and can no longer continue. Your vision fades.")

# -- player redirect, for input error --
def player_redirect(name):
    print(f"Sorry {name}! The guild cannot approve of that selection. Please choose again from the options below:")

# -- Run file if executed directly --
if __name__ == "__main__":
    dungeon_adventure()