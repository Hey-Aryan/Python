# Write a program which accept number from user and 
# return number of digits present in that number 

# 1234

def CntDigit(No):
    iDigit = 0
    iCnt = 0   # 1 2 3 4
    while(No != 0):
        iDigit = No % 10  # 1234 % 10 = 4  # 123 % 10 = 3 # 12 % 10 = 2 # 1 % 10 = 1
        iCnt = iCnt + 1   
        No = No // 10  # = 1234 // 10  = 123 // 10 = 12 // 10 = 1//10 = 0
        print(No)
    return iCnt

def main():
    iRet = 0
    Value = int(input("Enter the number : "))
    iRet = CntDigit(Value)
    print("Number of digits present in ",Value," = ",iRet)

if __name__ == "__main__":
    main()