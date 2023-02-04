import random
import json

class generate:
    def generate_recipe(self, ingredients):
        # Available recipes
        f = open('recipes.json')
        data = json.load(f)

        for dish in data:
            need = dish['Ingredients']
            can = True
            for string in need:
                found = False
                for ing in ingredients:
                    if ing in string:
                        found = True
                        break
                if not found:
                    can = False
                    break
            if can:
                print("We can make " + dish['Name'])
                print("Follow the following recipe: ")
                i = 1
                for step in dish['Method']:
                    print(str(i) +  ")" + step)
                    i+=1
                print("\n")


