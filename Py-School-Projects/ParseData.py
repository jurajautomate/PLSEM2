# 1. parse_tournament_data(raw_data)
#    - Takes the raw string above, returns a list of tuples
#    - Each tuple: (player, game, score, result) — all lowercase, score as int
#    - Skip empty lines and lines with invalid/non-numeric scores
#    - Concepts to use: split, strip, lower, try/except, tuples

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

def parse_tournament_data(raw_data):
    split_data = raw_data.split("\n")
    lists = []
    for line in split_data:
        if not
        new_list = line.strip().lower().split(" | ")
        lists.append(new_list)

    tuples = []
    for single in lists:
        new_tuples = tuple(single)
        tuples.append(new_tuples)
    print(tuples)
    return tuples

parse_tournament_data(raw_tournament_data)
