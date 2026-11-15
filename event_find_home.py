import random
import player

DAYS_IN_MONTH = 30

# housing type -> (viewings per month, success chance per viewing)
HOME_OPTIONS = {
    "WG": (4, 0.25),
    "studio": (2, 0.10),
}

def _choose_home_type():
    print("\nYou are still living in a temporary residence.")
    print(f"Temporary residence costs {player.RENT['temporary residence']} EUR per month.")
    print("What kind of home do you look for this month?")
    print(f"  1. WG     (rent {player.RENT['WG']} EUR per month)")
    print(f"  2. Studio (rent {player.RENT['studio']} EUR per month)")

    choice = input("Your choice (1-2): ").strip()

    if choice == "1":
        return "WG"
    elif choice == "2":
        return "studio"
    else:
        print("Invalid input. Looking for a WG by default.")
        return "WG"

def move_in_if_ready(p):
    if p["next_residence"] is None:
        return

    p["residence"] = p["next_residence"]
    p["next_residence"] = None
    print(f"Your new contract starts this month. You moved into your {player.RESIDENCE[p['residence']]}!")

def find_home_event(p):
    if player.RESIDENCE[p["residence"]] != "temporary residence":
        return
    if p["next_residence"] is not None:
        return

    home_type = _choose_home_type()
    viewings, chance = HOME_OPTIONS[home_type]
    days = sorted(random.sample(range(1, DAYS_IN_MONTH + 1), viewings))

    for day in days:
        print(f"Day {day}: Besichtigung for a {home_type}...")
        if random.random() < chance:
            p["next_residence"] = player.RESIDENCE.index(home_type)
            print(f"You got the {home_type}! Your contract starts next month.")
            return
        print("  Not lucky this time. Let's hope for the next chance!")

    print("You couldn't find a home this month.")
