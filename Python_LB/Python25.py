# Count Even and Odd Digits 

def CountEvenOdd(No):
    iDigit = 0
    iEvenCnt = 0
    iOddCnt = 0

    if(No < 0):  # Updater
        No = -No

    if(No == 0):  # Filter
        iEvenCnt = iEvenCnt + 1
    

    while(No != 0):
        iDigit = No % 10
        if(iDigit % 2 == 0):
            iEvenCnt = iEvenCnt + 1
        else:
            iOddCnt = iOddCnt + 1
        No = No // 10
    print("Number of Even Digits are : ",iEvenCnt)
    print("Number of Odd Digits are : ",iOddCnt)
            

def main():
    Value = int(input("Enter the number : "))

    CountEvenOdd(Value)

if __name__ == "__main__":
    main()