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
    split_list = []
    for line in split_data:
        if not line.strip():
            continue
        new_list = line.strip().lower().split(" | ")
        try:
            score = int(new_list[2])
        except ValueError:
            continue
        new_list[2] = score
        split_list.append(new_list)

    tuples = []
    for single in split_list:
        new_tuples = tuple(single)
        tuples.append(new_tuples)
    return tuples

parse_tournament_data(raw_tournament_data)

# expected output:
# [('playerone', 'zelda', 3200, 'win'), ('playertwo', 'mario kart', 2800, 'loss'), ('playerthree', 'zelda', 4100, 'win'), ('playerfour', 'smash bros', 1900, 'loss'), ('playerfive', 'mario kart', 3600, 'win'), ('playerone', 'smash bros', 2100, 'win'), ('playerthree', 'mario kart', 3900, 'win'), ('playertwo', 'zelda', 3000, 'loss'), ('playerfour', 'zelda', 2200, 'loss'), ('playerfive', 'smash bros', 4500, 'win'), ('playertwo', 'smash bros', 2600, 'win'), ('playerthree', 'smash bros', 3700, 'win'), ('playerfour', 'mario kart', 1800, 'loss'), ('playerfive', 'zelda', 4000, 'win')]