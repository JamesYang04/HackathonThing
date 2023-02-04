import json
import random

def sortCompressedDishes(compDish):
    return -compDish['MatchNum']

def sortOut(out):
    return sorted(out, key=sortCompressedDishes)