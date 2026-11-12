import character_sheet

print("You plan to go to the supermarket.")
print("Oh, you left your key in the room! You have to call Schlüsseldienst!")

def lost_key_event(player):
    print("You left your key inside room!")
    if player["german_level"] >= german_level.index("B2"):
        player["money"] -= 80
    else:
        player["money"] -= 100
        
    print(f"Today I lost my key. Left money is {player["money"]}.")