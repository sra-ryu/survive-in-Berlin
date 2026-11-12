import random
import player
import event_lost_key

TOTAL_MONTHS = 12
MONTHLY_LIVING_COST = 992  # based on Sperrkonto minimum

ALL_EVENTS = [
    event_lost_key.lost_key_event,
]

def schedule_events():
    months = random.sample(range(1, TOTAL_MONTHS + 1), len(ALL_EVENTS))
    return {month: event for month, event in zip(months, ALL_EVENTS)}

def introduce_player(p):
    print(f"\nHi, I'm {p['name']}. Now I have {p['money']} EUR for my first year in Berlin.")
    print(f"My German level is {player.GERMAN_LEVEL[p['german_level']]} and I'm a {p['status']}.")

def show_status(p, month):
    print(f"\n=== Month {month} / {TOTAL_MONTHS} ===")
    print(f"Money    : {p['money']} EUR")
    print(f"German   : {player.GERMAN_LEVEL[p['german_level']]}")
    print(f"Status   : {p['status']}")
    print(f"Residence: {player.RESIDENCE[p['residence']]}")

def game_loop(p):
    schedule = schedule_events()

    for month in range(1, TOTAL_MONTHS + 1):
        show_status(p, month)

        if month in schedule:
            schedule[month](p)

        p["money"] -= MONTHLY_LIVING_COST
        print(f"Living costs: -{MONTHLY_LIVING_COST} EUR")

        if p["money"] <= 0:
            print("\nYou ran out of money. Game over.")
            return

    print(f"\nYou survived a year in Berlin! Money remaining: {p['money']} EUR.")

def main():
    p = player.create_player()
    introduce_player(p)
    game_loop(p)

if __name__ == "__main__":
    main()
