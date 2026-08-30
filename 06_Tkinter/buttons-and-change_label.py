import tkinter as tk

window = tk.Tk()
window.title("My Tkinter App")

label = tk.Label(text="Hello World!")
label.pack()
window.minsize(400, 300) # minimum size of the window.
label["text"] = "Have a nice day!"
label.config(font="Arial", fg="white", bg="red")
label.config(text="myself suhan khan k !")
# the labeled text will get replaced.



count = 0 # to count how many times the button is clicked
def button_clicked():
    global count
    count = count + 1
    label["text"] = f"button clicked {count} times!"
# creating button widget in the window.
button = tk.Button(text="Click me",command=button_clicked)
# command takes actions from the given function.
button.pack()
window.mainloop()