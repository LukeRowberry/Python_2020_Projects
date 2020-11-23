class Car():

    def __init__(self):
        self.color = ""
        self.size = ""
        self.brand = ""
        self.make = ""
        self.tire_brand = ""
        self.tire_size = ""
        self.type = ""
        self.price = 0.0
        self.drive_train = ""
        self.fuel_type = ""
        self.year = ""
        self.engine = Engine()
        #self.radio = Radio()

        self.color = input("What color do you want your car?")
        self.size = input("What size do you want your car?")
        self.brand = input("What brand do you want your car?")
        self.make = input("What make do you want your car?")
        self.tire_brand = input("What is the tire brand?")
        self.tire_size = input("What is the tire size?")
        self.type = input("What is your type of car?")
        self.price = input("What is the price?")
        self.drive_train = input("Whats the drive train?")
        self.fuel_type = input("Whats the fuel type?")
        self.year = input("What year is your car?")

        

class Engine():

    def __init__(self):
        self.cylinder = 0
        self.cylinder_ornt = ""
        self.mpg = 0

        self.cylinder = input("What is the cylinder?")
        self.cylinder_ornt = input("What is the cylinder orientation?")
        self.mpg = input("What is the miles per gallon?")

        
        
def main():
    my_dream_car = Car()
    print(my_dream_car.color)
    






main()
    
        
        
        
