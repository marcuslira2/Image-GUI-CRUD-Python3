import tkinter  # from tkinter import Tk for Python 3.x
import tkinter.filedialog as fd
import

janela = tkinter.Tk()  # we don't want a full GUI, so keep the root window from appearing
canvas = tkinter.Canvas(janela, width=800, height=800)
canvas.pack()
filepath = fd.askopenfilenames()  # show an "Open" dialog box and return the path to the selected file
print(len(filepath))
lista ={}
print(len(lista))
for i in range(len(filepath)):
    lista[i] = tkinter.PhotoImage(file=filepath[i])
for l in range(len(filepath)):
    canvas.create_image((l + 1) * 100,  50, image=lista[l])
tkinter.mainloop()
