# Types of Functional Arguments in Python
#  1 Positional Arguments 
# --- Limitation ---
# data type is not specified caller callie has to manage it

def Display(Name, Age , Marks):
    print("Name is :",Name)
    print("Age is :",Age)
    print("Marks is :",Marks)

def main():
    print("Demonstration of Positional Arguments ")
    Display("Amit",25,89)
    Display("Sagar",21,78)

if __name__== "__main__":
    main()