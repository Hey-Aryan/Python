# Writw a program which accept one number and display below pattern 
#   5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5


def Display(No):
    
    for i in range(No):
        for j in range(1,No+1):
            print(j,end=" ")
        print()  

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()