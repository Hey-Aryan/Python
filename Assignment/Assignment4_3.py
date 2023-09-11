# Write a program which contains filter(), map(), and reduce() in it
# Python application contains one list of numbers. List contains 
# the numbers which are accepted from user. Filter should should 
# filter out all such numbers which greater than or equal to 70 
# and less than or equal to 90. Map functions will increase each number 
# by 10. Reduce will return product of all that numbers. 

def main():
    Arr = []
    Length = int(input("Enter the Length "))
    print("Enter the Elements ")

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    print(Arr)

if __name__ == "__main__":
    main()