#Import the Libraries
import numpy as np
import pandas as pd

#Importing the Dataset
Dataset = pd.read_csv("wine_weka_dataset.csv")
X = Dataset.iloc[:,:-1].values
y = Dataset.iloc[:,-1].values

#Lets Feature Scale the independent variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

#Splitting the dataset into training and testing and performing a good shuffle of data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 0.3, random_state =42, shuffle = True)

#Now lets define our Adaboost Classifier.
from sklearn.ensemble import AdaBoostClassifier
classifier = AdaBoostClassifier()
classifier.fit(X_train, y_train)

#Lets predict our test set results
y_pred = classifier.predict(X_test)

#Its time for evaluating our model.

from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
acc_train = accuracy_score(y_train, classifier.predict(X_train))
f1_train = f1_score(y_train, classifier.predict(X_train), average= 'weighted')

print("Traing set results")
print("ACCURACY ---------------------->",acc_train)
print("F1 SCORE ---------------------->",f1_train)

#Now lets see how well is our model. So now lets evaluate with our test set
acc_test = accuracy_score(y_test, y_pred)
f1_test = f1_score(y_test, y_pred, average= 'weighted')

print("Test set results")
print("ACCURACY ---------------------->",acc_test)
print("F1 SCORE ---------------------->",f1_test)

#Now lets have our famous Confusion Matrix to visually understand.
cm = confusion_matrix(y_test,y_pred)
print(cm)