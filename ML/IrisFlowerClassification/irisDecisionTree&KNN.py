# Iris Case study with decision tree and KNN

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 

def MarvellousCalculateAccuracyDecisionTree():

    iris = load_iris()

    data = iris.data
    target = iris.target 
    # A           C          B              D
    data_train, data_test, target_train, target_test = train_test_split(data,target,train_size=0.5,shuffle=True)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)
                                #D           #E
    Accuracy = accuracy_score(target_test,predictions)
                                
    return Accuracy


def MarvellousCalculateAccuracyKNeighbor():

    iris = load_iris()

    data = iris.data
    target = iris.target 
    # A           C          B              D
    data_train, data_test, target_train, target_test = train_test_split(data,target,train_size=0.5,shuffle=True)

    classifier = KNeighborsClassifier()

    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)
                                #D           #E
    Accuracy = accuracy_score(target_test,predictions)
                                
    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of classification algorithm with Decision Tree Classifier is",Accuracy*100,"%")

    Accuracy = MarvellousCalculateAccuracyKNeighbor()
    print("Accuracy of classification algorithm with K Neighbor Classifier is",Accuracy*100,"%")

if __name__ == "__main__":
    main()