#Luke Rowberry
#Dec,3,2020
#Dealing with pickles

#sidenote:use "pip" to install libraries
import pickle, shelve


variety = ["Dill","Sweet","Gherkin","Bread and Butter","Hot"]
shape = ["Whole","Spear","Chips","Slices","Relish"]
brand = ["Heinz","Great Value","Western Family","Vlassic","Claussen"]

try:
    shelf = shelve.open("pickles2.dat")
    shelf["x"] = variety
    shelf["y"] = shape
    shelf["z"] = brand
    shelf.sync()
except:
    print("There is a problem...")
    input("Press ENTER to exit...")
    quit()

print("brand-",shelf["x"])
print("shape-",shelf["y"])
print("variety-",shelf["z"])
shelf.close()


##file = open("assets/saved_data/pickles1.dat","wb")
##
###(what your dumping - where it dumps)
##pickle.dump(variety,file)
##pickle.dump(shape,file)
##pickle.dump(brand,file)
##
##
##file = open("assets/saved_data/pickles1.dat","rb")
##
##list1 = pickle.load(file)
##list2 = pickle.load(file)
##list3 = pickle.load(file)
##
##print(list1)
##print(list2)
##print(list3)


##file.close()
