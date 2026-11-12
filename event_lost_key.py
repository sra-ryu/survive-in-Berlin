import player

def lost_key_event(p):
    print("You left your key inside your room!")
    print("You have to call Schlüsseldienst!")

    if p["german_level"] >= player.GERMAN_LEVEL.index("B2"):
        p["money"] -= 80
    else:
        p["money"] -= 100

    print(f"Money left: {p['money']} EUR.")