import ntpath
import tkinter
import tkinter.filedialog as fd


janela = tkinter.Tk()
canvas = tkinter.Canvas(janela, width=200, height=200)
canvas.pack()
filepath = fd.askopenfilenames()
print(filepath)
lista ={}
print(len(lista))

for i in range(len(filepath)):
    lista[i] = tkinter.PhotoImage(file=filepath[i])
    print(lista[i])
for l in range(len(filepath)):
    canvas.create_image((l + 1) * 100,  50, image=lista[l])
print(filepath)
for v in range(len(filepath)):
    print(ntpath.basename(filepath[v]))
print(lista)
janela.geometry('800x640')
tkinter.mainloop()
