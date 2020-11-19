#Oregon Trail Game
#Luke Rowberry and Jordan Jackson
import datetime
import random

START_DATE = datetime.datetime(1848,3,1)
current_date = START_DATE
hp = 100
ox_hp = 100
total_miles = 2000
miles_traveled  = 0
food = 1000 #all below is temporary
rations = "full"
health_condition = "good"
weather = "cold"
pace = "normal"
ox = 4

def turn(hp,current_date,food,miles_traveled,total_miles):
    weather = random.choice(["hot","good","fair","poor","windy","rain","blizzard"])
    if hp >= 80:
        health_condition = "good"
    elif hp < 80 and hp >= 50:
        health_condition = "fair"
    else:
        health_condition = "poor"

    if rations == "full":
        rations_mod = 2
    elif rations == "half":
        rations_mod = 1
    else:
        rations_mod = .5

    problem = random.choice(["lost","snake bite","sick","ox died",
                             "none","none","none","none","none",
                             "none","none","none","none","none"])

    if problem == "lost":
        lost = random.randint(1,7)
        print("One of your family members got lost for",lost,"days")
        current_date += datetime.timedelta(days = lost)
        food -= (len(family_list)+1)*ration_mod * lost

    if problem == "snake bite":
        hp -= 50

    if problem == "sick":
        hp -= 20

    if problem == "ox died":
        ox -= 1
        food += 50

    print(str.format("""
   .....                                        ..'..                              ..',,,'..        
..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..   
,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                      ........        ...............            ...
 +-----------------------------+                                                                    
 |Date:{:_>24}|                 
 |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.        
 |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.      
 |Miles Travled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.      
 |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.       
 |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.        
 +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'         
                 ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,          
          .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'           
           .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.           
         .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.          
          ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.          
                .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.            
                 .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.            
                  .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.            
                .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.              
'..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
;;;;;;;;;;;;;;;;;:::;;;::;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;
""",current_date,weather,hp,miles_traveled,total_miles,food))
    
        
    
    print("What would you like to do?")
    while True:
        options = ["Continue on Trail",
               "Check Supplies",
               "Change Pace",
               "Change Rations",
               "Stop and Rest"]
        x = menu(options)
        if x == 1:
            miles_traveled = travel(pace,weather,health_condition) #doesnt exist yet
            food -= (len(family_list)+1)*ration_mod
            current_date += date.time.timedelta(days=1)
            total_miles -= miles_traveled
            break

        elif x == 2:
            check_supplys()
        elif x == 3:
            Pace() 
        elif x == 4:
            rations() 
        elif x == 5:
            hp,days = rest()
            food -= (len(family_list)+1)*rations_mod*days
            current_date += datetime.timedelta(days=rested)
            break

    if hp <= 0:
        die = random.choice(family_list)
        family_list.remove(die)
        hp = 100


    
    

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
    wagon_leader =get_name("What is your name?")
    family_list = []
    num = getnum("How many members are in your family?",2,7)
    for i in range(num):
        name = get_name("Whats your family members name?")
        family_list.append
    return wagon_leader,family_list
        

def shop(money,food,ammo,cloths,parts,ox):            #starter items shop
    bill = 0
    inventory = []
    items = ["Oxen","Food","Ammo",
              "Clothes","Wagon parts",
              "Checkout"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]
    print("\nBefore leaving Independence you should buy equipment")
    print(str.format("You have {} in cash to make this trip",money))
    input("\nPress ENTER to Continue")

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
            print("\nThere are 2 oxen in yoke, I recommend atleast 3 yoke, $40 a yoke.")
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
            print("\nI recommend atleast 200 lbs of food per person. My price is 20 cents per lb.")
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
            print("\nI sell boxes containing 20 bullets each. Eat set is $2.")
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
            print("\nI recommend atleast 2 sets of clothing per person. Eat set is $10.")
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
            parts = ["Wagon Wheel", "Wagon Axle", "Wagon Tongue","Back To Main Shop"]
            parts_cost = [10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost)-1] = parts_bill
                print("\nHere is a list of the parts you can buy:")
                for i in range(len(parts)):
                    print(str.format("{}.      {:20}      ${:.2f}",i+1,parts[i],parts_cost[i]))
                print(str.format("Total funds available:      ${:.2f}",(money-bill)- parts_bill))
                item = int(input("What item do you want to buy?"))
                if item ==1:
                    answer = int(input("\nHow many wagon wheels do you want?"))
                    for i in range(answer):
                        inventory.append("Wagon Wheel")
                        parts_bill += parts_cost[0]*answer
                elif item ==2:
                    answer = int(input("\nHow many wagon axles do you want?")) 
                    for i in range(answer):
                        inventory.append("Wagon Axle")
                        parts_bill += parts_cost[1]*answer
                elif item ==3:
                    answer = int(input("\nHow many wagon tongues do you want?"))
                    for i in range(answer):
                        inventory.append("Wagon Tongue")
                        parts_bill += parts_cost[2]*answer
                elif item == 4:
                    bill += parts_bill
                    spent_on_items[4] = parts_bill
                    break
        if choice == 6:
            if bill <= money:
                money -= bill
                return money,food,ammo,cloths,parts,ox
            else:
                print("""You don't have that much money...\n
                      Please alter your shopping list.""")
                    
def rest():
    pass
def hunt():
    pass

def Pace():
    while True:
        options = ["Slow","Normal","Fast"]
        x = menu(options)
        if x == 1:
            pace = "slow"
        elif x == 2:
            pace = "normal"
        elif x == 3:
            pace = "fast"
        return pace

def travel(pace,weather,health_condition):
    import random
    mph = 0
    weather_mod = 0
    hours = 0
    if pace == "fast":
        mph = 4
    elif pace == "slow":
        mph = 1
    else:
        mph = 2
    if health_condition == "poor":
        hours = 2
    elif health_condition == "fair":
        hours = 4
    else:
        hours = 8
    if weather == "blizzard":
        weather_mod = 0
    elif weather == "hot":
        weather_mod = .5
    elif weather == "rain":
        weather_mod = .25
    else:
        weather_mod = 1
    miles = hours * mph * weather_mod
    random_mod = random.randint(0,5)
    return miles - random_mod



def Rations():
    print ("Your current rations are", rations)
    while True:
        options = ["full","half","quarter"]
        x = menu(options)
        if x == 1:
            return "full"
        elif x == 2:
            return "half"
        elif x == 3:
            return "quarter"
        else:
            print("Not an option")
        

def check_supplies():
    pass
    
     

                           
                             
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
    miles = travel(pace,weather,health_condition)
    print(miles)
    rations = Rations()
    print(rations)
    #while len(family) > 0 and total_miles > 0:
        #turn(hp,food,total_miles,family)
        #hp,food,total_miles
        #hp,current_date,food,miles_traveled,total_miles,

    #if total_miles <= 0:
        #print("Congrats, you made it to Oregon!")
    #else:
        #print("You and your family have died on the trail!")

    

#start game
logo_screen()
start_screen()

