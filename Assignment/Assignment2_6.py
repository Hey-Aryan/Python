#   5
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *


def Display(No):
    
    for i in range(No+1):
        for j in range(No+1):
            if(i<j):
                print("*",end=" ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()