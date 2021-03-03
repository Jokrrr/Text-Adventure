import backend,sys,random

def closeCheck():
    closecheck = input("This will close the program do you want to continue?(y/n)").lower()
    if closecheck == "y":
            closeprogram()
    elif closecheck == "n":
            print("Returning to Main Menu")
            adventureStart()

def closeprogram():
    print("Closing Program...")
    sys.exit()

def charNameGen():
    fName = input("Please enter your characters name e.g. George \n")
    sNameList = ["The Brave", "The Honest", "The Slayer", "The Undefeated", "The Great One", "The Uncorrupted"]
    sNameRand = random.choice(sNameList)
    charNameGen.charName = fName + " " + sNameRand # assigns the variable as a member of the function
   
def IsleCitadel():
    castleAscii = r""" 
       /\         /\                    .           /\
      /  \       /  \                   |@>        /  \
     /    \     / .  \                  |         /    \
    /      \   /  |@> \       /\       / \       /      \
   /     /\ \ /   |    \     /  \     /   \     /        \
  /     /  \ /  _ | _   \   /    \    | O |    /          _   _   _
 /     /    \  |_|_|_|   \ /      \   |___|   /          | |_| |_| |
/     /      \  | O |     /        \  | |_|  /      /\   |         |
    _   _   _ \ |___|    /          \ |__|| /      /  \  |  O   O  |
   | |_| |_| |  | |_|   /             | |_|       /    \ |   __ _  |
   |         |  |__||  /              |_| |      /       |     |   |
   | O  O  O |  | |_| /               |__ |     /        | O  O  O |
   |  _      |  _   _   _        ______   |   _   _   _  |  _      |
   | |__|_ | |_| |_| |_| |______|      |_____| |_| |_| |_| |__|_ |_|
   |  |   _| |        _  |  | _|  ____     _||        _  |  |    | |
   |   _| _  ||_|   _|_  | _|_   |||||| |_| _||_|   _|_  |   _| _| |
   |  __|  |_|  |_       | | |__ |++++|   |_||  |_      ||  __|  |_|
   |_________|___________|-------------------|___________|_________|
                                 /_/_/
                                /_/_/
"""
    print(castleAscii)
    print("The citadel towers over you, the lair of the evil Lord Necronis")
    print("""
    A man from a local town approaches you
    Hello adventurer! What is your name?""")
    charNameGen()
    charNameVar = charNameGen.charName # assigns the member to charNameVar under the function 
    print("Welcome to Islefield ", charNameVar )
    closeCheck()
    
def townThornwall():
    townAscii = r""" 
    ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '"""
    print(townAscii)
    print("""
    The quaint town of Thornwall lays straight ahead
    A man with a book is waiting outside the town
    As you approach he demands your name with his quil at the ready
    """)
    charNameGen()
    charNameVar = charNameGen.charName # assigns the member to charNameVar under the function
    print("Welcome to our quaint little town", charNameVar, "I am the towns clerk I keep notes of all who pass through\n" )
    townSign = r"""
  _______ _                                   _ _ 
 |__   __| |                                 | | |
    | |  | |__   ___  _ __ _ ____      ____ _| | |
    | |  | '_ \ / _ \| '__| '_ \ \ /\ / / _` | | |
    | |  | | | | (_) | |  | | | \ V  V / (_| | | |
    |_|  |_| |_|\___/|_|  |_| |_|\_/\_/ \__,_|_|_|
                                                  
                                                  """
    print("A Large sign behind the man in inscribed with the towns name")
    print(townSign)
    closeCheck()

def adventureStart():
    try:
        start = input("""Please select a location for your adventure!
     1: Islefield Citadel
     2: Town Of Thornwall
     """)
        if start == "1":
            IsleCitadel()
        elif start == "2":
            townThornwall()
        else:
            print("Error: Input not recognized")
            adventureStart()   
    except ValueError:
        print("Value Error: Your Input was not recognized")
        print("Reloading")
        adventureStart()
    except Exception as e:
        print("Unknown Error: ", e)
        print("Reloading")
        adventureStart()
