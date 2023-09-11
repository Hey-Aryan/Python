#Write a program which conatins one function named as ADD()
#which accepts two numbers from user and return addition 
# of that two numbers

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans


def main():
    print("Enter first Number :")
    Value1= int(input())

    print("Enter Second Number :")
    Value2= int(input())

    Ret = Add(Value1,Value2)

    print("Additon is : ",Ret)


if __name__== "__main__":  # Starter Call for main
    main()