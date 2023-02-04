import random
import json

class generate:
    def generate_recipe(self, ingredients):
        # Available recipes
        ret = ""
        f = open('recipes_with_nutritional_info.json')
        data = json.load(f)

        assumed = ["leavening agents", "spices", "wheat flour", "sugars", "water", "oil", "butter", "salt", "rice flour", "vinegar", "honey"]
        for dish in data:
            need = dish['ingredients']
            can = True
            customCount = 0
            for t in need:
                found = False
                string = t['text']
                sList = string.split(", ")
                for ing in ingredients:
                    if sList[0] in assumed:
                        found = True
                        break
                    if ing in sList[0]:
                        found = True
                        customCount += 1
                        break
                    if sList[0] in ing:
                        found = True
                        customCount += 1
                        break
                if not found or customCount == 0:
                    can = False
                    break
            if can:
                print("We can make " + dish['title'])
                ret += "We can make " + dish['title'] + '\n'
                print("using these ingredients: ")
                for i in range(1, len(dish['ingredients']) + 1):
                    s = dish['ingredients'][i-1]['text']
                    qty = dish['quantity'][i-1]['text']
                    unit = dish['unit'][i-1]['text']
                    print(str(i) +  ") " + qty + " " + unit + " " + s)
                    ret += str(i) +  ") " + qty + " " + unit + " " + s + '\n'
                print("\n")
                ret += '\n'
        return ret


