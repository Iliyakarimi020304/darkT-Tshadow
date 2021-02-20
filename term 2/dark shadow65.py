import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='L1', font=('times', 20),width=5)
label.grid(row=0, column=0)
label = tk.Label(root, text='L2', font=('times', 20),width=5)
label.grid(row=0, column=1)
label = tk.Label(root, text='L3', font=('times', 20),width=5)
label.grid(row=1, column=0)
label = tk.Label(root, text='L3', font=('times', 20),width=5)
label.grid(row=1, column=1)
label = tk.Label(root, text='L4', font=('times', 20),width=5)
label.grid(row=3, column=1)

root.mainloop()