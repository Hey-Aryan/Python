# Maximum number 
# Find The maximum number from user input arr 


def MaxNumber(array,length):
    iMax = 0
    for i in range(length):
        if(array[i] > iMax):
            iMax = array[i]

    return iMax

def main():
    Arr = []
    Length = int(input("Enter the length of the list : "))

    print("Enter",Length,"Elements")
    for i in range (Length):
        Value = int(input())
        Arr.append(Value)

    Ret = MaxNumber(Arr,Length)

    print("Maximum Number in the List is : ",Ret)



if __name__ == "__main__":
    main()

