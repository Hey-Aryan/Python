# Accept 5 numbers and display summation of that 


def main():
    iSum = 0

    print("Enter the length of List : ")
    length = int(input())

    print("Enter the elements : ")
    Arr = list()

    for i in range(length):
        value = int(input())
        Arr.append(value)
    print("Elements are : ")
    for i in range(length):
        iSum = iSum + Arr[i]
    print("Addition of 5 elements are : ",iSum)

if __name__ == "__main__":
    main()

