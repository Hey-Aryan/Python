# Write a program which accepts number from user and check
# whether that number is positive or negative or zero

def ChkType(number):
    if(number > 0 ):
        print("Positive Number !!")
    elif(number < 0):
        print("Negative Number !!")
    else:
        print("Zero !!!")
    

def main():

    No = int(input("Enter the number : "))

    ChkType(No)

if __name__ =="__main__":
    main()

