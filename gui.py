import tkinter as tk
from tkinter import messagebox
from generaterecipe import generate

class RoundedTextbox(tk.Canvas):
    def __init__(self, parent, radius=10, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)

        self.radius = radius

        self.rect = self.create_rectangle(0, 0, self.winfo_width(), self.winfo_height(),
                                          fill="white", width=1, outline="black")
        self.text = self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                                     text="", anchor="center")

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        x1, y1, x2, y2 = self.coords(self.rect)
        self.coords(self.rect, 0, 0, event.width, event.height)
        self.coords(self.text, event.width / 2, event.height / 2)

    def insert(self, index, char):
        self.itemconfigure(self.text, text=self.itemcget(self.text, "text") + char)

def parseRecipe(rr):
    ret = "You can make " + rr['Title'] + "!\n\n"
    ret += "Ingredients: " + ' ,'.join(rr['Ingredients']) + "\n\n"
    ret += "Nutritional Facts:\n"
    for cat in rr['Nutrition Facts'].keys():
        ret += cat + " " + str(rr['Nutrition Facts'][cat]) + '\n'
    return ret

def show_recipe_step(index):
    recipe_label.config(text=parseRecipe(recipe[index]), wraplength=500)
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
    show_recipe_step(current_step)

root = tk.Tk()
root.title("Recipe Generator")
root.geometry("1440x900")

header = tk.Label(root, text="TBD NAME", bg="lightblue", font=("TkDefaultFont", 20), height=5)
header.pack(fill="x")

spacer = tk.Frame(root, height=20)
spacer.pack(fill="x")

label = tk.Label(root, text="Enter ingredients separated by commas:")
label.pack(pady=10)

textbox = tk.Entry(root, width = 50)
textbox.pack(pady=10)

button = tk.Button(root, text="Generate Recipe", command=get_ingredients)
button.pack(pady=10)

recipe_frame = tk.Frame(root)
recipe_frame.pack(pady=10)

back_button = tk.Button(recipe_frame, text="<", command=go_back, state="disabled")
back_button.pack(side="left", padx=10, pady=10)

recipe_label = tk.Label(recipe_frame, text="", wraplength=500, justify=tk.LEFT)
recipe_label.pack(side="left", padx=10)

next_button = tk.Button(recipe_frame, text=">", command=go_next, state="disabled")
next_button.pack(side="left", padx=10, pady=10)

root.mainloop()