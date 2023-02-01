# ------------------------------------------
# -- Object Oriented Programming => Intro --
# ------------------------------------------
# [1] Python Support Object Oriented Programming
# [2] OOP Is A Paradigm Or Coding Style
#     OOP Paradigm =>
#       Means Structuring Program So The Methods[Functions] and Attributes[Data]
#       Are Bundled Into Objects
# [3] Methods => Act As Function That Use The Information Of The Object
# [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
#     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
#     - Functional => Built On the Concept of Mathematical Functions
# [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# [6] Everything in Python is Object
# [7] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# [8] If Car Is Object
#     - Attributes => Model, Colour, Price
#     - Methods[Behaviors] => Walking, Stopping
# [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
#     - Class Car Can Create Many Cars Object
# ---------------------------------------------


# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function


# class member:

#     def __init__(self) -> None:

#         print("A new member has been added")


# member_one = member()
# member_two = member()
# member_three = member()


# print(member_one.__class__)


# ================#105 oop=======================================
# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------


# class member:

#     def __init__(self, first_name, middle_name, last_name) -> None:

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name


# member_1 = member("Osama", "Mohamed", "Elsayed")
# member_2 = member("Ahmed", "Ali", "mahmoud")
# member_3 = member("Sayed", "Ahmed", "Abdel3al")

# # print(dir(member_1))

# print(member_1.fname, member_1.mname, member_1.lname)
# print(member_2.fname)

# print(member_3.fname)


# =====================Python درس 106# - ال OOP الجزء 4 - ال Instance Attributes + Methods===
# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------


# class member:

#     def __init__(self, first_name, middle_name, last_name, gender) -> None:

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender

#     def full_name(self):

#         return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_titles(self):

#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"

#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"

#         else:

#             return f"{self.fname}"

#     def get_all_info(self):

#         return f"{self.name_with_titles()} , Your full name is: {self.full_name()}"


# member_1 = member("Osama", "Mohamed", "Elsayed", "Male")
# member_2 = member("Ahmed", "Ali", "mahmoud", "Male")
# member_3 = member("mona", "Ahmed", "Abdel3al", "Female")

# # print(dir(member_1))

# # print(member_1.fname, member_1.mname, member_1.lname)
# # print(member_2.fname)

# # print(member_3.fname)


# # print(member_3.full_name())

# # print(member_3.name_with_titles())


# print(member_1.get_all_info())


# ==============================درس 107# - ال OOP الجزء 5 - ال Class Attributes===================
# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------


# class member:

#     not_allowed_names = ["Hell", "Shit", "Baloot"]

#     users_num = 0

#     def __init__(self, first_name, middle_name, last_name, gender) -> None:

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender

#         member.users_num += 1

#     def full_name(self):

#         if self.fname in member.not_allowed_names:

#             raise ValueError("Name Not Allowed")
#         else:
#             return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_titles(self):

#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"

#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"

#         else:

#             return f"{self.fname}"

#     def get_all_info(self):

#         return f"{self.name_with_titles()} , Your full name is: {self.full_name()}"

#     def delete_user(self):

#         member.users_num -= 1

#         return f"User {self.fname} Deleted."


# print(member.users_num)

# member_1 = member("Osama", "Mohamed", "Elsayed", "Male")
# member_2 = member("Ahmed", "Ali", "mahmoud", "Male")
# member_3 = member("mona", "Ahmed", "Abdel3al", "Female")
# member_4 = member("Hell", "Ahmed", "Abdel3al", "Female")

# print(member.users_num)

# print(member_4.delete_user())
# print(member.users_num)
# # print(dir(member_1))

# # print(member_1.fname, member_1.mname, member_1.lname)
# # print(member_2.fname)

# # print(member_3.fname)


# # print(member_3.full_name())

# # print(member_3.name_with_titles())


# print(member_1.get_all_info())

# # print(dir(member))


# ====================== درس 108# - ال OOP الجزء 6 - ال Class Methods And Static Methods
# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------


# class member:

#     not_allowed_names = ["Hell", "Shit", "Baloot"]

#     users_num = 0

#     @classmethod
#     def show_user_count(cls):

#         print(f"we Have {cls.users_num} User in our system")

#     @staticmethod
#     def say_hello():
#         print("Hello from static method")

#     def __init__(self, first_name, middle_name, last_name, gender) -> None:

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender

#         member.users_num += 1

#     def full_name(self):

#         if self.fname in member.not_allowed_names:

#             raise ValueError("Name Not Allowed")
#         else:
#             return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_titles(self):

#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"

#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"

#         else:

#             return f"{self.fname}"

#     def get_all_info(self):

#         return f"{self.name_with_titles()} , Your full name is: {self.full_name()}"

#     def delete_user(self):

#         member.users_num -= 1

#         return f"User {self.fname} Deleted."


# print(member.users_num)

# member_1 = member("Osama", "Mohamed", "Elsayed", "Male")
# member_2 = member("Ahmed", "Ali", "mahmoud", "Male")
# member_3 = member("mona", "Ahmed", "Abdel3al", "Female")
# member_4 = member("Hell", "Ahmed", "Abdel3al", "Female")

# print(member.users_num)

# print(member_4.delete_user())
# print(member.users_num)


# print("#" * 40)

# member.show_user_count()


# print("#" * 40)

# # print(member_1.full_name())

