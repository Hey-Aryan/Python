# Write Mode 
# demo.txt

import os
def main():
    print("Enter the file that you want to open for reading purpose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"w") #Write mode
        if fobj:
            print("File opened successfully in Write mode")

            print("Enter the data that you want to write in the file")
            data = input()

            fobj.write(data)
            fobj.close()
        else:
            print("Unable to open the file ")
    else:
        print("There is no such file")

if __name__=="__main__":
    main()