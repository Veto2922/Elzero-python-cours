
# def get_score(**sub):

#     for key, valuo in sub.items():

#         print(f"{key} => {valuo}")


# get_score(Math=90, Science=80, Language=70, combuter=85)
# print("=" * 40)
# get_score(Logic=70, Problems=60)


# ===================task 2 =====================================

# def get_people_scores(name="", **sub):

#     if len(name) == 0:
#         pass
#     else:
#         print(f"Hello {name} You Have No Scores To Show" if len(
#             sub) == 0 else f"Hello {name} This is your score table:  ")

#     for key, valuo in sub.items():

#         print(f"{key} => {valuo}")


# get_people_scores("Ahmed")

# ==============================task 3====================================

my_skills = {

    "Math": 90,
    "Science": 80,
    "language": 70
}


def get_the_scores(name="", **skills):

    if len(name) == 0:
        pass
    else:
        print(f"Hello {name} You Have No Scores To Show" if len(
            skills) == 0 else f"Hello {name} This is your score table:  ")

    for key, valuo in skills.items():

        print(f"{key} => {valuo}")


get_the_scores(**my_skills)
 