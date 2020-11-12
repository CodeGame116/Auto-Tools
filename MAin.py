from tkinter import *
import pyautogui


window = Tk()
Label(text = "KeyPresser", bg = "grey", width = "300", font = ("Calibri", 13)).pack()
a = True
name = StringVar()
Entry(window, textvariable = name).pack()
yo = name.get()
Button(window, text = "Submit").pack()
def Start():
    while a == True:
        pyautogui.press(name.get())
def Stop():
    a = False

window.title("Auto Tools")

Label(text = "", bg = "red").pack()
Button(text = "Start", height = "2", width = "30", command = Start).pack()
Label(text = "", bg = "red").pack()
Button(text = "Stop", height = "2", width = "30", command = Stop).pack()
Label(text = "", bg = "red").pack()
a = True

def Start():
    while a == True:
        pyautogui.click(pyautogui.position())
def Stop():
    a = False
window.geometry("300x675")
Label(text = "", bg = "red").pack()
Label(text = "Autoclicker", bg = "grey", width = "300", font = ("Calibri", 13)).pack()
Label(text = "", bg = "red").pack()
Button(text = "Start", height = "2", width = "30", command = Start).pack()
Label(text = "", bg = "red").pack()
Button(text = "Stop", height = "2", width = "30", command = Stop).pack()
Label(text = "", bg = "red").pack()
window.configure(background = "red")

Label(text = "TextSpammer", bg = "grey", width = "300", font = ("Calibri", 13)).pack()
OBS = StringVar()
Entry(window, textvariable = OBS).pack()
yo = name.get()
Button(window, text = "Submit").pack()
# Test HEHEH
def Start():
    while a == True:
        pyautogui.typewrite(OBS.get())
        pyautogui.press("enter")
def Stop():
    a = False
Label(text = "", bg = "red").pack()
Button(text = "Start", height = "2", width = "30", command = Start).pack()
Label(text = "", bg = "red").pack()
Button(text = "Stop", height = "2", width = "30", command = Stop).pack()
Label(text = "", bg = "red").pack()


window.mainloop()
