##isawake = True #must be capital T or F
##issleeping = False
##
##name = "Luke"
##lastname = ""
##
##print(isawake)
##print(type(isawake))
##
##result = 30<44
##print(result)
##print(type(result))
##
##input1 = input("Enter a number between 1 and 100. ")
##input2 = input("Enter another number between 1 and 100. ")
##
##result = input1 != input2
##print("Is input one not equal to input two? ",result)
##
##if input1!= input2:
##    print("input1 != input2")


password = "Password1!"

userinput = input("Enter Your Password: ")

if userinput == password:
    print("--Access Granted--") #watch the indentations

if userinput != password:
    print("--Access Denied--")
