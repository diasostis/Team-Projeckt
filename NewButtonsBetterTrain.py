# import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from tkinter import *
from collections import Counter


# Command functions

def clicksum():
    # num of survivors plot
    plt.figure()
    sns.countplot(x="Survived", data=TitanicData, palette="winter")
    plt.show()


# num of survivors gender wise plot
def clickgender():
    plt.figure()
    sns.countplot(x="Survived", hue="Sex", data=TitanicData, palette="winter")
    plt.show()


# class of survivors plot
def clickclass():
    plt.figure()
    sns.countplot(x="Survived", hue="Class", data=TitanicData, palette="winter")
    plt.show()


# age of survivors plot
def clickage():
    plt.figure()
    sns.countplot(x="Survived", hue="Age", data=TitanicData, palette="winter")
    plt.show()


def createreport():
    X = TitanicData[["Class", "Age", "Sex"]]
    Y = TitanicData["Survived"]

    # convert categorical cols to numeric
    TitanicData.replace({"Survived": {"Yes": 1, "No": 0}, "Sex": {"Male": 0, "Female": 1},
                         "Class": {"First": 1, "Second": 2, "Third": 3, "Crew": 4},
                         "Age": {"Adult": 0, "Child": 1}},
                        inplace=True)

    # split data to training and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    # Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Prediction
    prediction = model.predict(X_test)

    newwdw = Toplevel(wdw)
    classre = classification_report(Y_test, prediction)
    classRetxt = Label(newwdw, text=("Classification Report", "\n", classre), bg="white", fg="black",
                       font="none 30 bold")
    classRetxt.grid(row=0, column=1, sticky=W)


def creatematrix():
    # convert categorical cols to numeric
    TitanicData.replace({"Survived": {"Yes": 1, "No": 0}, "Sex": {"Male": 0, "Female": 1},
                         "Class": {"First": 1, "Second": 2, "Third": 3, "Crew": 4},
                         "Age": {"Adult": 0, "Child": 1}},
                        inplace=True)

    X = TitanicData[["Class", "Age", "Sex"]]
    Y = TitanicData["Survived"]

    # split data to training and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)

    # Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Prediction
    prediction = model.predict(X_test)

    newwdw = Toplevel(wdw)
    matrix = confusion_matrix(Y_test, prediction)
    matrixtxt = Label(newwdw, text=("Confusion Matrix", "\n", matrix), bg="white", fg="black", font="none 30 bold")
    matrixtxt.grid(row=0, column=1, sticky=W)


def createscore():
    # convert categorical cols to numeric
    TitanicData.replace({"Survived": {"Yes": 1, "No": 0}, "Sex": {"Male": 0, "Female": 1},
                         "Class": {"First": 1, "Second": 2, "Third": 3, "Crew": 4},
                         "Age": {"Adult": 0, "Child": 1}},
                        inplace=True)

    X = TitanicData[["Class", "Age", "Sex"]]
    Y = TitanicData["Survived"]

    # split data to training and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)

    # Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Prediction
    prediction = model.predict(X_test)

    newwdw = Toplevel(wdw)
    score = accuracy_score(Y_test, prediction)
    scoretxt = Label(newwdw, text=("Accuracy score", score), bg="white", fg="black", font="none 40 bold")
    scoretxt.grid(row=0, column=1, sticky=W)


def traintestsplit():
    #convert categorical cols to numeric
    TitanicData.replace({"Survived": {"Yes": 1, "No": 0}, "Sex": {"Male": 0, "Female": 1},
                         "Class": {"First": 1, "Second": 2, "Third": 3, "Crew": 4},
                         "Age": {"Adult": 0, "Child": 1}},
                        inplace=True)

    X = TitanicData[["Class", "Age", "Sex"]]
    Y = TitanicData["Survived"]

    # split data to training and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)

    # Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    newwdw = Toplevel(wdw)
    text = Label(newwdw, text=(Counter(Y), "1490 not survived is 67.69% of 2201 passengers "
                                           "and 711 survived is 32.3% of 2201.", "\n",
            Counter(Y_train), "1191 not survived is 67.67% of 1760 passengers which is the train data "
                                    "and 569 survived is 32.32% of train data", "\n",
            Counter(Y_test), "299 not survived is 67.8% of 441 passengers which is the test data and "
                             "142 survived is 32.19% of test data"), bg="white", fg="black", font="none 15 bold")
    text.grid(row=0, column=1, sticky=W)


