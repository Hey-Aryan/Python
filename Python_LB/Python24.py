# ----  Digits Problem  ----
# ---- Count Even Digits ----
# its count and not display 

def CountEvenNumbers(No):
    iDigit = 0
    iCnt = 0
    
    while(No != 0):
        iDigit = No % 10
        if(iDigit % 2 == 0):
            iCnt = iCnt + 1
        No = No // 10
    return iCnt

def main():
    Value = int(input("Enter the number : "));
    iRet = 0

    iRet = CountEvenNumbers(Value)

    print("Number of even digits are : ",iRet)

if __name__ == "__main__":
    main()