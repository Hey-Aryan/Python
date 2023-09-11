# Read file

import os
def main():
    print("Enter the file that you want to open for reading purpose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"r") #read mode
        if fobj:
            print("File opened successfully in append mode")
            
            Line1 = fobj.readline()
            Line2 = fobj.readline()
            Line3 = fobj.readline()
            print("First Line is :",Line1)
            print("Second Line is :",Line2)
            print("Third Line is :",Line3)

            fobj.close()
        else:
            print("Unable to open the file ")
    else:
        print("There is no such file")

if __name__=="__main__":
    main()