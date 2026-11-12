import random
import player

def _call_schluesseldienst(p):
    cost = 80 if p["german_level"] >= player.GERMAN_LEVEL.index("B2") else 100
    p["money"] -= cost
    print(f"Schlüsseldienst opened the door. Cost: -{cost} EUR. Money left: {p['money']} EUR.")

def lost_key_event(p):
    print("\nOh no! You left your key inside your room.")
    print("What do you do?")
    print("  1. Try to open the door yourself")
    print("  2. Ask a neighbor for help")
    print("  3. Call Schlüsseldienst")

    choice = input("Your choice (1-3): ").strip()

    if choice == "1":
        if random.random() < 0.2:
            print("You managed to open the door yourself. Lucky!")
        else:
            print("You couldn't open the door.")
            _call_schluesseldienst(p)

    elif choice == "2":
        if random.random() < 0.3:
            print("Your neighbor helped you get in. Thanks!")
        else:
            print("Your neighbor couldn't help.")
            _call_schluesseldienst(p)

    elif choice == "3":
        _call_schluesseldienst(p)

    else:
        print("Invalid input. Calling Schlüsseldienst by default.")
        _call_schluesseldienst(p)
