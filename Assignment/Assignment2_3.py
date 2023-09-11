# Write a program which accept one number from user 
# and return its factorial 
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(No):
    iMult = 1
    for i in range(No,0,-1):  #1*2*3*4*5
        iMult = iMult * i

    return iMult

def main():
    iRet = 0
    Value = int(input("Enter the number : "))

    iRet = factorial(Value)
    print("Factorial is : ",iRet)



if __name__ == "__main__":
    main()