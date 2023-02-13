from tkinter import *
import tkinter as tk


root = Tk()
root.title("Tkinter Calculator")
root.geometry("312x324")
root.resizable(0,0)

def buttonClick(item):
    global count
    count = count + str(item)
    inputText.set(count)

def clearClick():
    global count
    count = ""
    inputText.set("")

def equalClick():
    global count
    result = str(eval(count))
    inputText.set(result)
    count = ""

# variables
inputText = StringVar()
count = ""

# frames
inputFrame = Frame(root, width=312, height=50)
inputFrame.pack(side=TOP)
buttonFrame = Frame(root, width=312, height=272.5, bg='gray')
buttonFrame.pack()

# entries
inputField = Entry(inputFrame, textvariable=inputText, width=50, bg="#eee", bd=0, justify=RIGHT, font=('arial', 18, 'bold'))
inputField.grid(row=0, column=0)
inputField.pack(ipady=10)

# buttons
buttonClear = Button(buttonFrame, text='C', fg='black', width=32, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: clearClick()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
buttonDivide = Button(buttonFrame, text='/', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick('/')).grid(row=0, column=3, padx=1, pady=1)
buttonMultiplier = Button(buttonFrame, text='*', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick('*')).grid(row=1, column=3, padx=1, pady=1)
buttonPlus = Button(buttonFrame, text='+', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick('+')).grid(row=2, column=3, padx=1, pady=1)
buttonMinus = Button(buttonFrame, text='-', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick('-')).grid(row=3, column=3, padx=1, pady=1)
buttonEqual = Button(buttonFrame, text='=', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: equalClick()).grid(row=4, column=3, padx=1, pady=1)

buttonSeven = Button(buttonFrame, text='7', fg='black', width=10, height=3, bd=0, bg="#eee", cursor='hand2', command= lambda: buttonClick(7)).grid(row=1, column=0, padx=1, pady=1)
buttonEight = Button(buttonFrame, text='8', fg='black', width=10, height=3, bd=0, bg="#eee", cursor='hand2', command= lambda: buttonClick(8)).grid(row=1, column=1, pady=1, padx=1)
buttonNine = Button(buttonFrame, text='9', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(9)).grid(row=1, column=2, pady=1, padx=1)

buttonFour = Button(buttonFrame, text='4', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(4)).grid(row=2, column=0, pady=1, padx=1)
buttonFive = Button(buttonFrame, text='5', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(5)).grid(row=2, column=1, pady=1, padx=1)
buttonSix = Button(buttonFrame, text='6', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(6)).grid(row=2, column=2, pady=1, padx=1)

buttonOne = Button(buttonFrame, text='1', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(1)).grid(row=3, column=0, pady=1, padx=1)
buttonTwo = Button(buttonFrame, text='2', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(2)).grid(row=3, column=1, pady=1, padx=1)
buttonThree = Button(buttonFrame, text='3', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(3)).grid(row=3, column=2, pady=1, padx=1)

buttonZero = Button(buttonFrame, text='0', fg='black', width=32, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: buttonClick(0)).grid(row=4, column=0, pady=1, padx=1, columnspan=3)


root.mainloop()