# close window
def closewdw():
    wdw.destroy()


# # Mouse hover functions
def hover_in(e):
    e.widget["bg"] = "OrangeRed"


def hover_out(e):
    e.widget["bg"] = "black"


# Initiate window
wdw = Tk()

# Background photo & Icon bitmap
bg = PhotoImage(file="Titanic-computergraphic2011.png")
wdw.iconbitmap("titanicbitmap.ico")

my_label = Label(wdw, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Window Config
wdw.title("ΠΛΗΠΡΟ - Project Titanic")
wdw.attributes("-fullscreen", True)

# Project title
titanic = Label(wdw, text="TITANIC", bg="black", fg="white", font="Times 30 italic bold")
titanic.grid(row=0, column=1, sticky=W)

# Button sum of survivors
survivors = Button(wdw, text="Sum Of Survivors", bg="black", fg="white",
                   font="none 16 bold", width=15, command=clicksum)
survivors.grid(row=0, column=2, sticky=W)
survivors.bind("<Enter>", hover_in)
survivors.bind("<Leave>", hover_out)

# Button gender
gender = Button(wdw, text="Sum Of Survivors Gender wise", bg="black", fg="white",
                font="none 16 bold", width=25, command=clickgender)
gender.grid(row=0, column=3, sticky=W)
gender.bind("<Enter>", hover_in)
gender.bind("<Leave>", hover_out)

# Button class
class_survivors = Button(wdw, text="Sum Of Survivors Class wise", bg="black", fg="white",
                         font="none 16 bold", width=25, command=clickclass)
class_survivors.grid(row=0, column=4, sticky=W)
class_survivors.bind("<Enter>", hover_in)
class_survivors.bind("<Leave>", hover_out)

# Button age
age = Button(wdw, text="Sum Of Survivors Age wise", bg="black", fg="white",
             font="none 16 bold", width=25, command=clickage)
age.grid(row=0, column=5, sticky=W)
age.bind("<Enter>", hover_in)
age.bind("<Leave>", hover_out)

# Button Classification Report
classRe = Button(wdw, text="Classification Report", bg="black", fg="white",
                 font="none 16 bold", width=20, command=createreport)
classRe.grid(row=1, column=2, sticky=W)
classRe.bind("<Enter>", hover_in)
classRe.bind("<Leave>", hover_out)

# Button Confusion Matrix
matrix = Button(wdw, text="Confusion Matrix", bg="black", fg="white",
                font="none 16 bold", width=18, command=creatematrix)
matrix.grid(row=1, column=3, sticky=W)
matrix.bind("<Enter>", hover_in)
matrix.bind("<Leave>", hover_out)

# Button Accuracy Score
score = Button(wdw, text="Accuracy Score", bg="black", fg="white", font="none 16 bold", width=20, command=createscore)
score.grid(row=1, column=4, sticky=W)
score.bind("<Enter>", hover_in)
score.bind("<Leave>", hover_out)

# Button Train_Test_Split
tts = Button(wdw, text="Train_Test_Split", bg="black", fg="white", font="none 16 bold", width=20,
             command=traintestsplit)
tts.grid(row=1, column=5, sticky=W)
tts.bind("<Enter>", hover_in)
tts.bind("<Leave>", hover_out)

# Button Exit
quit = Button(wdw, text="EXIT", bg="red", fg="white", font="none 20 bold", width=10, height=5, command=closewdw)
quit.grid(row=10, column=10, sticky=E)
quit.bind("<Enter>", hover_in)
quit.bind("<Leave>", hover_out)

# # load data from xlsx
TitanicData = pd.read_excel("Project38Titanic.xlsx")
TitanicData = pd.DataFrame(TitanicData, columns=["Class", "Age", "Sex", "Survived"])

# # drop 2 & 3 row
TitanicData = TitanicData.drop(TitanicData.index[0:2])

# # reset df index
TitanicData = TitanicData.reset_index(drop=True)

wdw.mainloop()
