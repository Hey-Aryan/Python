# Write a program which accept one number and return Addition of its factors
# 12 % 1  == 0
# 12 % 2  == 0
# 12 % 3  == 0       1 + 2 + 3 + 4 + 6 + = 16 
# 12 % 4  == 0
# 12 % 5  == 2
# 12 % 6  == 0
# 12 % 7  == 5
# 12 % 8  == 4
# 12 % 9  == 3
# 12 % 10 == 2
# 12 % 11 == 1
       

def AddFactors(No):
    iAdd = 0
    for i in range(1,No):
        if(No % i == 0):
            iAdd = iAdd + i
    return iAdd


def main():
    iRet = 0
    Value = int(input("Enter the number : "))

    iRet = AddFactors(Value)
    print("Addition of ",Value,"Factors is ",iRet)

if __name__ == "__main__":
    main()