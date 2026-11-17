import random

ITEMS_PER_ROUND = 5

# bin number -> color
BINS = {
    "1": "blue",
    "2": "black",
    "3": "brown",
    "4": "yellow",
}

# item -> correct bin number
TRASH = {
    "old newspaper": "1",
    "empty cardboard box": "1",
    "used tissue": "2",
    "cigarette butt": "2",
    "supermarket receipt": "2",
    "full vacuum cleaner bag": "2",
    "banana peel": "3",
    "egg shells": "3",
    "coffee grounds": "3",
    "empty yogurt cup": "4",
    "plastic wrap": "4",
    "empty milk carton": "4",
    "aluminum can": "4",
}

GRANDMA_LINES = [
    "Nein, nein, nein!",
    "Ach, du meine Güte!",
    "Junge Leute heutzutage...",
    "Das gibt's doch nicht!",
]

def _show_bins():
    for number, color in BINS.items():
        print(f"  {number}. {color.capitalize()} bin")

def _sort_item(item):
    print(f"\nYou pick up: {item}")
    _show_bins()
    choice = input("Which bin? (1-4): ").strip()
    correct = TRASH[item]

    if choice == correct:
        print("Plop! Into the right bin.")
        return True

    color = BINS[correct]
    print("An old German lady suddenly appears from behind the bins...")
    print(f'Grandma: "{random.choice(GRANDMA_LINES)} The {item} goes in the {color.upper()} bin!"')
    return False

def trash_sorting_event(p):
    print("\nYour trash bag is full. Time to take it down to the courtyard.")
    print("Remember: Germans take recycling VERY seriously.")

    items = random.sample(list(TRASH), ITEMS_PER_ROUND)
    score = sum(_sort_item(item) for item in items)

    print(f"\nYou sorted {score} / {ITEMS_PER_ROUND} items correctly.")
    print(result_message(score))

def result_message(score):
    if score == ITEMS_PER_ROUND:
        return 'Grandma nods from her window: "Sehr gut. You are almost German now."'
    if score >= ITEMS_PER_ROUND - 2:
        return "Not bad. Grandma is still watching you, though."
    return "Grandma sighs and starts re-sorting the bins herself."
