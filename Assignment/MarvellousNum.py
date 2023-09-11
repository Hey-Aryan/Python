# This function Accepts List and check each  element in the list is 
# a prime number or not and if True then adds that element in iSum variable 

def ChkPrime(Brr,length):
    iSum = 0
    iCnt = 0
    No = 0
    for i in range(length):
        No = Brr[i]
        for i in range(1,No):
            if (No % i == 0):
                iCnt = iCnt + 1
        if(iCnt == 1):
            iSum = iSum + No
        iCnt = 0
    
    return iSum

    
