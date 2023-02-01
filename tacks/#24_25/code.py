
A = "Osama",
print(A[0])
print(type(A))
print("**********************************************************")

# -------------------------task2----------------------------------------
friends = ("Osama", "Ahmed", "Sayed")
lst = list(friends)
lst[0] = "Elzero"
t = tuple(lst)
print(lst)
print(type(t))
print(f"{len(t)} Elemants")


print("**********************************************************")

# -------------------------task2----------------------------------------
nums = (1, 2, 3)
letters = ("A", "B", "C")

total = nums + letters
print(f"nums_and_letters_one = {total}")
print(f"{len(total)} Elemants")

print("**********************************************************")

# -------------------------task2----------------------------------------
my_tuple = (1, 2, 3, 4)

a, b, _, c = my_tuple

print(a)
print(b)
print(c)

print("**********************************************************")
