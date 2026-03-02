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

def get_unique_players(parsed_data):

    players_list = [item[0] for item in parsed_data]
    unique_players_list = list(set(players_list))
    return unique_players_list

def get_wins_only(parsed_data):

    wins_only_list = [item for item in parsed_data if item[3] == "win"]
    return wins_only_list

def get_last_three(parsed_data):

    last_three = parsed_data[-3:]
    return last_three

def get_every_other(parsed_data):

    every_other = parsed_data[::2]
    return every_other

def get_all_scores(parsed_data):

    score_list = [item[2] for item in parsed_data]
    return score_list


