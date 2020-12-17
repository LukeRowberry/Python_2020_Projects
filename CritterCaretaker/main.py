import random
class Critter(object):
    """this is the class that defines what a critter is"""
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2, 7)
        self.name = ""
        self.happy = 50
        self.isAlive = True

    def get_hunger(self):
        return self.hunger

    def get_health(self):
        return self.health

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def get_happy(self):
        return self.happy

    def set_name(self, name):
        if len(name) > 4:
            if (name.contains("uck")) == False:
                self.name = name


    def set_height(self, height):
        if height < 5 and height > 1:
            self.height = height

    def intro(self):
        print("Hello, my name is "+self.get_name())

    def hud(self):
        print(self.get_name())
        health = self.get_health()
        if health > 80:
            print("Health: Great")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            print("Your pet ran out of health!")
            self.die()
        else:
            print("Health: Poor")
        hunger = self.get_hunger()
        if hunger > 40 :
            print("Hunger: Starving")
        elif hunger > 20 :
            print("Hunger: Really Hungry")
        elif hunger < 10:
            print("Hunger: Full")
        else:
            print("Hunger: Hungry")
        if hunger == 100:
            print("You let your pet starve!")
            self.die()
        if hunger == -100:
            print("You overfed your pet!")
            self.die()
        happy = self.get_happy()
        if happy > 80:
            print("Happy: Content")
        elif happy > 60:
            print("Happy: Excited")
        elif happy > 50:
            print("Happy: Happy")
        else:
            print("Happy: Grumpy")

    def die(self):
        print("Your pet has died. You suck!")
        self.health = 0
        self.isAlive = False

    def feed(self, food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheeseburger":
            self.hunger -= 13
        elif food == "steak":
            self.hunger -= 23
        elif food == "corn":
            self.hunger -= 3
        elif food == "cheesecake":
            self.hunger -= 100
        else:
            self.hunger -= 5

    def pass_time(self, hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happy += 10
                self.health -= 5
            if self.hunger > 50:
                self.weight -= 1
                self.happy -= 10
                self.health -= 5
            self.happy -= 5

    def play(self, time):
        self.pass_time(self, time)
        self.happy += 10 * time
        if self.happy > 100:
            self.happy = 100
        self.health += 10 * time
        if self.health > 100:
            self.health = 100

def main():
    pet = Critter()
    name = input("What would you like to name your pet?")
    pet.set_name(name)
    height = int(input("How tall is your pet? (2in.-5in.)"))
    pet.set_height(height)
    pet.intro()
    pet.hud()
    while pet.isAlive:
        pet.pass_time(1)
        print("What would you like to do now?")
        print("Feed")
        print("Play")
        print("Nothing")
        response = input()
        if response == "feed":
            food = input("What do you want to feed your pet?")
            pet.feed(food)
        if response == "play":
            time = input("How long would you like to play?")
            pet.play(time)
        pet.hud()

main()