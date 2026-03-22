# -- main coffee order loop --
def coffee_order():
    print("Welcome to Cafe Ole!")
    name = get_user_name()
    more_drinks = True
    drinks = []
    # -- order loop --
    while more_drinks:
        user_drink = get_user_order(name)
        user_size = get_user_size()
        ordered_drink = f"{user_size} {user_drink}"
        print(f"Alrighty! That's a {ordered_drink}!")
        drinks.append(ordered_drink)
        # -- determining if loop continues or breaks --
        more_drinks = get_more_drinks(name)
    print("Perfect: Altogether, I have: ")
    for ordered_drink in drinks:
        print("-", ordered_drink)
    print("That order should be ready shortly! Thank you so much for coming to Cafe Ole!")
        
# -- get_user_name helper function --
def get_user_name ():
    name = input("Can I get your name, for the order?\n> ")
    return name

# -- get_user_order helper function -- 
def get_user_order(name):
    while True:
        user_selection = input(f"Thank you, {name}! What can I get started for you, today?\n"
                            " [A] Brewed Coffee\n"
                            " [B] Mocha\n"
                            " [C] Latte\n"
                            " [D] Earl Grey Tea\n"
                            " [E] Green Tea\n> "
                            ).strip().lower()
        if user_selection == "a":
            return "Brewed Coffee"
        elif user_selection == "b":
            return mocha_special()
        elif user_selection == "c":
            return latte_milk_choice()
        elif user_selection == "d":
            return "Earl Grey"
        elif user_selection == "e":
            return "Green Tea"
        else:
            error_statement()

# -- get_user_size helper function --
def get_user_size():
    while True:
        size_selection = input("And what size for that order?\n"
                           " [A] Small\n"
                           " [B] Medium\n"
                           " [C] Large\n> "
                           ).strip().lower()
        if size_selection == "a":
            return "Small"
        elif size_selection == "b":
            return "Medium"
        elif size_selection == "c":
            return "Large"
        else:
            error_statement()

# -- mocha_special helper function --
def mocha_special():
    while True:
        special_selection = input("Can I interest you in our limited edition salted caramel mocha?\n"
                                " [A] Sure!\n"
                                " [B] No, thank you! Not today!\n> "
                                ).strip().lower()
        if special_selection == "a":
            return "Salted Caramel Mocha"
        elif special_selection == "b":
            return "Mocha"
        else:
            error_statement()

# -- latte milk selection --
def latte_milk_choice():
    while True:
        milk_selection = input("And for that latte, which milk type would you like:\n"
                               " [A] Whole Milk\n"
                               " [B] 2% Milk\n"
                               " [C] Soy Milk\n"
                               " [D] Almond Milk\n"
                               " [E] Oat Milk\n> "
                               ).strip().lower()
        if milk_selection == "a":
            return "Whole Milk Latte"
        elif milk_selection == "b":
            return "2% Milk Latte"
        elif milk_selection == "c":
            return "Soy Milk Latte"
        elif milk_selection == "d":
            return "Almond Milk Latte"
        elif milk_selection == "e":
            return "Oat Milk Latte"
        else:
            error_statement()

# -- get_more_drinks helper function --
def get_more_drinks(name):
    while True:
        more_coffee = input(f"{name}, can I get you anything else?\n"
                         " [A] Yes, please!\n"
                         " [B] No, thank you! I am all set.\n> "
                         ).strip().lower()
        if more_coffee == "a":
            return True
        elif more_coffee == "b":
            return False
        else:
            error_statement()
    
# -- user redirect, error statement --  
def error_statement():
    print("Sorry! Didn't catch that! Could you try again, based on the letter selection, below:")

if __name__ == "__main__":
    coffee_order()