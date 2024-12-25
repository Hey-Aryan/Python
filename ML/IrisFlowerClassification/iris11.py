import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()
# Features / Independent Variables 
print("Feature names of iris data set")
print(iris.feature_names)

#Target = Labels / Dependent Variables
print("Target names of iris data set") 
print(iris.target_names) 

# Indices of removed elements
test_index = [1,2,3,4,5,51,52,53,54,55,101,102,103,104,105] # testing data set

# Training data with removed elements
train_Labels = np.delete(iris.target,test_index)
train_Feature = np.delete(iris.data,test_index,axis=0) #axis = horizontal = 0; vertical = 1

# Testing data for testing on trainning data
test_Labels = iris.target[test_index]   # D
test_Feature = iris.data[test_index]       # C

# form decision tree classifier
VarunChaModel = tree.DecisionTreeClassifier() # A B 

# Apply training data to form tree
VarunChaModel.fit(train_Feature,train_Labels) # (A B)

print("Values that we removed for testing")
print(test_Labels)    # D

print("Result of testing")
print(VarunChaModel.predict(test_Feature)) # E

















