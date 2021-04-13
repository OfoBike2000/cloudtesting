import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

apps = []

def addApp():
    filename = filedialog.askopenfile(intialdir="/", tittle="Select File",
                                    filetypes=(("executabeles","*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.

canvas = tk.Canvas(root, height=500, width=500, bg="#263D52")
canvas.pack()

frame = tk.Frame(root,bg="light Grey")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="light Grey", bg="#263D42", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="light Grey", bg="#263D42")

runApps.pack()

root.mainloop()

