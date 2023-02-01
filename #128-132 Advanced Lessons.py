# -------------------------------------------------
# -- Advanced_Lessons => __name__ And "__main__" --
# -------------------------------------------------
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
# - From Import => Import The Code From File To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
# ---------------------------------------------------

import string
import unittest
import logging
import random
import timeit
print(__name__)


# درس 129# - دروس متقدمة - معرفة وقت تنفيذ ال Code بواسطة Timeit
# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------

# print(dir(timeit))


# print(timeit.timeit("'Elzero' * 1000"))

# name = "Elzero"

# # print(name * 1000)

# print(timeit.timeit("name = 'Elzero'; name * 1000"))

# # print(random.randint(0, 50))

# print(random.randint(0, 50))

# print(timeit.timeit(stmt="random.randint(0,50)", setup="import random"))


# print(timeit.repeat(stmt="random.randint(0,50)", setup="import random", repeat=4))


# درس 130# - دروس متقدمة - إضافة ال Logging لل Code ألخاص بك
# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name and Extension
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# ------------------------
# getLogger => Return a Logger With the Specified Name


# logging.basicConfig(filename="my_app.log",
#                     filemode="a",
#                     format="(%(asctime)s) ==> %(name)s | %(levelname)s | '%(message)s'", datefmt="%d - %B - %Y , %H:%M:%H")

# my_logger = logging.getLogger("Elzero")

# my_logger.warning("this is error massage")


# درس 131# - دروس متقدمة - إختبار الواحدات بواسطة Unittest
# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------


# assert 3 * 8 == 24, "should be 24"

# def test_case_one():

#     assert 5 * 10 == 50, "shoud be 50"


# def test_case_two():

#     assert 4 * 10 == 40, "shoud be 40"


# if __name__ == "__main__":

#     test_case_one()
#     test_case_two()

#     print("All tests passed")

# ================================================

# class MyTestCase(unittest.TestCase):

#     def test_one(self):
#         self.assertTrue(100 > 99, "shoud be True")

#     def test_two(self):

#         self.assertEqual(40+60, 100, "should be 100")

#     def test_three(self):

#         self.assertGreater(100, 80, "shoud be true")


# if __name__ == "__main__":

#     unittest.main()


# unittest.TestCase.assertTrue


# --------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# --------------------------------------------------------

#import string
#import random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def make_serial(count):

    all_chars = string.ascii_letters + string.digits
    # print(all_chars)

    chars_count = len(all_chars)
    # print(chars_count)

    serial_list = []

    while count > 0:

        random_number = random.randint(0, chars_count - 1)

        random_char = all_chars[random_number]

        serial_list.append(random_char)

        count -= 1

    print("".join(serial_list))


make_serial(100)
