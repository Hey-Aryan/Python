# Write a program which contains one lambda function which accepts 
# two parameters and return its multiplication 

Mult = lambda No1,No2 : (No1*No2)

def main():
    Ret = 0
    Value1 = int(input("Enter first number  : "))
    Value2 = int(input("Enter second number : "))

    Ret = Mult(Value1,Value2)
    print("Multiplication is   :",Ret)


if __name__ == "__main__":
    main()