# # print(member.full_name(member_1))


# member.say_hello()


# ================ درس 109# - ال OOP الجزء 7 - ال Magic Methods

# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------


# import profile


# class skill:

#     def __init__(self):

#         self.skills = ["Html", "Css", "Js"]

#     def __str__(self):

#         return f"This Is my skills => {self.skills}"

#     def __len__(self):

#         return len(self.skills)


# profile = skill()

# print(profile)
# print(len(profile))


# profile.skills.append("PHP")
# profile.skills.append("MySQL")
# print(profile)
# print(len(profile))

# print(profile.__class__)


# my_string = "Osama"

# print(type(my_string))
# print(my_string.__class__)
# print(dir(str))
# print(str.upper(my_string))


# ===================درس 110# - ال OOP الجزء 8 - نظام الوراثة Inheritance


# ============================================================================
# ================================Father======================================
# class Food:  # Base class

#     def __init__(self, name, price):

#         self.name = name
#         self.price = price

#         print(f"{self.name} Food is created from main class")

#     def eat(self):

#         print("Eat method from base class")

# #============================================================================
# #==================================son=======================================


# class Apple(Food):  # Derived Class

#     def __init__(self, name, price, amount):

#         # Food.__init__(self, name) #create instance from Base class

#         super().__init__(name, price)

#         self.amount = amount

#         # self.name = name
#         # self.price = price + 20

#         print(f"{self.name} is created from Derived class and price {self.price}  And amount is {self.amount} ")

#     def get_from_tree(self):
#         print("Get From Tree From Derived Class")
# #======================================================================================================================


# # food_1 = Food()


# food_2 = Apple("Pizza", 150, 500)


# # food_2.eat()
# food_2.get_from_tree()


# ============درس 111# - ال OOP الجزء 9 - نظام الوراثة Inheritance المتعدد و Method Override
# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------


# class BaseOne:

#     def __init__(self):

#         print("Base one")

#     def fun_1(self):
#         print("One")


# class BaseTwo:

#     def __init__(self):

#         print("Base Two")

#     def fun_2(self):
#         print("TWO")


# class Derived(BaseOne, BaseTwo):

#     pass


# my_var = Derived()

# # print(Derived.mro())

# print(my_var.fun_1())
# print(my_var.fun_2())

# my_var.fun_1()
# my_var.fun_2()


# class Base:

#     pass

# class DerivedOne(Base):

#     pass

# class DerivedTwo(DerivedOne):

#     pass


# ===========درس 112# - ال OOP الجزء 10 - نظام تعدد الأوجه Polymorphism
# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

# n1 = 10
# n2 = 20

# print(n1 + n2)

# s1 = "Hello"
# s2 = "Python"

# print(s1 + " " + s2)


# print(len([1, 2, 3, 4, 5, 6]))
# print(len("Osama Elzero"))
# print(len({"Key_One": 1, "Key_Two": 2}))


# class A:

#     def do_some(self):

#         print("FOrm class A")

#         raise NotImplementedError("Derived Class must implement this method")


# class B(A):

#     def do_some(self):

#         print("FOrm class B")


# class C(A):

#     def do_some(self):

#         print("FOrm class C")


# my_instance = C()

# my_instance.do_some()


# ======درس 113# - ال OOP الجزء 11 - نظام التغليف Encapsulation
# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------


# class Member:

#     def __init__(self, name):

#         self.name = name #public


# one = Member("Ahmed")

# print(one.name)
# one.name = "Sayed"
# print(one.name)


# class Member:

#     def __init__(self, name):

#         self._name = name  # protected


# one = Member("Ahmed")

# print(one._name)
# one._name = "Sayed"
# print(one._name)


# class Member:

#     def __init__(self, name):

#         self.__name = name  # private

#     def say_hello(self):

#         return f"Hello {self.__name}"


# one = Member("Ahmed")

# # print(one.__name)
# # one._name = "Sayed"
# # print(one.say_hello())

# print(one._Member__name)


# درس 114# - ال OOP الجزء 12 - ال Getters + Setters
# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

# class Member:

#     def __init__(self, name):

#         self.__name = name  # Private

#     def say_hello(self):

#         return f"Hello {self.__name}"

#     def get_name(self):

#         return self.__name

#     def set_name(self, new_name):

#         self.__name = new_name


# one = Member("Ahmed")

# print(one.get_name())
# one.set_name("abbas")
# print(one.get_name())


# # درس 115# - ال OOP الجزء 13 - ال Property Decorator
# # --------------------------------------------------------
# # -- Object Oriented Programming => @Property Decorator --
# # --------------------------------------------------------

# class Member:

#     def __init__(self, name, age):

#         self.name = name

#         self.age = age

#     def say_hello(self):

#         return f"Hello {self.name}"

#     @property
#     def age_in_days(self):

#         return self.age * 365


# one = Member("Ahmed", 40)

# print(one.name)
# print(one.age)
# print(one.say_hello())
# print(one.age_in_days())

# print(one.age_in_days)


# درس 116# - ال OOP الجزء 14 - التجريد Abstract Base Class
# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import abstractmethod, ABCMeta
from operator import methodcaller


class programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):

        pass

    def has_name(self):
        pass


class python(programming):

    def has_oop(self):

        return "Yes"


class pascal(programming):

    def has_oop(self):

        return "No"


one = pascal()

print(one.has_oop())
