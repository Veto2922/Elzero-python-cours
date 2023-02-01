# ----------------------------------
# -- Regular Expressions => Intro --
# ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# -----------------------------------------------------------


# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# -------------


# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# -----------------------------------------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]
# -------------


# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$


# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
# \	  Escape Special Characters
# ()  Separate Groups
# -----------------------------

# (\d-|\d\)|\d>) (\w+)
# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$


# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------


import re
import re  # for regular Expression

# my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

# print(my_search)
# print(my_search.span())

# print(my_search.string)
# print(my_search.group())


# is_email = re.search(
#     r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "os@osama.com")

# print(is_email)

# if is_email:

#     print("This is A Valid Email")

#     print(is_email.span())
#     print(is_email.string)
#     print(is_email.group())

# else:

#     print("This is Not A Valid Email")


# 2)findall method

# email_input = input("please write your email")

# seaech = re.findall("[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info", email_input)


# empty_list = []

# if seaech != []:
#     empty_list.append(seaech)

#     print("Email Added")

# else:
#     print("invalid Email")

# for email in empty_list:
#     print(email)


# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------


string_one = "I love Python"

search_1 = re.split("\s", string_one)

print(search_1)


print("#" * 40)

string_2 = "How-to_write_a_very-good-Article"

search_2 = re.split(r"-|_", string_2)

print(search_2)


# get word from Url

for counter,  word in enumerate(search_2, 1):

    if len(word) == 1:
        continue

    print(f"Word number: {counter} => {word.lower()}")


print("#" * 40)


print(re.sub(r"f", "o", "I lfve pythf in world"))


# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------


my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)


print(search.group())
# print(search.groups())


# for group in search.groups():

#   print(group)


print(f"Protocal: {search.group(1)}")
print(f"sub domain: {search.group(2)}")

print(f"Domain name: {search.group(3)}")

print(f"Top level bomain: {search.group(4)}")

print(f"port: {search.group(5)}")
print(f"query string: {search.group(6)}")
