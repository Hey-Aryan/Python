# Display numbers using loop

def DisplayNumbers(No):
    for i in range (1,No+1):
        print(i)

def main():
    Value = int(input("Enter the Number till whichh you want to print : "))

    DisplayNumbers(Value)

if __name__ == "__main__":
    main()