# import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# load data from xlsx
TitanicData = pd.read_excel("Project38Titanic.xlsx")
TitanicData = pd.DataFrame(TitanicData, columns=["Class", "Age", "Sex", "Survived"])

# drop 2 & 3 row
TitanicData = TitanicData.drop(TitanicData.index[0:2])

# reset df index
TitanicData = TitanicData.reset_index(drop=True)

# num of survivors // Sum
print(TitanicData["Survived"].value_counts())
print("\n")

# num of survivors plot
sns.set()
sns.countplot(x="Survived", data=TitanicData, palette="winter")
plt.show()

# num of Male / Female
print(TitanicData["Sex"].value_counts())
print("\n")

# num of survivors gender wise plot
sns.countplot(x="Survived", hue="Sex", data=TitanicData, palette="winter")
plt.show()

# num of Class
print(TitanicData["Class"].value_counts())
print("\n")

# num of survivors class wise plot
sns.countplot(x="Survived", hue="Class", data=TitanicData, palette="winter")
plt.show()

# num of Age
print(TitanicData["Age"].value_counts())
print("\n")

# num of survivors age wise plot
sns.countplot(x="Survived", hue="Age", data=TitanicData, palette="winter")
plt.show()

# convert categorical cols to numeric
TitanicData.replace({"Survived": {"Yes": 1, "No": 0}, "Sex": {"Male": 0, "Female": 1},
                     "Class": {"First": 1, "Second": 2, "Third": 3, "Crew": 4},
                     "Age": {"Adult": 0, "Child": 1}},
                    inplace=True)

# keep df of values except "Survived" and create a "Survived" one
X = TitanicData[["Class", "Age", "Sex"]].copy()
Y = TitanicData["Survived"]

# split data to training and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(" Data Shape\n", X.shape, X_train.shape, X_test.shape)
print("\n")

# Logistic Regression
model = LogisticRegression()
model.fit(X_train, Y_train)

# Prediction
prediction = model.predict(X_test)

# Classification Report
classre = classification_report(Y_test, prediction)
print(" Classification Report\n", classre)
print("\n")

# Confusion Matrix
mtrx = confusion_matrix(Y_test, prediction)
print(" Confusion Matrix\n", mtrx)
print("\n")

# Accuracy Score
accscr = accuracy_score(Y_test, prediction)
print(" Accuracy Score\n", accscr)
print("\n")
