import tkinter as tk
import webbrowser
from generaterecipe import generate
from PIL import Image, ImageTk
import receipts
import math
def parseRecipe(rr):
    ret = "You can make " + rr['Title'] + "!\n\n"
    ret += "Ingredients: " + ' ,'.join(rr['Ingredients']) + "\n\n"
    ret += "Nutritional Facts:\n"
    for cat in rr['Nutrition Facts'].keys():
        if cat == 'Energy': ret += cat + " " + str(round(rr['Nutrition Facts'][cat])) + 'cal\n'
        else: ret += cat + " " + str(round(rr['Nutrition Facts'][cat])) + 'g\n'
    return ret

def show_recipe_step(index):
    recipe_label.config(text=parseRecipe(recipe[index]), wraplength=800)
    global link
    linkbutton.pack(pady=10)
    link = recipe[index]['Link']
    back_button.config(state="normal" if index > 0 else "disabled")
    next_button.config(state="normal" if index < len(recipe) - 1 else "disabled")
    global current_step
    current_step = index

def go_back():
    linkbutton.pack_forget()
    show_recipe_step(current_step - 1)

def go_next():
    linkbutton.pack_forget()
    show_recipe_step(current_step + 1)

def open_hyperlink():
    webbrowser.open_new(link)

def read_image():
    ingredients = receipts.grabReceipt()
    textbox.delete(0, tk.END)
    textbox.insert(0, ingredients)
        

def get_ingredients():
    ingredients = textbox.get().split(',')
    global recipe
    test1 = generate()
    recipe = test1.generate_recipe(ingredients)
    if len(recipe) == 0:
        recipe_label.config(text="Sorry, no recipe found", wraplength=800)
        back_button.config(state="disabled")
        next_button.config(state="disabled")
        back_button.pack_forget()
        next_button.pack_forget()
        linkbutton.pack_forget()
    else:
        global current_step
        current_step = 0
        recipe_label.pack_forget()
        back_button.pack(side="left", padx=10, pady=10)
        recipe_label.pack(side="left", padx=10)
        next_button.pack(side="left", padx=10, pady=10)
        show_recipe_step(current_step)

root = tk.Tk()
root.title("Recipe Generator")
root.geometry("1440x900")

image = Image.open("logo.png")
image = image.resize((600, 600), Image.LANCZOS)
image = ImageTk.PhotoImage(image)


header = tk.Label(root, image=image, bg="white", font=("TkDefaultFont", 30), height=180)
header.pack(fill="x")

spacer = tk.Frame(root, height=20)
spacer.pack(fill="x")

label = tk.Label(root, text="Enter ingredients separated by commas:")
label.pack(pady=10)

textbox = tk.Entry(root, width = 50)
textbox.pack(pady=10)

button = tk.Button(root, text="Generate Recipe", command=get_ingredients)
button.pack(pady=10)

button2 = tk.Button(root, text="Read Receipt", command=read_image)
button2.pack(pady=10)

recipe_frame = tk.Frame(root)
recipe_frame.pack(pady=10)

back_button = tk.Button(recipe_frame, text="<", command=go_back, state="disabled")

recipe_label = tk.Label(recipe_frame, text="", justify=tk.LEFT, font=("TkDefaultFont", 12), wraplength=800)
recipe_label.pack(side="left", padx=10)

next_button = tk.Button(recipe_frame, text=">", command=go_next, state="disabled")

linkbutton = tk.Button(root, text="Open Link", command=open_hyperlink, bg='lightblue')

root.mainloop()
