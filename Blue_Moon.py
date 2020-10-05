moon = input("Is there a blue moon tonight? (Yes/No) ")
day_week = input("What is the day of the week? (Monday - Sunday) ")
day_month = int(input("What day of the month? (1 - 31) "))

if moon == ("Yes"):
    print("Once in a Blue Moon")
elif day_month <= 7:
    if day_week == ("Monday"):
        print("Manic Monday")
    elif  day_week == ("Tuesday"):
        print("Tuesday's Gone")
    elif day_week == ("Wednesday"):
        print("Just Wednesday")
    elif day_week == ("Thursday"):
        print("Sweet Thursday")
    elif day_week == ("Friday"):
        print("Friday I'm in Love")
    elif day_week == ("Saturday"):
        print("Saturday in the Park")
    elif day_week == ("Sunday"):
        print("Lazing on a Sunday Afternoon")
    else:
        print("Days of the Week")
else:
    print("Day Dream Believer")

input()
        
    
    
