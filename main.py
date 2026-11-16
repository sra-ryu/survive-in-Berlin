import random
import player
import utils
import event_lost_key
import event_find_home
import event_find_job
import event_trash_sorting

TOTAL_MONTHS = 12
MONTHLY_LIVING_COST = 992  # based on Sperrkonto minimum

# (event, months it can happen in)
ALL_EVENTS = [
    (event_lost_key.lost_key_event, range(1, TOTAL_MONTHS + 1)),
    (event_trash_sorting.trash_sorting_event, range(1, 4)),
]

def schedule_events():
    schedule = {}
    # place events with fewer possible months first so they always get a slot
    for event, months in sorted(ALL_EVENTS, key=lambda e: len(e[1])):
        free_months = [m for m in months if m not in schedule]
        schedule[random.choice(free_months)] = event
    return schedule

def introduce_player(p):
    print(f"\nHi, I'm {p['name']}. Now I have {p['money']} EUR for my first year in Berlin.")
    print(f"My German level is {player.GERMAN_LEVEL[p['german_level']]} and I'm a {p['status']}.")

def show_status(p):
    print(f"Money    : {p['money']} EUR")
    print(f"German   : {player.GERMAN_LEVEL[p['german_level']]}")
    print(f"Status   : {p['status']}")
    print(f"Residence: {player.RESIDENCE[p['residence']]}")

def game_loop(p):
    schedule = schedule_events()

    for month in range(1, TOTAL_MONTHS + 1):
        print(f"\n=== Month {month} / {TOTAL_MONTHS} ===")
        event_find_home.move_in_if_ready(p)
        event_find_job.start_job_if_ready(p)
        show_status(p)
        player.check_german_level_up(p, month)

        event_find_home.find_home_event(p)
        event_find_job.find_job_event(p)

        if month in schedule:
            schedule[month](p)

        p["money"] -= MONTHLY_LIVING_COST
        print(f"Living costs: -{MONTHLY_LIVING_COST} EUR")

        rent = player.RENT[player.RESIDENCE[p["residence"]]]
        p["money"] -= rent
        print(f"Rent: -{rent} EUR")

        event_find_job.pay_salary(p)

        if p["money"] <= 0:
            print("\nYou ran out of money. Game over.")
            return

        utils.pause()

    print(f"\nYou survived a year in Berlin! Money remaining: {p['money']} EUR.")

def main():
    p = player.create_player()
    introduce_player(p)
    game_loop(p)

if __name__ == "__main__":
    main()
