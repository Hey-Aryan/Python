# UserDefined Function to create filter,map,reduce

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No: No+2
Add = lambda A,B: A+B

# Tasks     : Name of function
# Elements  : List of Data Elements 
def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

# Tasks     : Name of function
# Elements  : List of Data Elements 
def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

# Tasks     : Name of function
# Elements  : List of Data Elements 
def reduceX(Task, Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)
    return Sum


def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input data          ->",Data)

    output = list(filterX(CheckEven,Data))
    print("Ouput after filterX ->",output)

    moutput = list(mapX(Increase,output))
    print("Ouput after mapX    ->",moutput)

    result = reduceX(Add,moutput)
    print("Ouput after reduceX ->",result)

if __name__ == "__main__":
    main()


