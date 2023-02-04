import tkinter as tk
from tkinter import messagebox
from generaterecipe import generate

def show_recipe_step(index):
    recipe_label.config(text=recipe[index], wraplength=500)
    back_button.config(state="normal" if index > 0 else "disabled")
    next_button.config(state="normal" if index < len(recipe) - 1 else "disabled")
    global current_step
    current_step = index

def go_back():
    show_recipe_step(current_step - 1)

def go_next():
    show_recipe_step(current_step + 1)

def get_ingredients():
    ingredients = textbox.get().split(',')
    global recipe
    test1 = generate()
    recipe = test1.generate_recipe(ingredients)
    global current_step
    current_step = 0
    print(recipe[0])
    print(recipe[1])
    show_recipe_step(current_step)

root = tk.Tk()
root.title("Recipe Generator")
root.geometry("1440x900")

header = tk.Label(root, text="MasterChef", font=("TkDefaultFont", 16))
header.pack(pady=10)

label = tk.Label(root, text="Enter ingredients separated by commas:")
label.pack(pady=10)

textbox = tk.Entry(root, width = 50)
textbox.pack(pady=10)

button = tk.Button(root, text="Generate Recipe", command=get_ingredients)
button.pack(pady=10)

recipe_frame = tk.Frame(root)
recipe_frame.pack(pady=10)

back_button = tk.Button(recipe_frame, text="<", command=go_back, state="disabled")
back_button.pack(side="left", padx=10)

recipe_label = tk.Label(recipe_frame, text="", wraplength=500)
recipe_label.pack(side="left", padx=10)

next_button = tk.Button(recipe_frame, text=">", command=go_next, state="disabled")
next_button.pack(side="left", padx=10)

root.mainloop()