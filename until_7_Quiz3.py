menu = {
    "b": "Burger",
    "c": "Chicken",
    "p": "Pizza"
}

def show_menu():
    print("Welcome to yummy restaurant. Here is the menu")
    for key, value in menu.items():
        print(f"{key}: {value}")

def get_user_choice():
    while True:
        choice = input("Choose a menu (Enter b,c,p): ").lower()
        if choice in menu:
            print(f"You Choose : {menu[choice]}")
            break
        else:
            print("Enter the Menu again")


show_menu()
get_user_choice()