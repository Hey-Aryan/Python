# Write a program which accept N numbers from user and store it 
# into List. Accept one another number from user and return frequency of that number from list 


def Frequency(Brr,length,No):
    iCnt = 0
    for i in range (length):
        if(Brr[i] ==  No):
            iCnt = iCnt + 1
    return iCnt 

def main():
    Arr = list()
    element = 0
    iRet = 0

    Length = int(input("Enter the Length of List : "))

    print("Enter the Elements :")

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)
    
    element = int(input("Enter the element to find frequency of : "))

    iRet = Frequency(Arr,Length,element)

    print("Frequency is : ", iRet)


if __name__=="__main__":
    main()