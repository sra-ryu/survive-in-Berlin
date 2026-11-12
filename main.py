import random
import player
import event_lost_key

TOTAL_MONTHS = 12

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
    for month in range(1, TOTAL_MONTHS + 1):
        show_status(p, month)

        if random.random() < 0.3:
            event_lost_key.lost_key_event(p)

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
