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



def menu(options):       #menu function
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


def learn():              #learn game
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






def start_screen():     #Start menu screen
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

def char_setup():         #profession and money

    while True:
        options = ["Be a banker from Boston","Be a carpanter from Ohio"," Be a farmer from Illinois","Find out the differences between these choices"]
        x = menu(options)
        print(design)
        if x == 1:
            money = 1600
            prof = "Banker"
            break
        elif x == 2:
            money = 800
            prof = "Carpanter"
            break
        elif x == 3:
            money = 600
            prof = "Farmer"
            break
        elif x == 4:
            pass #description of professions

    return money,prof

def get_name(question):         #family names 
    while True:
        name = input(question)
        if len(name)>= 2:
            return name
        print("not a valid name")
def getnum(question,low,high):
    while True:
        num = input(question)
        if num.isnumeric():
            num = int(num)
            if num >= low and num <= high:
                return num
        print("not a valid number")
    

def naming_players():
    wagon_leader =get_name("what is your name?")
    family_list = []
    num = getnum("how many members are in your family?",2,7)
    for i in range(num):
        name = get_name("Whats your family members name?")
        family_list.append
    return wagon_leader,family_list
        

def shop(money,food,ammo,cloths,parts,ox):            #starter items shop
    bill = 0
    inventory = []
    items = ["Oxen","Food","Ammunition",
              "Clothes","Wagon parts",
              "Check out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]
    print("\nBefore leaving Independence you should buy Equipment")
    print(str.format("you have {} in cash to make this trip",money))
    print("remember you can buy supplys along the way so you don't have to spend it all now")
    input("press ENTER to Continue")

    while True:
        
        spent_on_items[len(spent_on_items)-1] = bill
        print("\nWelcome to JL's general store")
        print("\nHere is a list of things you can buy")
        for i in range(len(items)):
            print(str.format("{}.      {:20}      ${:.2f}",i+1,items[i],spent_on_items[i]))
        print(str.format("Total bill so far:       ${:.2f}",bill))
        print(str.format("Total funds available:      ${:.2f}",money-bill))
        choice = int(input("What item?: "))
        
        if choice == 1:
            bill -= spent_on_items[0]
            ox = 0
            spent_on_items[0] = 0.00
            print("2 oxen in yoke, recommend atleast 3 yoke, $40 a yoke.")
            print(str.format("Total bill so far:       ${:.2f}",bill))
            answer = int(input("How many yoke?: "))
            cost = answer*40
            ox = answer*2
            bill += cost
            spent_on_items[0] = cost
        elif choice == 2:
            bill -= spent_on_items[1]
            food = 0
            spent_on_items[1] = 0.00
            print("I recommend atleast 200 lbs of food per person. My price is 20 cents per lb.")
            print(str.format("Total bill so far:       ${:.2f}",bill))
            answer = int(input("How many pounds of food?: "))
            cost = answer*0.20 
            food = answer
            bill += cost
            spent_on_items[1] = cost
        elif choice == 3:
            bill -= spent_on_items[2]
            ammo = 0
            spent_on_items[2] = 0.00
            print("I sell boxes containing 20 bullets each. Eat set is $2.")
            print(str.format("Total bill so far:       ${:.2f}",bill))
            answer = int(input("How many boxes of ammo?: "))
            cost = answer*2.00
            ammo = answer
            bill += cost
            spent_on_items[2] = cost
        elif choice == 4:
            bill -= spent_on_items[3]
            cloths = 0
            spent_on_items[3] = 0.00
            print("I recommend atleast 2 sets of clothing per person. Eat set is $10.")
            print(str.format("Total bill so far:       ${:.2f}",bill))
            answer = int(input("How many sets of clothes?: "))
            cost = answer*10.00
            cloths = answer
            bill += cost
            spent_on_items[3] = cost
        elif choice == 5:
            print("""\nIt's a good idea to have
some wagon parts on hand.""")

            parts_bill = 0.00
            parts = ["wagon wheel", "wagon axle", "wagon tongue","checkout"]
            parts_cost = [10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost)-1] = parts_bill
                print("\nHere is a list of the parts you can buy:")
                for i in range(len(parts)):
                    print(str.format("{}.      {:20}      ${:.2f}",i+1,parts[i],parts_cost[i]))
                print(str.format("Total funds available:      ${:.2f}",(money-bill)-parts_bill))
                item = int(input("what item to buy?"))
                if item ==1:
                    answer = int(input("how many wagon wheels do you want?"))
                    for i in range(answer):
                        inventory.append("wagon wheel")
                        parts_bill += parts_cost[0]*answer
                if item ==2:
                    answer = int(input("how many wagon axles do you want?")) 
                    for i in range(answer):
                        inventory.append("wagon axel")
                        parts_bill += parts_cost[1]*answer
                if item ==3:
                    answer = int(input("how many wagon tongues do you want?"))
                    for i in range(answer):
                        inventory.append("wagon tongue")
                        parts_bill += parts_cost[2]*answer
                elif item == 4:
                    bill += parts_bill
                    spent_on_items[4] = parts_bill
                    break
                    
                
        
        

                           
                             
def play_game():     #Playing the game  

    money = 0
    prof = ""
    leader = ""
    family = []
    money,prof = char_setup()
    leader,family = naming_players()

   
    food = 0
    ammo = 0
    cloths = 0
    parts =[]
    ox = 0
    money,food,ammo,cloths,parts,ox = shop(money,food,ammo,cloths,parts,ox)   


    

#start game
logo_screen()
start_screen()
