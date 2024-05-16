import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

con = sqlite3.connect("auto_shop.db")

window = Tk()
window.title("bibika.ru")
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

image = Image.open("main_photo.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(window, image=photo)
label.pack()

window.mainloop()