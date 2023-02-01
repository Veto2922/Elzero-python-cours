
# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

from time import time
myString = "Osama"

myList = [1, 2, 3, 4, 5]

# for letter in myString:

#     print(letter, end=" ")

# for number in myList:

#     print(number, end=" ")


# myIterator = iter(myString)

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

# for letter in "Elzero":

#     print(letter, end=" ")


# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 85


myGen = myGenerator()

print(next(myGen))

print("Hello from python")

print(next(myGen))

print("Hello from python")
print(next(myGen))

print("Hello from python")
print(next(myGen))

for mynum in myGen:
    print(mynum)


# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

def myDecorator(func):  # decorator

    def nestedFunc():

        print("Before")  # Message From Decorator

        func()  # Execute Function

        print("After")  # Message From Decorator

    return nestedFunc  # Return All Data


@myDecorator
def sayHello():

    print("hello from say hello function ")


@myDecorator
def sayHowAreYou():

    print("Hello From Say How Are You Function")

# afterDecoration = myDecorator(sayHello)

# afterDecoration()


sayHello()

print("#" * 50)

sayHowAreYou()


# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorator(func):  # Decorator

    def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

        if num1 < 0 or num2 < 0:

            print("Beware One Of The Numbers Is Less Than Zero")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


def myDecoratorTwo(func):  # Decorator

    def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

        print("Coming From Decorator Two")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


@myDecorator
@myDecoratorTwo
def calculate(n1, n2):

    print(n1 + n2)


calculate(5, 90)


# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------


def myDecorator(func):  # Decorator

    def nestedFunc(*numbers):  # Any Name Its Just For Decoration

        for number in numbers:

            if number < 0:

                print("Beware One Of The Numbers Is Less Than Zero")

        func(*numbers)  # Execute Function

    return nestedFunc  # Return All Data


@myDecorator
def calculate(n1, n2, n3, n4):

    print(n1 + n2 + n3 + n4)


calculate(-5, 90, 50, 150)


def speedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(start)
        print(end)

        print(f"Function Running Time Is: {end - start}")

    return wrapper


@speedTest
def bigLoop():

    for number in range(1, 20000):

        print(number)


bigLoop()
