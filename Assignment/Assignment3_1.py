# Write a Program Which accepts N numbers from user and store
# it into LIST. Return Addition of all elements from that List

def Summation(Brr,length):
    iSum = 0

    for i in range(length):
        iSum = iSum + Brr[i]
    return iSum

def main():
    Arr = list()
    iRet = 0
    print("Enter the Length of the list : ")
    Length = int(input())

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    iRet = Summation(Arr,Length)

    print("Addition of elements is : ",iRet)
    

if __name__ == "__main__":
    main()