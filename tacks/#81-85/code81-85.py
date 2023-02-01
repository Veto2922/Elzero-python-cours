
# def reverse_string(my_string):

#     yield my_string[::-1]


# name = ["Ahmed", "mohmaed"]

# for n in reverse_string(name):
#     print(n)


# =======================task 2 ================================

def myDec(colefun):

    def netfun():

        print("Sugar Added From Decorators")

        colefun()

        print("#" * 20)
    return netfun()


@myDec
def make_tea():
    print("Tea Created")


@myDec
def make_coffe():
    print("Coffe Created")


make_tea
make_coffe
