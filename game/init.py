import sys,game
introText = r"""______                            _   _____ _           ______       _   _   _                           _       
| ___ \                          | | |_   _| |          | ___ \     | | | | | |                         | |      
| |_/ / ___ _   _  ___  _ __   __| |   | | | |__   ___  | |_/ / __ _| |_| |_| | ___ _ __ ___   ___ _ __ | |_ ___ 
| ___ \/ _ \ | | |/ _ \| '_ \ / _` |   | | | '_ \ / _ \ | ___ \/ _` | __| __| |/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
| |_/ /  __/ |_| | (_) | | | | (_| |   | | | | | |  __/ | |_/ / (_| | |_| |_| |  __/ | | | | |  __/ | | | |_\__ \
\____/ \___|\__, |\___/|_| |_|\__,_|   \_/ |_| |_|\___| \____/ \__,_|\__|\__|_|\___|_| |_| |_|\___|_| |_|\__|___/
             __/ |                                                                                               
            |___/                                                                                                """
print(introText)
spacer = "\n"
print(spacer)
print("""Welcome to Beyond The Battlements
a Text Based Adventure Game created by Jokrr
I hope you enjoy playing this game""")
print(spacer)
menu = input("""Please select an option
1: Start Game
2: About
3: Quit 
""")
#System Functions
def closeCheck():
    closecheck = input("This will close the program do you want to continue?(y/n)").lower()
    if closecheck == "y":
            closeprogram()
    elif closecheck == "n":
            print("Returning to Main Menu")
            menuCheck()
    else:
        print("""Input not recognized
        Reloading...""")
        closeCheck()
def closeprogram():
    print("Closing Program...")
    sys.exit()
#Menu option check

def gameLoad():
    print("Starting game...")
    game.adventureStart()
def gameAbout():
    print("Loading Information...")

def menuCheck():
    try:
        if menu == "1":
            gameLoad()
        elif menu == "2":
            gameAbout()
        elif menu == "3":
            closeCheck()
    except ValueError:
        print("Value Error: You did not input a number")
        print("Reloading")
        menuCheck()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        menuCheck()
menuCheck()