import encodings
from itertools import product
import os
from unicodedata import name
from unittest import result
from pprint import pprint
file_name = 'recepies.txt'
def cook_book_dict(file_name):
    with open(file_name, encoding='utf_8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish_name = line.strip()
            print(dish_name)       
            ingredient_name = []
            for item in range(int(file_obj.readline())):
                ingredient = file_obj.readline() 
                ingredient_name.append(ingredient.strip().split('|'))
            cook_book[dish_name] = ingredient_name
            # print(f"Item - {file_obj.readline()}")
            file_obj.readline()  # Чтение пустой строки, чтобы перейти в нужный магазин
            # name_key = ['ingredient_name', 'quantity', 'measure']
            # print(ingredient_name)
            for item in  ingredient_name:
            #     pprint(ingredient_name[1][0])
            #   product_dict = {
                # 'ingredient_name':ingredient_name[0],
                #  'quantity':ingredient_name[1],
                #  'measure':ingredient_name[2]
            #         }
            # pprint(product_dict)
            


    return cook_book
pprint(cook_book_dict(file_name))

