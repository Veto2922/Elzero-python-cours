# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

# x = [1, 2, 3, 4, []]

# if all(x):

#     print("All Elements Is True")

# else:

#     print("Theres At Least One Element Is False")


# x = [0, 0, []]

# if any(x):

#     print("There's At Least One Element is True")

# else:

#     print("Theres No Any True Elements")

# print(bin(100))

# a = 1
# b = 2

# print(id(a))
# print(id(b))


# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------============================================

# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 40))


# round(number, numofdigits)
print(round(150.501))
print(round(150.554, 2))

# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))


# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ")

print("First Line", end=" ")
print("Second Line")
print("Third Line")


# ------------------------
# -- Built In Functions --
# ------------------------===========================================
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------============================================

# abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 50)

# pow(base, exp, mod) => Power
print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10

print("#" * 50)


# min(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "Osama"))
print(min(myNumbers))

print("#" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "Osama"))
print(max(myNumbers))

print("#" * 50)


# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
