import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

label1 = tk.Label(root, text="Widget 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Widget 2")
label2.grid(row=1, column=1)

root.mainloop()
