# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []


# for data, x in zip(my_list, my_tuple):

#     print(data+x, end="")
#     # print(x, end="")


# ==========================task2==========================================

# from PIL import Image
# # from email.mime import image
# # from turtle import xcor


# my_list1 = ["E", "L", "Z"]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):

#     print(item2 + item3, end="")


# ==================task 3 =================================================


# myImage = Image.open("elzero-pillow.png")

# # myImage.show()

# myBox = (400, 0, 800, 400)
# myNewImage = myImage.crop(myBox)

# # myNewImage.show()


# myConverted = myNewImage.convert("L")
# myConverted.show()
# myNewImage.save("newInage.png")


# =================================task 4 =====================================

from pydoc import doc


def say_hello_to(name):
    """
    "parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    """
    return f"Hello {name}"


print(say_hello_to("Osama"))  # "Hello Osama"


print(say_hello_to.__doc__)

print(help(say_hello_to))


#===========================task 5 ===========================================

