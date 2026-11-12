import random
import player
import event_lost_key

TOTAL_MONTHS = 12
MONTHLY_LIVING_COST = 992  # based on Sperrkonto minimum

def introduce_player(p):
    print(f"\nHi, I'm {p['name']}. Now I have {p['money']} EUR for my first year in Berlin.")
    print(f"My German level is {player.GERMAN_LEVEL[p['german_level']]} and I'm a {p['status']}.")

def show_status(p, month):
    print(f"\n=== Month {month} / {TOTAL_MONTHS} ===")
    print(f"Money    : {p['money']} EUR")
    print(f"German   : {player.GERMAN_LEVEL[p['german_level']]}")
    print(f"Status   : {p['status']}")
    print(f"Residence: {player.RESIDENCE[p['residence']]}")

ALL_EVENTS = [
    event_lost_key.lost_key_event,
]

def schedule_events():
    events = ALL_EVENTS.copy()
    random.shuffle(events)

    schedule = {month: [] for month in range(1, TOTAL_MONTHS + 1)}
    for i, event in enumerate(events):
        schedule[(i % TOTAL_MONTHS) + 1].append(event)

    return schedule

def game_loop(p):
    schedule = schedule_events()

    for month in range(1, TOTAL_MONTHS + 1):
        show_status(p, month)

        for event in schedule[month]:
            event(p)

        p["money"] -= MONTHLY_LIVING_COST
        print(f"Living cost this month: -{MONTHLY_LIVING_COST} EUR")

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
