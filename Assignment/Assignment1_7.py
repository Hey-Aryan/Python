# write a program which contains one function that accepts one
# number from user and returns true if number is divisible 
# by 5 other wise return false 

def Divisible5(No):
    if(No % 5 == 0):
        print("True")
    else:
        print("False")

def main():
    Value = 0
    
    print("Enter the number ")
    Value = int(input())

    Divisible5(Value)


if __name__ == "__main__":
    main()

