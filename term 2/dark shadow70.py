import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)
# ##########################
patients = ttk.Frame(note)
note.add(patients, text='patients')
timers = ttk.Frame(note)
note.add(timers, text="Timers")
# ###########################################################
lf1 = tk.LabelFrame(patients, text="patient 1")
lf1 = grid(row=0, column=0)

tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Time').grid(row=1, column=0)
name1 = tk.StringVar()
time1 = tk.StringVar()
tk.Entery(lf1, textvariable=name1).grid(row=0, column=1)
tk.Entery(lf1, textvariable=time1).grid(row=0, column=1)
# ###########################################################
root.mainloop()