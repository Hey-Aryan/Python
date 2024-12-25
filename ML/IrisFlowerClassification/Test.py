import numpy as np 

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array1)

column = np.array([10,11,12])

# Function 
#array1 = np.delete(arr, 1, axis =1 )

# Parameters 
# arr = array in which deletion is to be performed 
# index position of either row or either column 
# 

arr = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
print(arr)

narr = np.delete(arr,4,axis = 1) # horizontal
print("Deleted array : ",narr)