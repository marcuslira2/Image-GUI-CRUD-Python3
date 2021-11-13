import tkinter  # from tkinter import Tk for Python 3.x
import tkinter.filedialog as fd

tkinter.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = fd.askopenfilenames() # show an "Open" dialog box and return the path to the selected file
print(filename)
