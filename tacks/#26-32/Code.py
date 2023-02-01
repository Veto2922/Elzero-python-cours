
my_list = [1, 2, 3, 3, 4, 5, 1]

Unique_list = [1, 2, 3, 4, 5]

print(Unique_list)
print(type(Unique_list))
print(Unique_list[0:4])

print("*"*100)
# -------------------------task 2-----------------------------------------\
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print(nums | letters)
print(nums.difference(letters))


print("*"*100)

# -------------------------task 3-----------------------------------------\
my_set = {1, 2, 3}
letters = {"A", "B", "C"}


print(my_set)

print(my_set.clear())
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")

print("*"*100)

# -------------------------task 4-----------------------------------------\
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

print("*"*100)
# -------------------------task 5-----------------------------------------\
skills = {
    "one": "HTML Progress Is 90%",
    "two": "CSS Progress Is 80%",
    "three": "Python Progress Is 30%",
    "four": "AI Progress Is 20%"
}

print(skills["one"])
print(skills["two"])
print(skills["three"])
print(skills["four"])

skills["five"] = "C++ progress is 50%"
print(skills["five"])
print("*"*100)
