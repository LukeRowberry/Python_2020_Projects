#Logo Screen for Oregon Trail

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


logo_screen()


options = ["option 1","option 2","option 3","option 4","option 1","option 2","option 3"]
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


x = menu(options)
print(x)
input()


def start_screen():
    trail = """

___________.__             ________                                       ___________             .__.__   
\__    ___/|  |__   ____   \_____  \_______   ____   ____   ____   ____   \__    ___/___________  |__|  |  
  |    |   |  |  \_/ __ \   /   |   \_  __ \_/ __ \ / ___\ /  _ \ /    \    |    |  \_  __ \__  \ |  |  |  
  |    |   |   Y  \  ___/  /    |    \  | \/\  ___// /_/  >  <_> )   |  \   |    |   |  | \// __ \|  |  |__
  |____|   |___|  /\___  > \_______  /__|    \___  >___  / \____/|___|  /   |____|   |__|  (____  /__|____/
                \/     \/          \/            \/_____/             \/                        \/
                """

    
    
    

    
