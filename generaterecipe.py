import json
import sortFunc

class generate:
    def generate_recipe(self, ingredients, mode):

        f = open('recipes_with_nutritional_info.json')
        data = json.load(f)

        assumed = ["leavening agents", "spices", "wheat flour", "sugars", "water", "oil", "butter", "salt", "rice flour", "vinegar", "honey"]
        out = []
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
                    elif ing in sList[0]:
                        found = True
                        customCount += 1
                        break
                    elif sList[0] in ing:
                        found = True
                        customCount += 1
                        break
                if not found or customCount == 0:
                    can = False
                    break
            
            if can:
                """
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
        return ret"""

                #Format: 
                #[Title (string), Ingredients (string list), Nutrition Facts (dictionary string -> string), Link (string), MatchNum]

                #Title
                compressedDish = {}
                compressedDish['Title'] = dish['title']

                #Ingredients
                temp = []
                N = len(dish['ingredients'])
                for i in range(0, N):
                    s = dish['ingredients'][i]['text']
                    qty = dish['quantity'][i]['text']
                    unit = dish['unit'][i]['text']
                    temp.append(qty + " " + unit + " " + s)
                compressedDish['Ingredients'] = temp

                #Nutrition Facts
                temp = {}
                energy = 0
                fat = 0
                protein = 0
                salt = 0
                saturates = 0
                sugars = 0
                for i in range(0, N):
                    fat += dish['nutr_per_ingredient'][i]['fat']
                    energy += dish['nutr_per_ingredient'][i]['nrg']
                    protein += dish['nutr_per_ingredient'][i]['pro']
                    saturates += dish['nutr_per_ingredient'][i]['sat']
                    salt += dish['nutr_per_ingredient'][i]['sod']
                    sugars += dish['nutr_per_ingredient'][i]['sug']
                
                temp['Fat'] = fat
                temp['Energy'] = energy
                temp['Protein'] = protein
                temp['Salt'] = salt
                temp['Saturates'] = saturates
                temp['Sugars'] = sugars

                compressedDish['Nutrition Facts'] = temp

                #Link
                compressedDish['Link'] = dish['url']

                #MatchNum
                compressedDish['MatchNum'] = customCount

                out.append(compressedDish)

        #outside dish forloop
        #returns sorted list of compressed dishes
        sMode = sortFunc.sortMode.NORMAL
        if mode == "Normal": sMode = sortFunc.sortMode.NORMAL
        if mode == "High Calories": sMode = sortFunc.sortMode.HICAL
        if mode == "Low Calories": sMode = sortFunc.sortMode.LOWCAL
        if mode == "Low Sugar": sMode = sortFunc.sortMode.LOWSUG
        if mode == "Low Salt": sMode = sortFunc.sortMode.LOWSOD
        if mode == "High Protein": sMode = sortFunc.sortMode.HIPRO
        if mode == "Low Fats": sMode = sortFunc.sortMode.LOWFAT
        return sortFunc.sortOut(out, sMode)









