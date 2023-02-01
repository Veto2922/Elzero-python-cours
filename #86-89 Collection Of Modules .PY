
# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------


list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}


for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

    print("List 1 Item =>", item1)
    print("List 2 Item =>", item2)
    print("Tuple 1 Item =>", item3)
    print("Dict 1 Key =>", item4, "Value =>", dict1[item4])


# ultimateList = zip(list1, list2)
# print(ultimateList)


# for item in ultimateList:
#     print(item)


# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------=============================
# from PIL import Image
# from email.mime import image

# myImage = image.open("Blackbear.2019.1080p.WEBRip.x264-[YTS.LT].jpg")

# myImage.show()


# # My Cropped Image
# myBox = (300, 300, 800, 800)
# myNewImage = myImage.crop(myBox)

# # Show The New Image
# myNewImage.show()

# # My Converted Mode Image
# myConverted = myImage.convert("L")
# myConverted.show()


# --------------------------------------------=============================
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------


# def elzero_function(name):
#     """
# Elzero Function
#   It Say Hello From Elzero
# Parameter:
#   name => Person Name That Use Function
# Return:
#   Return Hello Message To The Person
# """
#     print(f"Hello {name} From Elzero")


# elzero_function("Ahmed")

# print(dir(elzero_function))

# print(elzero_function.__doc__)

# help(elzero_function)


# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# -----------------------------------------------

"""
This is My Module
To Create Function
To Say Hello
"""


def sayHello(name):

    msg = "Hello"

    return f"{msg} {name}"


sayHello("Ahmed")
