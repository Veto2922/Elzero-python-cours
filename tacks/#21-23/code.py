
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends.pop(0))


print(friends[3])
print(friends.pop(3))

print("***********************************************************************")

# *****************************task2*****************************************
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0::2])
print(friends[1::2])

print("***********************************************************************")

# *****************************task3*****************************************

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4:1])
print(friends[3:5:1])


print("***********************************************************************")

# *****************************task4*****************************************
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
list_b = ["Elzero", "Elzero"]

friends.remove("Ali")
friends.remove("Mahmoud")
friends.extend(list_b)
print(friends)


print("***********************************************************************")

# *****************************task5*****************************************

friends = ["Osama", "Ahmed", "Sayed"]

friends.append("salem")
friends.insert(0, "nasser")

print(friends)


print("***********************************************************************")

# *****************************task6*****************************************
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)


print("***********************************************************************")

# *****************************task7*****************************************
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)

print("***********************************************************************")

# *****************************task8*****************************************
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)


print("***********************************************************************")
# *****************************task9*****************************************
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

len(friends)
print(len(friends))

print("***********************************************************************")

# *****************************task10*****************************************
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[4][0])
print(technologies[4][2])


print("***********************************************************************")
