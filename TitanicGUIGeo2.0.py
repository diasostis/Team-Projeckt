from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



# Command functions

def clicksum():
    # num of survivors plot
    plt. figure()
    sns.set()
    sns.countplot(x="Survived", data=TitanicData, palette="winter")
    plt.show()


def clickgender():
    plt. figure()
    # num of survivors gender wise plot
    sns.countplot(x="Survived", hue="Sex", data=TitanicData, palette="winter")
    plt.show()
 


def clickclass():
    plt. figure()
    # class of survivors plot
    sns.countplot(x="Survived", hue="Class", data=TitanicData, palette="winter")
    plt.show()



def clickage():
    plt. figure()
    # age of survivors plot
    sns.countplot(x="Survived", hue="Age", data=TitanicData, palette="winter")
    plt.show()
    

def closewdw():
    wdw.destroy()

# # Mouse hover functions
def hover_in(e):
    e.widget["bg"] = "OrangeRed"

def hover_out(e):
    e.widget["bg"] = "black"


# load data from xlsx
TitanicData = pd.read_excel("Project38Titanic.xlsx")
TitanicData = pd.DataFrame(TitanicData, columns=["Class", "Age", "Sex", "Survived"])

# drop 2 & 3 row
TitanicData = TitanicData.drop(TitanicData.index[0:2])

# reset df index
TitanicData = TitanicData.reset_index(drop=True)

# Initiate window
wdw = Tk()

bg=PhotoImage(file="Titanic-computergraphic2011.png")
wdw.iconbitmap("321886.ico")

my_label=Label(wdw,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

# Window Config
wdw.title("ΠΛΗΠΡΟ - Project Titanic")
#wdw.configure(bg="black")
wdw.attributes("-fullscreen", True)

# Project title
titanic = Label(wdw, text="TITANIC", bg="black", fg="white", font="none 24 bold")
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
class_survivors = Button(wdw, text="Class Of Survivors", bg="black", fg="white",
                   font="none 16 bold", width=15, command=clickclass)
class_survivors.grid(row=0, column=4, sticky=W)
class_survivors.bind("<Enter>", hover_in)
class_survivors.bind("<Leave>", hover_out)


# Button age
age = Button(wdw, text="Age Of Survivors", bg="black", fg="white",
                   font="none 16 bold", width=15, command=clickage)
age.grid(row=0, column=5, sticky=W)
age.bind("<Enter>", hover_in)
age.bind("<Leave>", hover_out)


# Button Exit
quit = Button(wdw, text="EXIT", bg="red", fg="white", font="none 20 bold", width=10, height=5, command=closewdw)
quit.grid(row=10, column=10, sticky=E)
quit.bind("<Enter>", hover_in)
quit.bind("<Leave>", hover_out)


wdw.mainloop()