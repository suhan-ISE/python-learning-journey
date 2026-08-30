import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Tkinter App") # title

#label
label = ttk.Label(window, text="Hello World", font=("Times New Romen", 20, "bold"))
label.pack()

# window size
window.minsize(400, 300)

# function to operate.
def button():
    user_text = user_input.get()
    label.config(text=user_text)

# user input
user_input = ttk.Entry()
user_input.pack()

#button
button = ttk.Button(text="click", command=button)
button.pack()

#quitting
quit = ttk.Button(text="quit", command=window.destroy)
quit.pack()
window.mainloop()
