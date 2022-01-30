import requests
from player import Player
import player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
            player_dict['nationality']
        )

        players.append(player)

    print("Oliot:")
    
    finplayers = sorted(list(filter(lambda x: (x.nationality == "FIN"), players)), key=lambda x: x.points(),reverse=True)

    
    for player in finplayers:
        print(player)

if __name__ == "__main__":
    main()
