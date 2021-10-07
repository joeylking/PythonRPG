import random

# As a user, I want an engaging story to be told using print() statements. 
# As a user, I want Hercules (and each enemy), to have health, attack power, and a list of attack names saved in a Dictionary.
# As a user, I want the ability to select Hercules’ attack using a menu prompt.
# As a user, I want the foe’s attack to be chosen at random.
# As a user, I want the results of each attack to be logged in the terminal. 
# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero. 
# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow.
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

hercules = {
    "health" : 100,
    "power" : 90,
}
lion = {
    "health" : 100,
    "power" : 60,
}
hydra = {
    "health" : 100,
    "power" : 70,
}
boar = {
    "health" : 100,
    "power" : 65,
}
birds = {
    "health" : 100,
    "power" : 75,
}
bull = {
    "health" : 100,
    "power" : 70,
}
horses = {
    "health" : 100,
    "power" : 70,
}
hippolyte = {
    "health" : 100,
    "power" : 80,
}
geryon = {
    "health" : 100,
    "power" : 80,
}
hesperides = {
    "health" : 100,
    "power" : 70,
}
cerberus = {
    "health" : 100,
    "power" : 75,
}

def labors_menu():
    def print_menu():
        print(10 * "-", "CHOOSE YOUR LABOR", 10 * "-")
        print("1. The Nemean Lion")
        print("2. The Lernaean Hydra")
        print("3. The Erymanthean Boar")
        print("4. The Stymphlaian Birds")
        print("5. The Cretan Bull")
        print("6. The Horses of Diomedes")
        print("7. Hippolyte's Belt")
        print("8. The Cattle of Geryon")
        print("9. The Apples of Hesperides")
        print("10. Cerberus")
        print(39 * "-")

    loop = True

    while loop:
        print_menu()
        choice = input("Enter your choice [1-10]: ")
        if choice == '1':
            print("To the hills of Nemea you go!")
            loop = False
        elif choice == '2':
            print("Off to Lerna!")
            loop = False
        elif choice == '3':
            print("Mount Erymanthus it is!")
            loop = False
        elif choice == '4':
            print("The town of Stymphalos awaits your arrival!")
            loop = False
        elif choice == '5':
            print("To Crete!")
            loop = False
        elif choice == '6':
            print("Good luck in Bistonia!")
            loop = False
        elif choice == '7':
            print("To the Amazons!")
            loop = False
        elif choice == '8':
            print("Get those cows!")
            loop = False
        elif choice == '9':
            print("Mmm apples!")
            loop = False
        elif choice == '10':
            print("Get that dog!")
            loop = False

def RunGame():

    print("""
    
    Hello, Hercules. 
    
    
    Apollo has ordred you to complete 12 heroic labors for Eurystheus.


    """)

    labors_menu()


RunGame()
