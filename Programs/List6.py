# Accept n numbers and store that in List and display


def main():

    print("Enter Number of elements taht you want to store :")
    Length=int(input())

    Arr = list() # dynamically create the (object) empty list 

    print("Enter the elements : ")
    for i in range(Length):
        value = int(input())
        Arr.append(value)    # method used to append while allocating the memory dynamically

    print("Elements from List are : ")
    for i in range(Length):
        print(Arr[i])

if __name__ == "__main__":
    main()

# As and when memory gets allocated 
# append = insert last 
# append = default module
# ek ek add hote in append and not directly 6 allocate hote