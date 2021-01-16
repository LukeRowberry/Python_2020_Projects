class Robot:
    name = "Mr. Roboto"
    thank_you = "Domo arigato"

    def thanks():
        print(Robot.thank_you)
        print(Robot.name)

Robot.thanks()
Robot.name = "T-1000" 
Robot.thank_you = "Thankee Kindly"
Robot.thanks()
