
from sre_compile import isstring


class Game:

    def __init__(self, name, dev, year, price):

        self.name = name
        self.developer = dev
        self.year = year
        self.price_in_pounds = float(price) * 19

    # def __int__(self):

    #     return int(self.price_in_pounds)


game_one = Game("Ys", "Falcom", 2010, 50)


# print(dir(game_one))

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds}", end="")

print("#" * 50)

# ==============================task 2 ==========================================


class User:

    def __init__(self, first_name, secand_name, age, gender):

        self.fname = first_name
        self.sname = secand_name
        self.age = 40 - age
        self.gender = gender

    def full_details(self):

        if self.gender == "Male":

            return f"Hello Mr {self.fname} {self.sname[0]}. [{self.age}] Years To Reach 40"

        elif self.gender == "Female":

            return f"Hello Mrs {self.fname} {self.sname[0]}. [{self.age}] Years To Reach 40"

        else:

            return f"{self.fname}"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

print("#" * 50)
# ================================task 3 =======================================================


class Message:

    @classmethod
    def print_message(cls):
        return ("Hello from class method")

    def __init__(self):

        pass


print(Message.print_message())


print("#" * 50)
# =================================task 4 =======================================================


class Games:

    def __init__(self, game):

        self.games = game

    def show_games(self):

        if isinstance(self.games, str):

            print(f"I Have One Game Called {self.games}")

        elif isinstance(self.games, list):
            print(f"I Have Many Games: ")

            for i in self.games:
                print(f"-- {i}")

        elif isinstance(self.games, int):

            print(f"I Have {self.games} Game.")

        else:
            print("The input in not correct")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)


my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()

print("#" * 50)
# =========================================task 5===============================


class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):

    def __init__(self, n, p):

        super().__init__(n, p)


class Moderators(Admins):

    def __init__(self, n, p):

        super().__init__(n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")


print(member_one.show_info())
print(member_two.show_info())


print("#" * 50)
# =========================================task 6===============================


class A:

    def __init__(self, one):

        self.one = one


class B:

    def __init__(self, two):

        self.two = two


class C:

    def __init__(self, three):

        self.three = three


class Text(A, B, C):

    def __init__(self, one, two, three):

        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

        # super().__init__(one)
        # # super().__init__(two)
        # # super().__init__(three)

    def show_name(self):

        return f"The name is {self.one}{self.two}{self.three}"


the_name = Text("El", "ze", "ro")

print(the_name.show_name())
