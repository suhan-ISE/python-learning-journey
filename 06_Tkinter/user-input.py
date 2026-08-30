import tkinter as tk
window = tk.Tk()
window.title("Tkinter App") # title

#label
label = tk.Label(window, text="Hello World", font=("Times New Romen", 20, "bold"))
label.pack()

# window size
window.minsize(400, 300)

# function to operate.
def button():
    user_text = user_input.get()
    label.config(text=user_text)

# user input
user_input = tk.Entry()
user_input.pack()

#button
button = tk.Button(text="click", command=button)
button.pack()

window.mainloop()
