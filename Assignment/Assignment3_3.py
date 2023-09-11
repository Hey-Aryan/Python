# Write a program which accept N numbers from user and store it 
# into List. Return Minimun Number from  that List

def Minimun(Brr,length):
    iMin = 99999999999
    for i in range(length):
        if(Brr[i] < iMin):
            iMin = Brr[i]
    return iMin

def main():
    Arr = list()
    iRet = 0
    Length = int(input("Enter the Length of List : "))

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    iRet = Minimun(Arr,Length)

    print("Minimun number is :",iRet)

if __name__ == "__main__":
    main()