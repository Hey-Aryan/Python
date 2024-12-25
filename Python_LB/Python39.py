# Accept n numbers from user and display even and odd count
# Variation 2


def ChkEven(Brr,length):
    iCnt = 0
    for i in range(length):
        if(Brr[i] % 2 == 0):
            iCnt = iCnt + 1
    return iCnt 

def main():
    iRet = 0
    Arr = list()
    Length = int(input("Enter the number of elements : "))

    print("Enter",Length,"Elements :")
    for i in range(Length):
        Value = int(input())
        Arr.append(Value)
    
    iRet = ChkEven(Arr,Length)

    print("Total numbers of Even numbers are : ",iRet)
    print("Total numbers of Odd numbers are : ",Length-iRet)

    

if __name__ == "__main__":
    main()