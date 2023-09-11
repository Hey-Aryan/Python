# Create a module named Arithmetic which contains 4 functions 
# Add() , Sub() , Mult() , Div() 
# All functions accept 2 parameters and perfor the operation
# Write a code to call all functions 
# Input from user 
import Arithmetic

def main():
    iRet = 0
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))
    
    iRet = Arithmetic.Add(Value1,Value2)
    print("Addition is : ",iRet)

    iRet = Arithmetic.Sub(Value1,Value2)
    print("Substraction is : ",iRet)

    iRet = Arithmetic.Mult(Value1,Value2)
    print("Multiplication is : ",iRet)

    iRet = Arithmetic.Div(Value1,Value2)
    print("Division is : ",iRet)


if __name__ =="__main__":
    main()

 