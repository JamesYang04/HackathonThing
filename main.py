from generaterecipe import generate
import gui as gui
gui
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

test = generate()
ingredients = ['apples', 'chicken', 'salmon']
Ingredients= ["butter", "sugar", "750g luxury mixed dried fruit (one that includes mixed peel and glac\u00e9 cherries)", "finely grated zest and juice of 1 orange", "finely grated zest of 1 lemon", "100ml/3\u00bd fl oz cherry brandy or brandy plus 4tbsp more", "85g macadamia nut", "3 large eggs, lightly beaten", "85g ground almond", "200g plain flour", "\u00bd tsp baking powder", "1 tsp ground mixed spice", "1 tsp ground cinnamon", "\u00bc tsp ground allspice"]
recipe = test.generate_recipe(ingredients)
