# here there is no self executable line 
# on indentation 0

def Addition(No1,No2):
    Result = 0
    Result = No1 + No2
    return Result


def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))

    Answer = 0
    Answer = Addition(Value1,Value2)

    print("Additon is : ",Answer)

