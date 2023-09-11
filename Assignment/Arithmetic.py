def Add(No1,No2):
    iAns = 0
    iAns = No1 + No2
    return iAns

def Sub(No1,No2):
    iAns = 0
    iAns = No1 - No2
    return iAns

def Mult(No1,No2):
    iAns = 0
    iAns = No1 * No2
    return iAns

def Div(No1,No2):
    iAns = 0
    iAns = No1 / No2
    return iAns


def factorial(No):
    iMult = 1
    for i in range(No,0,-1):  #1*2*3*4*5
        iMult = iMult * i

    return iMult