def main():
    print("Enter the name of the file that you want to create :")
    File_name = input()
    try:
        fobj = open(File_name,"x")

    except FileExistsError as obj:
        print("File Already exists :",obj)
        return

if __name__ =="__main__":
    main()