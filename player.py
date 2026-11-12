import random

MIN_START_MONEY = 11904 # about one year of blocked account
MAX_START_MONEY = 20000

GERMAN_LEVEL = ["A1", "A2", "B1", "B2", "C1", "C2"]

RESIDENCE = ["WG", "studio", "dormitory", "temporary residence"]

# A character has name, money, status, german_level and residence
def create_player():
    name = input("Enter your name: ")
    money = random.randint(MIN_START_MONEY, MAX_START_MONEY)
    status = "language learner" # default initial status
    german_level = GERMAN_LEVEL.index("A1") # default initial status
    residence = RESIDENCE.index("temporary residence")

    return {"name": name, "money": money, "status": status, "german_level": german_level, "residence": residence}