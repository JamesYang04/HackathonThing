import tkinter as tk
from generaterecipe import generate

def get_ingredients():
    ingredients = textbox.get().split(',')
    test1 = generate()
    recipe = test1.generate_recipe(ingredients)
    result_label.config(text=recipe)

root = tk.Tk()
root.title("Recipe Generator")
root.geometry("400x400")

label = tk.Label(root, text="Enter ingredients separated by commas:")
label.pack(pady=10)

textbox = tk.Entry(root)
textbox.pack(pady=10)

button = tk.Button(root, text="Generate Recipe", command=get_ingredients)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()