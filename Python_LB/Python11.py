#Additon of Factors

def AddFactors(No):
    iSum = 0
    for i in range(1,No):
        if(No % i == 0):
            iSum = iSum + i
    return iSum

def main():
    iRet = 0
    Value = int(input("Enter the Number : "))
    iRet = AddFactors(Value)
    print("Summation of factors are : ",iRet)

if __name__ == "__main__":
    main()



