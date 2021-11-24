import ntpath
import pathlib
import tkinter
import tkinter as tk
import tkinter.filedialog as fd
import os
import sqlite3

import app
import bd
janela = tkinter.Tk()
janela.geometry('840x640')
f3 = tk.Frame(janela)
f3.grid(column=0,row=0,stick='nsew')



canvas02 = tk.Canvas(f3, width=200, height=200,bg ='blue')

canvas02.grid(column=2,row=1)
try:

    connection = sqlite3.connect('./bancocadastro.db')
    cursor = connection.cursor()
    select = """SELECT * FROM imagem WHERE user =?"""
    cursor.execute(select, ['n'])
    result = cursor.fetchall()

except Exception as erro:
    print(erro)
finally:
    if connection:
        cursor.close()
        connection.close()
filepath = result[0][2]

print(filepath)
lista ={}
print(len(lista))
lista[0]= tk.PhotoImage(file=filepath)

print(lista[0])

canvas02.create_image(100,100,image=lista[0])

janela.mainloop()



