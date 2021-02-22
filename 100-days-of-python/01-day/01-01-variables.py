#Get some info about variables.

name = "Jack" 
print(name)

name = "Angela"
print(name)

name = input("What is your name? ")
length = len(name)
print("Your name is", name, "\nIt's length", length, "chars")

cup1 = "cofee"
cup2 = "tea"
cup3 = cup1
cup1 = cup2
cup2 = cup3

print(cup1, cup2)