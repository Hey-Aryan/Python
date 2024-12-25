# Frequency of n numbers 

def ChkFrequency(Brr,length,No):
    iCnt = 0
    for i in range(length):
        if(No == Brr[i]):
            iCnt = iCnt + 1
    return iCnt

def main():
    iRet = 0
    Arr = list()
    Length = int(input("Enter the number of elements: "))

    print("Enter",Length,"the Elements")

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    number = int(input("Enter the number you wanna check : "))

    iRet = ChkFrequency(Arr,Length,number)

    print("Frequency is : ",iRet)

if __name__ == "__main__":
    main()