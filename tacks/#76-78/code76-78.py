from my_mod import say_welcome as nwe_welcome
import my_mod
import random
from random import randint, random, randrange

print(f"Random Number Between 10 And 50 => {randint(10,50)}")

print(f"Random Even Number Between 2 And 10 => {randrange( 2 , 11  , 2)}")


print(f"Random odd Number Between 1 And 9 => {randrange( 1 , 10  , 2)}")

print(dir(random))


# ======================task 2 =============================================


my_mod.say_hello("Abdelrahamn")

my_mod.say_welcome("Abdelrahamn")

# =====================task 3 ===============================


# say_welcome("Ahmed")

# ==========================task 4 =======================

nwe_welcome("Ahmed")


