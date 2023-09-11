# Write a program which accept N numbers from user and store it into list
# Return Maximun number from that list

def Maximum(Brr,length):
    iMax = 0
    for i in range(length):
        if(Brr[i]>iMax):
            iMax = Brr[i]
    return iMax

def main():
    Arr = list()
    iRet = 0
    Length = int(input("Enter the Length of List : "))

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    iRet = Maximum(Arr,Length)

    print("Maximum number is :",iRet)

if __name__ == "__main__":
    main()