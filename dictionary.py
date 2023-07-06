

studentGrades = {"Ben": 92, "Diane": 97, "Sam": 81}

print(studentGrades["Diane"])

myCars = ({"Make": "Ford", "Model": "Model A", "Year": 2031, "colors":("blue", "grey")},
        {"Make": "Chevy", "Model": "Cavalier", "Year": 1997})

print(myCars[0]["colors"][1])

#for item in studentGrades:
#        print(studentGrades[item])

if "Ben" in studentGrades:
        print("It is!")
        
if 92 in studentGrades.values():
        print("92 is found in the values!")
        
values = studentGrades.values()
valuesList = list(values)
print(valuesList[1])

keys = studentGrades.keys()
keysList = list(keys)
print(keysList)

for i in range (0, len(values)):
        print(studentGrades[keysList[i]])
        
items = studentGrades.items()
itemsLists = list(items)
print(itemsLists[0][1])
