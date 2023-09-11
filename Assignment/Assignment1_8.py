# Write a program which accepts number from user and 
# print that number of * on screen

def Display(No):

    for No in range(No):
        print("*",end=" ")
    print("\n")

def main():
    Value = 0
    
    print("Enter the number ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()


