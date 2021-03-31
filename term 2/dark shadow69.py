import tkinter as tk
root = tk.Tk()
def up():
    global temp
    temp += 1
    fan()


def dn():
    global temp
    temp -= 1
    fan()







tk.Label(root, text='temperature').grid(row=0, column=0)
button = tk.Button(root, text=">", command=up)
button.pack
button1 = 



root.mainloop()