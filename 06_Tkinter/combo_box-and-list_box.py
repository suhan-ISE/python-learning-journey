import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tkinter App") # title

#label
label = ttk.Label(window, text="Hello World", font=("Times New Romen", 10, "bold")
                  , padding=5)
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
quit.pack(pady=5)

# SEPARATOR
sep = ttk.Separator(window, orient="horizontal")
sep.pack(fill="x")

# text input for description.

text = tk.Text(height=5, width=20)
text.pack(pady=5)
text.focus() # for cursor
text.insert("1.0", "enter your text here") #default text


def text_function():
    text_data = text.get("1.0", "end")
    print(text_data)

text_button = ttk.Button(text="get text", command=text_function)
text_button.pack()

#checkbutton
check_option =tk.StringVar()

def check_option_task():
    print(check_option.get())
check_button = ttk.Checkbutton(text="agree with terms and condition",variable=check_option,command=check_option_task,
                               onvalue="tick", offvalue="untick")
check_button.pack()

# Radiobutton
radio_value = tk.StringVar()
def radio_option_task():
    print(radio_value.get())
option_1 = ttk.Radiobutton(text="Male", value="male",variable=radio_value,command=radio_option_task).pack()
option_2 = ttk.Radiobutton(text="Female", value="female",variable=radio_value, command=radio_option_task).pack()

# combo boxes
selected_countries = tk.StringVar()
country_names = ("india", "USA", "canada", "japan","germany")
countries = ttk.Combobox(textvariable=selected_countries,values =country_names )
countries["state"] = "readonly"
countries.pack()

def display_country(event):
    msg = f"the selected country is \"{selected_countries.get()}\""
    country_label = ttk.Label(text=msg)
    country_label.pack()
    #print(f"the selected country is \"{selected_countries.get()}\"")

countries.bind("<<ComboboxSelected>>", display_country)

# listbox
food_items = ("pizza","french fries","bav bhaji","tea","coffee")
fav_food= tk.StringVar(value = food_items)
food_list = tk.Listbox(listvariable=fav_food,height=5,selectmode="multiple")
food_list.pack()

def display_food(event):
    food_indices  = food_list.curselection()
    for food in food_indices:
        print(food_list.get(food))
food_list.bind("<<ListboxSelect>>", display_food)

window.mainloop()