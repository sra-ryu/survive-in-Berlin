import random

MIN_START_MONEY = 11904  # about one year of blocked account
MAX_START_MONEY = 20000

GERMAN_LEVEL = ["A1", "A2", "B1", "B2", "C1", "C2"]
RESIDENCE = ["WG", "studio", "dormitory", "temporary residence"]
RENT = {
    "WG": 300,
    "studio": 400,
    "temporary residence": 500,
}

def create_player():
    name = input("Enter your name: ")
    money = random.randint(MIN_START_MONEY, MAX_START_MONEY)
    status = "language learner"
    german_level = GERMAN_LEVEL.index("A1")
    residence = RESIDENCE.index("temporary residence")

    return {
        "name": name,
        "money": money,
        "status": status,
        "german_level": german_level,
        "residence": residence,
        "next_residence": None,
        "job": None,
        "next_job": None,
        "german_next_attempt": 3,
        "german_next_prob": 1.0,
    }

def check_german_level_up(p, month):
    if p["german_next_attempt"] != month:
        return

    current_idx = p["german_level"]
    current = GERMAN_LEVEL[current_idx]

    if current_idx >= GERMAN_LEVEL.index("C1"):
        return

    next_idx = current_idx + 1
    next_level = GERMAN_LEVEL[next_idx]
    prob = p["german_next_prob"]

    if random.random() < prob:
        p["german_level"] = next_idx
        print(f"Your German level has risen from {current} to {next_level}!")
        _schedule_next_attempt(p, month, next_idx)
    else:
        print(f"You failed the German test. Your level remains {current}.")
        _schedule_retry(p, month, current_idx, prob)

def _schedule_next_attempt(p, month, level_idx):
    level = GERMAN_LEVEL[level_idx]
    if level in ("C1", "C2"):
        p["german_next_attempt"] = None
    elif level == "B2":
        p["german_next_attempt"] = month + 3
        p["german_next_prob"] = 0.25
    elif level == "B1":
        p["german_next_attempt"] = month + 3
        p["german_next_prob"] = 0.5
    else:
        p["german_next_attempt"] = month + 3
        p["german_next_prob"] = 1.0

def _schedule_retry(p, month, level_idx, failed_prob):
    level = GERMAN_LEVEL[level_idx]
    if level == "B1":
        p["german_next_attempt"] = month + 1
        p["german_next_prob"] = 1.0
    elif level == "B2":
        if failed_prob == 0.25:
            p["german_next_attempt"] = month + 1
            p["german_next_prob"] = 0.5
        else:  # failed_prob == 0.5, second fail
            p["german_next_attempt"] = month + 1
            p["german_next_prob"] = 1.0
