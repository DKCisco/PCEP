

studentNames = ["Ben", "Diane", "Sam", "Pat"]

print(studentNames)
print(studentNames[2])

for name in studentNames:
    print(name)
    

studentNames.append("Joe")

for name in studentNames:
    print(name)

studentNames.remove("Sam")

for name in studentNames:
    print(name)
    
studentTuple = ("Lori", "Kate", "David")
print(studentTuple[1])

studentSet = {"Alan", "Steven", "Bridget"}

for name in studentSet:
    print(name) # Sets are unordered
