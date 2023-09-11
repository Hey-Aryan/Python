# Check Prime Number 

# 11 % 1  == 0
# 11 % 2  == 1
# 11 % 3  == 2      
# 11 % 4  == 3
# 11 % 5  == 1
# 11 % 6  == 5
# 11 % 7  == 4
# 11 % 8  == 3
# 11 % 9  == 2
# 11 % 10 == 1
       

def AddFactors(No):
    iCnt = 0

    if(No == 1):
        print("1 is neither a prime nor a composite number ")
        exit()

    for i in range(1,No):
        if(No % i == 0):
            iCnt = iCnt + 1
    if(iCnt == 1):
        return True
    else:
        return False


def main():
    bRet = 0
    Value = int(input("Enter the number : "))

    bRet = AddFactors(Value)
    if(bRet == True):
        print("Its a prime number ")
    else:
        print("Its not a prime number ")



if __name__ == "__main__":
    main()