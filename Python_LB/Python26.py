# Reverse the Digits 

def Reverse(No):
    iDigit = 0
    iRev = 0

    if(No < 0 ):
        No = -No

    while(No != 0):
        iDigit = No % 10
        iRev = (iRev*10) + iDigit 
        No = No // 10  
    return iRev

def main():
    Value = int(input('Enter the number you want to reverse : '))
    iRet = 0

    iRet = Reverse(Value)

    print("Reversed Digits are : ",iRet)

if __name__ == "__main__":
    main()


    