import tkinter as tk
import re

def numTransform(num):
    x = re.search("0[0-9][0-9]", num)
    print(x)

def loadGUI():
    window = tk.Tk()
    label = tk.Label(text="Name")
    entry = tk.Entry()
    label.pack()
    entry.pack()
    button = tk.Button(text="Click me!")
    button.pack()
    #window setup
    
    def handle_click(event):
        info = entry.get()
        window.destroy()
        print(f"You have chosen chapter {info}!")
        return info
    button.bind("<Button-1>", handle_click)
    #button function
    
    window.mainloop()
    #start window
#loadGUI()
numTransform("030")
    