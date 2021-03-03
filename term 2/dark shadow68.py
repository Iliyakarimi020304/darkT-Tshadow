import tkinter as tk
import tkinter.ttk as ttk
from typing import Text
import reg

def srch():
    pass




def register():
    reg.register(
        name.get(),
        last.get(),
        birth.get(),
        code.get(),
    )


root = tk.Tk()

tk.Label(root, text='name').grid(row=0, column=0)
name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Label(root, text='Last Name').grid(row=1, column=0)
last = tk.Entry(root)
last.grid(row=1, column=1)


tk.Label(root, text='Birth Date').grid(row=2, column=0)
birth = tk.Entry(root)
birth.grid(row=2, column=1)

tk.Label(root, text='ID code').grid(row=3, column=0)
code = tk.Entry(root)
code.grid(row=3, column=1)


frame = tk.Frame(root)
frame.grid(row=6, column=0, columnspan=2)

tk.Button(frame, text='register', command=register).grid(row=0, column=0)
tk.Button(frame, text='cancel', command=root.destroy).grid(row=0, column=1)

ttk.Separator(root,orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky="ew")
tk.label(root, text='sratch').grid(row=6, column=0)
search = tk.Entry(root)
search.grid(row=6, column=1)
tk.Button(root, text='Search, command=srch).grid(row=7, column=0, columnspan=2)

root.mainloop()
