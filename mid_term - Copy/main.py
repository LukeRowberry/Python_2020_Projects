#Luke Rowberry
#12,3,2020
#Test that can read plain text files

#imports
import sys

#functions
def open_file(file_name,mode):
    """open and returns an open file with the given permissions"""
    try:
        file = open("assets/test_files/"+file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name,"Ending program. \n", e)
        try:
            file = open("assets/errors/errors_log.txt","a+")
            file.writelines(str(e))
            input("\n\nPress ENTER to exit...")
            sys.exit()
        except:
            sys.exit()
    else:
        return file

def main():
    file = open_file("example_test.txt","r")

main()
