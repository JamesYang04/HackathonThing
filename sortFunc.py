import json
import random
from enum import Enum

class sortMode(Enum):
    NORMAL = 0
    HICAL = 1
    LOWCAL = 2
    LOWSUG = 3
    LOWSOD = 4
    HIPRO = 5
    LOWFAT = 6
    


def sortCompressedDishesNORMAL(compDish):
    return -100*compDish['MatchNum']

def sortCompressedDishesHICAL(compDish):
    return -100*compDish['MatchNum'] - compDish['Nutrition Facts']['Energy']

def sortCompressedDishesLOWCAL(compDish):
    return -100*compDish['MatchNum'] + compDish['Nutrition Facts']['Energy']

def sortCompressedDishesLOWSUG(compDish):
    return -100*compDish['MatchNum'] + compDish['Nutrition Facts']['Sugars']

def sortCompressedDishesLOWSOD(compDish):
    return -100*compDish['MatchNum'] + compDish['Nutrition Facts']['Salt']

def sortCompressedDishesHIPRO(compDish):
    return -100*compDish['MatchNum'] - compDish['Nutrition Facts']['Protein']

def sortCompressedDishesLOWFAT(compDish):
    return -100*compDish['MatchNum'] + compDish['Nutrition Facts']['Fat'] 

def sortOut(out, mode):
    if (mode == sortMode.NORMAL): return sorted(out, key=sortCompressedDishesNORMAL)
    if (mode == sortMode.HICAL): return sorted(out, key=sortCompressedDishesHICAL)
    if (mode == sortMode.LOWCAL): return sorted(out, key=sortCompressedDishesLOWCAL)
    if (mode == sortMode.LOWSUG): return sorted(out, key=sortCompressedDishesLOWSUG)
    if (mode == sortMode.LOWSOD): return sorted(out, key=sortCompressedDishesLOWSOD)
    if (mode == sortMode.HIPRO): return sorted(out, key=sortCompressedDishesHIPRO)
    if (mode == sortMode.LOWFAT): return sorted(out, key=sortCompressedDishesLOWFAT)
    
