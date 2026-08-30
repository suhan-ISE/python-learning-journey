# Step 1: Import the tkinter module
# Step 2: Create the main application window (root window)
# Step 3 (Optional but good practice): Set the window title
# Step 4: Create a widget - a Label widget to display text
# tk.Label(parent_widget, text="Your text here")
# Step 5: Arrange the widget using a layout manager (pack() is simplest for now)
# pack() places widgets in a block.
# Step 6: Start the Tkinter event loop
# This keeps the window open and responsive to user interactions
# This line will execute only after the Tkinter window is closed.

import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter App")
label = tk.Label(root, text="Hello, Myself suhan khan k!")
label.pack()
root.mainloop()
print("Application closed.")