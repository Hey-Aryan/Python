# Write a program which accept N numbers from user and store it into List
# Return addition of all prime numbers from that List()
# Main python file accept N numbers from user and pass each to 
# chkPrime() function which is part of our user defined module named as 
# marvellousNum Name of the function from main python file should be 
# ListPrime()

import MarvellousNum

def main():
    Arr = list()
    iRet = 0
    Value = 0
    Length = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    iRet = MarvellousNum.ChkPrime(Arr,Length)

    print("Addition of prime numbers is : ",iRet)

if __name__ =="__main__":
    main()
    