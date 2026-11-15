import random
import player

DAYS_IN_MONTH = 30
LOW_MONEY_THRESHOLD = 3000
MINIJOB_SALARY = 556

# job language -> interviews per month
INTERVIEWS = {
    "English": 2,
    "German": 3,
}

ENGLISH_JOB_CHANCE = 0.25
GERMAN_BASE_CHANCE = 0.1  # at A1
GERMAN_CHANCE_PER_LEVEL = 0.1

def _interview_chance(p, job_language):
    if job_language == "English":
        return ENGLISH_JOB_CHANCE
    return GERMAN_BASE_CHANCE + GERMAN_CHANCE_PER_LEVEL * p["german_level"]

def _choose_job_language():
    print("\nYour money is running low. You need to find a minijob!")
    print(f"A minijob pays {MINIJOB_SALARY} EUR per month.")
    print("Which language do you want to work in?")
    print(f"  1. English ({INTERVIEWS['English']} interviews per month)")
    print(f"  2. German  ({INTERVIEWS['German']} interviews per month)")

    choice = input("Your choice (1-2): ").strip()

    if choice == "1":
        return "English"
    elif choice == "2":
        return "German"
    else:
        print("Invalid input. Looking for an English job by default.")
        return "English"

def start_job_if_ready(p):
    if p["next_job"] is None:
        return

    p["job"] = p["next_job"]
    p["next_job"] = None
    print(f"Your minijob starts this month. You now work in {p['job']}!")

def pay_salary(p):
    if p["job"] is None:
        return

    p["money"] += MINIJOB_SALARY
    print(f"Minijob salary: +{MINIJOB_SALARY} EUR")

def find_job_event(p):
    if p["job"] is not None or p["next_job"] is not None:
        return
    if p["money"] > LOW_MONEY_THRESHOLD:
        return

    job_language = _choose_job_language()
    chance = _interview_chance(p, job_language)
    days = sorted(random.sample(range(1, DAYS_IN_MONTH + 1), INTERVIEWS[job_language]))

    for day in days:
        print(f"Day {day}: Job interview ({job_language})...")
        if random.random() < chance:
            p["next_job"] = job_language
            print("You got a minijob! You start working next month.")
            return
        print("  They chose someone else. Keep trying!")

    print("You couldn't find a job this month.")
