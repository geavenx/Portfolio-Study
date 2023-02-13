import random
import string
from tkinter import *

root = Tk()
root.title("Very Simple Password Generator")

alphaLowercase = list(string.ascii_lowercase)
alphaUppercase = list(string.ascii_uppercase)
numbers = list(string.digits)
specialCharacters = list('!@#%&*()`¨^')

# função obter
def obter():
    lenghtUppercase = int(uppercaseEntry.get())
    lenghtLowercase = int(lowercaseEntry.get())
    lenghtNumbers = int(numbersEntry.get())
    lenghtSpecialCharacters = int(specialCharacterEntry.get())
    password = []

    for x in range(lenghtUppercase):
        password.append(random.choice(alphaUppercase))
    for x in range(lenghtLowercase):
        password.append(random.choice(alphaLowercase))
    for x in range(lenghtNumbers):
        password.append(random.choice(numbers))
    for x in range(lenghtSpecialCharacters):
        password.append(random.choice(specialCharacters))

    random.shuffle(password)
    random.shuffle(password)
    print("".join(password))

    root.clipboard_clear()

    finalAnswer = Label(root, text=password)
    finalAnswer.grid(row=4, column=1)

    def copy():
        root.clipboard_clear()
        root.clipboard_append("".join(password))
    copyButton = Button(root, text="Copy to Clipboard",
                        command=copy, height=1, width=20)
    copyButton.grid(row=5, column=1)


# entry
uppercaseEntry = Entry(root)
uppercaseEntry.grid(row=0, column=1)
lowercaseEntry = Entry(root)
lowercaseEntry.grid(row=1, column=1)
numbersEntry = Entry(root)
numbersEntry.grid(row=2, column=1)
specialCharacterEntry = Entry(root)
specialCharacterEntry.grid(row=3, column=1)


# label
uppercaseLabel = Label(root, text="Enter uppercase count in password: ")
uppercaseLabel.grid(row=0, column=0)
lowercaseLabel = Label(root, text="Enter lowercase count in password: ")
lowercaseLabel.grid(row=1, column=0)
numbersLabel = Label(root, text="Enter number count in password: ")
numbersLabel.grid(row=2, column=0)
specialCharactersLabel = Label(
    root, text="Enter special character count in password: ")
specialCharactersLabel.grid(row=3, column=0)

# button
button = Button(root, text="Create Password!",
                command=obter, height=1, width=20)
button.grid(row=4, column=0)
closeButton = Button(
    root, text="Exit", command=root.destroy, height=1, width=20)
closeButton.grid(row=5, column=0)

root.mainloop()