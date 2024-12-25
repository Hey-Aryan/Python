# Command Line Arguments 
import sys  #argv argc in this module

def main():
    print("Demonstration of Command Line Arguments")
    print("Number of command line arguments are :",len(sys.argv)) 
    print("First Argument  : ",sys.argv[0]) 
    print("Second Argument : ",sys.argv[1]) 
    print("Third Argument  : ",sys.argv[2]) 
    

    # len(sys.argv) == length of array




if __name__ == "__main__":
    main()


#python3 Command1.py Marvellous 11