# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# def show_skills(*skills):

#   print(type(skills))

#   for skill in skills:

#     print(f"{skill}")


# show_skills("Html", "CSS", "JS")

mySkills = {
    'Html': "80%",
    'Css': "70%",
    'Js': "50%",
    'Python': "80%",
    "Go": "40%"
}


def show_skills(**skills):

    print(type(skills))

    for skill, value in skills.items():

        print(f"{skill} => {value}")


show_skills(**mySkills)


# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------+===================================

# myTuple = ("Html", "CSS", "JS")

# mySkills = {
#     'Go': "80%",
#     'Python': "50%",
#     'MySQL': "80%"
# }


# def show_skills(name, *skills, **skills_p):

#     print(f"Hello {name} \nSkills without progress: ")

#     for skill in skills:

#         print(f"- {skill}")

#     print("Skills with progress : ")

#     for skill_key, skill_value in skills_p.items():

#         print(f"- {skill_key} =>  {skill_value}")


# show_skills("osama", *myTuple, ** mySkills)


# --------------------
# -- Function Scope --
# --------------------=========================================

# x = 1  # Global Scope


# def one():

#     global x

#     x = 2

#     print(f"Print Variable From Function Scope {x}")


# def two():

#     x = 10

#     print(f"Print Variable From Function Scope {x}")


# one()
# print(f"Print Variable From Global Scope {x}")
# two()
# print(f"Print Variable From Global Scope After One Function Is Called {x}")


# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x[1:])


def cleanWord(word):

  if len(word) == 1:

    return word

  print(f"Print Start Function {word}")

  if word[0] == word[1]:

    print(f"Print Before Condition {word}")

    return cleanWord(word[1:])

  print(f"Print Before Return {word}")

  return word[0] + cleanWord(word[1:])

  # Stash [ World ]


print(cleanWord("WWWoooorrrldd"))


# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def say_hello(name, age): return f"Hello {name} your Age Is: {age}"


hello = lambda name, age : f"Hello {name} your Age Is: {age}"


print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))
