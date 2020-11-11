#Oregon Trail Game


design = """
                                  ___
=================================(___)===================================
                                  
"""
def logo_screen():
    logo = """
         ____.____        _________ __            .___.__              
        |    |    |      /   _____//  |_ __ __  __| _/|__| ____  ______
        |    |    |      \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
    /\__|    |    |___   /        \|  | |  |  / /_/ | |  (  <_> )___ \ 
    \________|_______ \ /_______  /|__| |____/\____ | |__|\____/____  >
                     \/         \/                 \/               \/
"""

    creator = """
                     Jordan Jackson - Luke Rowberry
"""

    copy = """
                       This game is copyrighted ©
"""

    print(logo)
    print(creator)
    print(copy)



def menu(options):
    index = 1
    for i in options:
        print (str.format("[{}: ........ {:.50}]",index,i))
        index+=1
    while True:
        choice = input("Pick a number between 1 and "+str(len(options)))
        if choice.isnumeric():
            choice = int(choice)
            if choice >= 1 and choice <= len(options):
                return choice
            else:
                print("Not a good option")
        else:
            print("Not a good option")


def learn():
    print("""\nTry taking a journey by
covered wagon across 2000
miles of plains,rivers, and
mountains. Try! on the
plains, will you slosh your
oxen through mud and
water-filled ruts or will you
plod through dust six inches

deep?\n""")
    user_input = input("Press ENTER to Continue\n")

    print("""How will you cross the rivers?
If you have money, you might
take a ferry (if there is a
ferry). Or, you can ford the
river and hope you and your
wagon aren't swallowed alive!\n""")
    user_input = input("Press ENTER to Continue\n")

    print("""What about supplies? Well, if
you're low on food you can
hunt. You might get a buffalo...
you might. And there are
bear in the mountains.\n""")

    user_input = input("Press ENTER to Continue\n")

    print("""At the Dalles, you can try
navigating the Columbia River,
but if running the rapids with
a makeshift raft makes you
queasy, better take the Barlow
Road.\n""")

    user_input = input("Press ENTER to Continue\n")

    print("""If for some reason you don't
survive -- your wagon burns,
or thieves steal your oxen, or
you run out of provisions, or
you die of cholera -- don't
give up! Try again...and
again.\n""")

    user_input = input("Press ENTER to Continue\n")

    print("""     The Software team responsible
for creation of this product includes:
            Jordan Jackson
            Luke Rowberry\n""")

    user_input = input("Press ENTER to Continue\n")






def start_screen():
    print(design)
    while True:
        options = ["Travel the trail","Learn about the trail","Quit Game"]
        x= menu(options)
        print(design)
        if x == 1:
            break
        elif x == 2:
            learn()
        elif x == 3:
            quit()
    play_game()

def char_setup():

    while True:
        options = ["Be a banker from Boston","Be a carpanter from Ohio"," Be a farmer from Illinois","Find out the differences between these choices"]
        x = menu(options)
        print(design)
        if x == 1:
            mon = 1600
            prof = "Banker"
            break
        elif x == 2:
            mon = 800
            prof = "Carpanter"
            break
        elif x == 3:
            mon = 600
            prof = "Farmer"
            break
        elif x == 4:
            pass

    play_game

def get_name():
    print(design)
    username = input("What is your name")

    print(design)
    fam_one = input("What is your first family members name")

    print(design)
    fam_two = input("What is your second family members name")

    print(design)
    fam_three = input("What is your third family members name")

    print(design)
    fam_four = input("What is your fourth family members name")

    play_game()

def shop(money,food,ammo,cloths,parts,ox):
    bill = 0
    items = ["Oxen","Food","Ammunition",
              "clothes","Wagon parts",
              "Check out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]
    print("Before leaving Independence you should buy Equipment")
    print(str.format("you have {} in cash to make this trip"))
    print("remember you can buy supplys along the way so you")
    
def play_game():

    mon = 0
    prof = "no"
    char_setup()
    print(mon)
    print(prof)
    get_name()

#need to return choice to play game
    

#start game
logo_screen()
start_screen()
    
