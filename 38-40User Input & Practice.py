
# ----------------
# -- User Input --
# ----------------


# # fName = input("what\'s Is Your First Name?")
# # mName = input("What\'s Is Your Middle name?")
# # lName = input("What\'s Is Your Last Name?")

# # fName = fName.strip().capitalize()

# # lName = lName.strip().capitalize()

# print(f"Hello {fName} {mName:.1s} {lName} Heppy to See You")

# -----------------------------------------------------------------
# ---------------------------
# -- Practical Slice Email --
# ---------------------------

# theName = input("What's your Name?").strip().capitalize()
# theEmail = input("What's Your Email?").strip()

# userName = theEmail[0:theEmail.index("@")].strip()
# webSite = theEmail[theEmail.index("@") + 1:]

# print(f"Hello {theName} Your Email is {theEmail}")
# print(f"Your Username IS {userName}  \n  And Your Website Is {webSite} ")


# email = "xobedo@gmail.com"
# print(email[0:email.index("@")])

# ----------------------------------------------------------
# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

age = int(input("what's Your Age ?").strip())

months = age * 12
weeks = months * 4
day = age * 365
hour = day * 24
minutes = hour * 60
seconds = minutes * 60

print('Your Lived For:')
print(f"{months} Months")
print(f"{weeks:,} weeks")
print(f"{day:,} Day")
print(f"{hour:,} Hour")
print(f"{minutes:,} Minutes")
print(f"{seconds:,} seconds")
