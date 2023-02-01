

# def remove_chars(char):

#     return char[1:-1]


# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list = map(remove_chars, friends_map)


# for i in cleaned_list:
#     print(i)


# By lambda fun :

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# cleaned_list = map(lambda name: name[1:-1], friends_map)


# for i in cleaned_list:
#     print(i)


# ======================task 2 ==================================

from functools import reduce
from unicodedata import name


def get_name(name):

    # if str(name[0:-1]) == "m":

    return str(name[-1:]) == "m"


# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# names = filter(get_name, friends_filter)

# for i in names:

#     print(i)

# By lambda fun :


# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# names = filter(lambda name: str(name[-1:]) == "m", friends_filter)

# for i in names:

#     print(i)


# ========================Task 3 ===================================================

def sup(num1, num2):

    return num1 * num2


nums = [2, 4, 6, 2, 2]
print(reduce(sup, nums))

# By lambda Function

nums = [2, 4, 6, 2, 2]
print(reduce(lambda num1, num2:  num1 * num2, nums))

# -------------------task 4 ===================================================

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
re_skills = list(reversed(skills))

for c, skill in enumerate(re_skills, start=50):

    if isinstance(skill, int):
        continue
    else:
        print(f"{c} - {skill}")
