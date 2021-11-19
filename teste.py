import tkinter
import tkinter.filedialog as fd


janela = tkinter.Tk()
canvas = tkinter.Canvas(janela, width=800, height=800)
canvas.pack()
filepath = fd.askopenfilenames()
print(len(filepath))
lista ={}
print(len(lista))
for i in range(len(filepath)):
    lista[i] = tkinter.PhotoImage(file=filepath[i])
for l in range(len(filepath)):
    canvas.create_image((l + 1) * 100,  50, image=lista[l])
tkinter.mainloop()
