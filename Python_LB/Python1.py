# Additon of two numbers 

def Addition(No1,No2):
    Ans = No1 + No2
    return Ans


def main():
    Value1 = int(input("Enter the first number :"))
    Value2 = int(input("Enter the second number :"))
    iAdd = 0
    iAdd = Addition(Value1,Value2)
    print("Addition is ",iAdd)
if __name__ == "__main__":
    main()