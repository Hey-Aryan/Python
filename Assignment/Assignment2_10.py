# Write a program which accept number from user and return addition 
# of digits in that number 



def CntDigit(No):
    iDigit = 0
    iSum = 0
    while(No != 0):
        iDigit = No % 10 
        iSum = iSum + iDigit
        No = No // 10 
    return iSum

def main():
    iRet = 0
    Value = int(input("Enter the number : "))
    iRet = CntDigit(Value)
    print("Addition of digits present in ",Value," = ",iRet)

if __name__ == "__main__":
    main()