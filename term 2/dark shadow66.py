import tkinter as tk

 


frame = tk.Frame(root)

l1 = tk.Label(root, text='Weight')
l1.grid(row=0, column=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)

l2 = tk.Button(root, text='Height')
l2.grid(row=1, column=0)
e2 = tk.Button(root)
e2.grid(row=1, column=1)




root.mainloop()