
"""This is my code to say hello to any one """


myFriends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_peoples) -> list:
    '''This Function Only Say Hello To Someone'''
    for someone in some_peoples:
        print(f"Hello {someone}")


say_hello(myFriends)
