"""
=============================================================================
🏆 PYTHON GAPS PROJECT — "Game Tournament Analyzer"
=============================================================================

You have raw tournament data (provided below). Build a system that parses,
analyzes, and reports on it. How you structure your code is up to you.

Run this file when done — the test suite at the bottom checks your work.
Your functions must match the EXACT names and return types listed in each
challenge, but everything else (how you build them, helper functions,
variables, structure) is your call.

=============================================================================
"""

# ============================================================================
# RAW DATA
# ============================================================================

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


# ============================================================================
# CHALLENGES — your functions must use these exact names
# ============================================================================
#
# 1. parse_tournament_data(raw_data)
#    - Takes the raw string above, returns a list of tuples
#    - Each tuple: (player, game, score, result) — all lowercase, score as int
#    - Skip empty lines and lines with invalid/non-numeric scores
#    - Concepts to use: split, strip, lower, try/except, tuples
#
# 2. build_player_stats(parsed_data)
#    - Takes output of #1, returns a dict keyed by player name
#    - Each value should contain: games_played, wins, losses, total_score,
#      and a list of individual scores (key name: "scores")
#    - Concepts to use: dictionaries (nested), tuple unpacking, .get()
#
# 3. Five one-liner functions using the parsed data:
#    - get_unique_players(parsed_data) → list of unique player names
#    - get_wins_only(parsed_data) → only entries where result is "win"
#    - get_last_three(parsed_data) → last 3 entries
#    - get_every_other(parsed_data) → entries at index 0, 2, 4, ...
#    - get_all_scores(parsed_data) → list of just the scores
#    Concepts to use: list comprehensions, slicing, negative indexing
#
# 4. analyze_player(player_stats, player_name)
#    - Returns a tuple: (win_rate, avg_score, best_score, worst_score)
#    - Unknown player → return (0.0, 0, 0, 0)
#    - No global variables — pass everything as parameters
#    - Concepts to use: returning multiple values, scope
#
# 5. numpy_analysis(parsed_data)
#    - Return a dict with keys:
#      "scores" (numpy array), "mean", "median", "std", "min", "max",
#      "above_mean_count" (int — how many scores beat the mean),
#      "matrix" (2D array: each row = [score, 1 for win / 0 for loss]),
#      "just_scores" (first column of matrix),
#      "just_outcomes" (second column of matrix)
#    - Concepts to use: np.array, np.mean/median/std, boolean indexing,
#      2D array slicing
#
# 6. pandas_analysis(parsed_data)
#    - Return a dict with keys:
#      "dataframe" (columns: player, game, score, result),
#      "avg_per_player" (average score grouped by player),
#      "avg_per_game" (average score grouped by game),
#      "high_scorers" (rows where score > 3000),
#      "result_counts" (how many wins vs losses),
#      "best_player" (tuple: (player_name, score) of highest single score)
#    - Concepts to use: pd.DataFrame, groupby, filtering, value_counts
#
# ============================================================================


# WRITE YOUR CODE HERE




# ============================================================================
# 🧪 TESTS — Run this file to check your work
# ============================================================================
import numpy as np
import pandas as pd

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 RUNNING TESTS")
    print("=" * 60)

    passed = 0
    failed = 0

    def test(name, condition):
        global passed, failed
        if condition:
            print(f"  ✅ {name}")
            passed += 1
        else:
            print(f"  ❌ {name}")
            failed += 1

    # --- Challenge 1 ---
    print("\n📝 Challenge 1: Parse Tournament Data")
    parsed = parse_tournament_data(raw_tournament_data)
    test("Returns a list", isinstance(parsed, list))
    test("Has 14 entries (1 bad line skipped)", len(parsed) == 14)
    test("Entries are tuples", len(parsed) > 0 and isinstance(parsed[0], tuple))
    test("Names are lowercase", len(parsed) > 0 and parsed[0][0] == "playerone")
    test("Scores are ints", len(parsed) > 0 and isinstance(parsed[0][2], int))
    test("Bad data line was skipped", all(isinstance(e[2], int) for e in parsed))

    # --- Challenge 2 ---
    print("\n📝 Challenge 2: Build Player Stats")
    stats = build_player_stats(parsed)
    test("Returns a dict", isinstance(stats, dict))
    test("Has 5 players", len(stats) == 5)
    test("playerone has correct wins", stats.get("playerone", {}).get("wins") == 2)
    test("playerfive has 3 games", stats.get("playerfive", {}).get("games_played") == 3)
    test("scores list exists", isinstance(stats.get("playerone", {}).get("scores"), list))

    # --- Challenge 3 ---
    print("\n📝 Challenge 3: Comprehensions & Slicing")
    players = get_unique_players(parsed)
    test("Unique players = 5", players is not None and len(set(players)) == 5)
    wins = get_wins_only(parsed)
    test("Wins only has 9 entries", wins is not None and len(wins) == 9)
    last3 = get_last_three(parsed)
    test("Last 3 entries", last3 is not None and len(last3) == 3)
    every_other = get_every_other(parsed)
    test("Every other entry", every_other is not None and len(every_other) == 7)
    scores = get_all_scores(parsed)
    test("All scores extracted", scores is not None and len(scores) == 14)

    # --- Challenge 4 ---
    print("\n📝 Challenge 4: Analyze Player")
    result = analyze_player(stats, "playerfive")
    test("Returns a tuple", isinstance(result, tuple))
    test("Has 4 values", len(result) == 4)
    test("Win rate is 1.0 for playerfive", result[0] == 1.0)
    test("Unknown player returns zeros", analyze_player(stats, "nobody") == (0.0, 0, 0, 0))

    # --- Challenge 5 ---
    print("\n📝 Challenge 5: NumPy Analysis")
    np_result = numpy_analysis(parsed)
    test("Scores is numpy array", isinstance(np_result["scores"], np.ndarray))
    test("Mean is reasonable", np_result["mean"] is not None and 2500 < np_result["mean"] < 4000)
    test("Above mean count is int", isinstance(np_result["above_mean_count"], (int, np.integer)))
    test("Matrix has 2 columns", np_result["matrix"] is not None and np_result["matrix"].shape[1] == 2)
    test("just_scores matches first column", np_result["just_scores"] is not None and len(np_result["just_scores"]) == 14)

    # --- Challenge 6 ---
    print("\n📝 Challenge 6: Pandas Analysis")
    pd_result = pandas_analysis(parsed)
    test("DataFrame created", isinstance(pd_result["dataframe"], pd.DataFrame))
    test("DataFrame has 14 rows", len(pd_result["dataframe"]) == 14)
    test("avg_per_player exists", pd_result["avg_per_player"] is not None)
    test("high_scorers filtered", pd_result["high_scorers"] is not None and all(pd_result["high_scorers"]["score"] > 3000))
    test("best_player is tuple", isinstance(pd_result["best_player"], tuple))
    test("best_player is playerfive with 4500", pd_result["best_player"] == ("playerfive", 4500))

    # --- Summary ---
    print(f"\n{'=' * 60}")
    print(f"🏁 RESULTS: {passed} passed, {failed} failed out of {passed + failed}")
    print(f"{'=' * 60}")
