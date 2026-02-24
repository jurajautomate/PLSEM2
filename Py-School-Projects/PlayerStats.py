from ParseData import parse_tournament_data

raw_tournament_data = """
  PlayerOne | Zelda | 3200 | Win
  playerTWO | Mario Kart | 2800 | Loss
  PLAYERthree | Zelda | 4100 | Win
  PlayerFour | Smash Bros | 1900 | Loss
  PlayerFive | Mario Kart | 3600 | Win
  PlayerOne | Smash Bros | 2100 | Win
  PlayerThree | Mario Kart | 3900 | Win
  PlayerTwo | Zelda | 3000 | Loss
  PlayerFour | Zelda | 2200 | Loss
  PlayerFive | Smash Bros | 4500 | Win
  PlayerOne | Mario Kart | BAD_DATA | Win
  PlayerTwo | Smash Bros | 2600 | Win
  PlayerThree | Smash Bros | 3700 | Win
  PlayerFour | Mario Kart | 1800 | Loss
  PlayerFive | Zelda | 4000 | Win
"""

data = parse_tournament_data(raw_tournament_data)

player_stats = {}

for id, *rest in data:
    if not id in player_stats:
        player_stats[id] = {"games_played": 1, "wins": 0, "losses": 0, "total_score": rest[1], "scores": rest[1]}
        if rest[2] == "win":
            player_stats[id]["wins"] = 1
        else:
            player_stats[id]["losses"] = 1
    else:
        