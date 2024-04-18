# from tkinter import *
#
#
# def change():
#     b1['text'] = "Изменено"
#     b1['bg'] = '#000000'
#     b1['fg'] = '#ffffff'
#     b1['activebackground'] = '#555555'
#     b1['activeforeground'] = '#ffffff'
#
#
# root = Tk()
# b1 = Button(text="Изменить", width=15, height=3)
# b1.config(command=change)
# b1.pack()
# root.mainloop()


import tkinter as tk
from tkinter import messagebox


def insert_color_code(event):
    color_button = event.widget
    color_name = color_button.cget("text")
    color_code = color_button.cget("bg")

    entry.insert(tk.END, f"{color_code}\n")
    label.config(text=f"{color_name}")


root = tk.Tk()
root.title("Радужные кнопки")

# Создаем семь кнопок с цветами радуги
red_button = tk.Button(root, text="Красный", bg="#ff0000", command=lambda: insert_color_code(None))
red_button.pack()

orange_button = tk.Button(root, text="Оранжевый", bg="#ff7d00", command=lambda: insert_color_code(None))
orange_button.pack()

yellow_button = tk.Button(root, text="Желтый", bg="#ffff00", command=lambda: insert_color_code(None))
yellow_button.pack()

green_button = tk.Button(root, text="Зеленый", bg="#00ff00", command=lambda: insert_color_code(None))
green_button.pack()

blue_button = tk.Button(root, text="Голубой", bg="#007dff", command=lambda: insert_color_code(None))
blue_button.pack()

indigo_button = tk.Button(root, text="Синий", bg="#0000ff", command=lambda: insert_color_code(None))
indigo_button.pack()

violet_button = tk.Button(root, text="Фиолетовый", bg="#7d00ff", command=lambda: insert_color_code(None))
violet_button.pack()

# Создаем текстовое поле для отображения кодов цветов
entry = tk.Text(root, height=10, width=40)
entry.pack()

# Создаем метку для отображения названий цветов
label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack()

# Запускаем главный цикл обработки событий
root.mainloop()