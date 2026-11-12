import create_palyer

def introduce_player(player):
    print(f"Hi, I'm {player['name']}. Now I have {player['money']} EURO for my first year in Berlin.")
    print(f"My German level is {create_palyer.GERMAN_LEVEL[player['german_level']]} and I'm {player['status']}.")

player = create_palyer.create_player()
introduce_player(player)