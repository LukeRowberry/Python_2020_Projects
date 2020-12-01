#Read It
#Luke Rowberry
#Dec,1,2020


#main
#text_file = open("file location with extention","permissions")

#C:\Users\luke.rowberry\Desktop\read_write_project\assets\saved_data
try:
    text_file = open("assets\\saved_data\\write_me.txt","w") #\\ or /
except:
    print("That file doesn't exist...")
    text_file = open("assets\\saved_data\\write_me.txt","w+")

#read funciton moves cursor through file and starts where it stops
#negative reads whole text

##line1 = text_file.readline()
##line2 = text_file.readline()
##print(line1)
##print(line2)

##text = "space"
##while text != "":
##    text = text_file.readline()
##    print(text)

##lines = text_file.readlines()
##print(lines)
##for line in lines:
##    print(line)

lines = ["top text\n","12345\n","bottom text\n"]
text_file.writelines(lines)

##text_file.writelines("example text") #must use \n to seperate
##text_file.writelines("24")
##text_file.writelines("asdsgujsetgs")

text_file.close()
#close text to return cursor to top

#write can only write and not read
try:
    text_file = open("assets\\saved_data\\write_me.txt","r")
except:
    print("That file doesn't exist...")
    text_file = open("assets\\saved_data\\write_me.txt","w+")

line1 = text_file.readline()
line2 = text_file.readline()
line3 = text_file.readline()
print(line1)
print(line2)
print(line3)
text_file.close()






