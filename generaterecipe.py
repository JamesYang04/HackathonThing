import random
import json

class generate:
    def generate_recipe(self, ingredients):
        # Available recipes
        f = open('recipes_with_nutritional_info.json')
        data = json.load(f)

        for dish in data:
            need = dish['ingredients']
            can = True
            for t in need:
                found = False
                string = t['text']
                for ing in ingredients:
                    if ing in string:
                        found = True
                        break
                if not found:
                    can = False
                    break
            if can:
                print("We can make " + dish['title'])
                print("Follow the following recipe: ")
                i = 1
                for steps in dish['instructions']:
                    step = steps['text']
                    print(str(i) +  ")" + step)
                    i+=1
                print("\n")


