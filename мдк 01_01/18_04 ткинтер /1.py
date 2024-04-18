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

# Словарь с соответствием названия цвета и его кода в шестнадцатеричной системе
colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff"
}

def insert_color_code(color):
    color_code = colors[color]
    color_entry.delete(0, tk.END)
    color_entry.insert(tk.END, color_code)
    color_label.config(text=color)

# Создание графического интерфейса
root = tk.Tk()
root.title("Цвета радуги")

# Создание метки для отображения названия цвета
color_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), pady=10)
color_label.pack()

# Создание текстового поля для отображения кода цвета
color_entry = tk.Entry(root, font=("Helvetica", 12), width=10, state="readonly")
color_entry.pack()

# Создание кнопок для каждого цвета
for color in colors:
    button = tk.Button(root, text=color, bg=colors[color], padx=10, pady=5, font=("Helvetica", 10),
                       command=lambda c=color: insert_color_code(c))
    button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()