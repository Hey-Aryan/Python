# Write a prorgram which conatins one lambda function 
# which accepts one parameter ad return power of two

# Name = lambda + Parameters + Function Logic  
Square = lambda No: No * No

def main():
    Ret = 0
    Value = int(input("Enter the number : "))
    Ret = Square(Value) # Lambda function call
    print("Power of 2 = ",Ret)

if __name__ == "__main__":
    main()