# Count Digits
# Variation 2
# updater

def CountDigits(No):
    iDigit = 0
    iCnt = 0
    i = 0

    if (No < 0):  #updater
        No = - No

    while(No != 0):
        iDigit = No % 10
        No = No // 10
        iCnt = iCnt + 1
    return iCnt

def main():
    iRet = 0
    Value = int(input("Enter the number : "))

    iRet = CountDigits(Value)

    print("Total Number of Digits are : ",iRet)

if __name__ == "__main__":
    main()

