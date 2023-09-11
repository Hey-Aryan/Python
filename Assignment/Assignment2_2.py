# Writw a program which accept one number and display below pattern 
#   5
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *

def Display(No):
    
    for i in range(No):
        for i in range(No):
            print("*",end=" ")
        print()  

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()