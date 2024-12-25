# Write a program which contains filter(), map(), and reduce() in it
# Python application contains one list of numbers. List contains 
# the numbers which are accepted from user. Filter should should 
# filter out all such numbers which greater than or equal to 70 
# and less than or equal to 90. Map functions will increase each number 
# by 10. Reduce will return product of all that numbers. 
from functools import reduce

def Function1(No):
    if(No >= 70 and No <= 90):
        return True 
    else:
        return False

def Function2(No):
    return No + 10

def Function3(A,B):
    return A*B
    


def main():
    Arr = []
    Length = int(input("Enter the Length "))
    print("Enter the Elements ")

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    print("Entered Array is ",Arr)

    output1 = list(filter(Function1,Arr))
    print(output1)

    output2 = list(map(Function2,output1))
    print(output2)
    print(type(output2))

    output3 = reduce(Function3,output2)
    print(output3)
    print(type(output3))
    

if __name__ == "__main__":
    main()