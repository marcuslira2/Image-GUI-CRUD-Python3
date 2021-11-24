import tkinter

import PIL

janela=tkinter.Tk()
canvas = tkinter.Canvas(janela,width=200,height=200,bg='red')
canvas.pack()

img = tkinter.PhotoImage(file='C:/Users/CLEIDE_PC/Pictures/Pokemon/32px-Pokémon_Fire_Type_Icon.svg.png')

canvas.create_image(100,100,image=img)

janela.mainloop()