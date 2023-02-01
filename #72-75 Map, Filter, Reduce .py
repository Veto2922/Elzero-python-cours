# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------


from functools import reduce


def formatText(taxt):

    return f"- {taxt.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "sAYed  "]

myFormatedData = map(formatText, myTexts)


# print(myFormatedData)

for name in myFormatedData:

    print(name)

print("#" * 40)

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):

    print(name)


# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumber(num):

    return num > 10


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for number in myResult:

    print(number)


print("#" * 50)


# Example 2

def checkname(name):

    return str(name).startswith("O")


myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myResult = filter(checkname, myTexts)

for name in myResult:

    print(name)


print("#" * 50)


# Example 3

# def checkname(name):

#     return str(name).startswith("O")


myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ammer"]

myResult = filter(lambda name: name.startswith("A  "), myNames)

for name in myResult:

    print(name)


# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------


def sumAll(num1, num2):

    return num1 + num2


numbers = [1, 8, 2, 9, 100]

# result = reduce(sumAll, numbers)

# print(result)


result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)


# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------=============================================

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:

    print(f"{counter} - {skill}")

print("#" * 50)

# help()

# print(help(print))

print("#" * 50)


# reversed(iterable)

myString = "Elzero"


print(reversed(myString))

for letter in reversed(myString):

    print(letter)

for s in reversed(mySkills):

    print(s)
