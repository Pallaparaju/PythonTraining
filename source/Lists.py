# Introduction to Lists#
from typing import List

fruits = ['Banana', 'Oranges', 'Apples', 'Berries', 'Mangoes']
print(fruits)
print(fruits[0],fruits[1],fruits[3])
print(fruits[0:3])
fruits.append("Blackberries")
print(fruits)
fruits[0]='Cherries'
print(fruits)

del fruits[3]
print(fruits)
print(len(fruits))
print(fruits*10)

listnum = [1,26,29,100,89,67]
print(max(listnum), min(listnum))
print(fruits + listnum)