#Dictionaries#

family = {"Raju":25, "Sreedhar":45, "Lakshmi":39}
print(family)
print('Age of Raju',family["Raju"],'\n' 'Age of my dad ',family["Sreedhar"], '\n''Age of my mom',family["Lakshmi"])

family["Lakshmi"]=40
print(family)
print("Number of members in my family are ",len(family))

del family["Raju"]
print("Parents are",family)