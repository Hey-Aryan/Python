import os.path

def main():
    print("Enter the name of the file that you want to create :")
    File_name = input()

    check_file = os.path.exists(File_name)
    if(check_file == True):
        print("File Already exists")
    else:
        fobj = open(File_name,"x")

    

if __name__ =="__main__":
    main()