import os

def main():
    print("Enter the name of the file that you want to create :")
    File_name = input()

    if os.path.exists(File_name):
        os.remove(File_name)
    else:
        print("There is no file")

    

if __name__ =="__main__":
    main()