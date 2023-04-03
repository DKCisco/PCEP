
file_object = open("output.txt", mode="w")

print("Hello Ben!", file=file_object)

print("Hello", "Ben ","ThirdValue", sep=":")

print("Hello", end="")
print("Goodbye")

print("Hello", "Ben ","ThirdValue", end="\n", sep=":")
