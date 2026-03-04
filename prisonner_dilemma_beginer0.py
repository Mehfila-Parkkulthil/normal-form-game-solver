# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============================================================
# NORMAL FORM GAME SOLVER - BEGINNER VERSION
# ============================================================

# STEP 1: Players and Strategies
players = ["Prisoner 1", "Prisoner 2"]
strategies = ["Cooperate", "Defect"]

# STEP 2: Payoff Matrix
payoff_matrix = {
    ("Cooperate", "Cooperate"): (-1, -1),
    ("Cooperate", "Defect"):    (-3,  0),
    ("Defect",    "Cooperate"): ( 0, -3),
    ("Defect",    "Defect"):    (-2, -2),
}

# STEP 3: Display Table
def display_game(players, strategies, payoff_matrix):
    print("\n" + "=" * 55)
    print("      NORMAL FORM GAME - PRISONER'S DILEMMA")
    print("=" * 55)
    print(f"\n  Player 1 (rows)   : {players[0]}")
    print(f"  Player 2 (columns): {players[1]}")

    print(f"\n{'':22}", end="")
    for s2 in strategies:
        print(f"{s2:>16}", end="")
    print()

    print("  " + "-" * 52)

    for s1 in strategies:
        print(f"  {s1:<20}", end="")
        for s2 in strategies:
            payoff = payoff_matrix[(s1, s2)]
            cell = f"({payoff[0]}, {payoff[1]})"
            print(f"{cell:>16}", end="")
        print()

    print("  " + "-" * 52)
    print("  Format: (Player 1 payoff, Player 2 payoff)")
    print("  Payoff = years in jail (lower = worse)")
    print("=" * 55)

# STEP 4: Explain Outcomes
def explain_game(players, strategies, payoff_matrix):
    print("\n PLAIN ENGLISH EXPLANATION")
    print("-" * 55)

    for i, player in enumerate(players):
        print(f"  Player {i+1}: {player}")
        print(f"    Available strategies: {', '.join(strategies)}")

    print("\n ALL POSSIBLE OUTCOMES:")
    print("-" * 55)

    for (s1, s2), (p1, p2) in payoff_matrix.items():
        print(f"\n  >> {players[0]} chooses '{s1}'")
        print(f"     {players[1]} chooses '{s2}'")
        print(f"     Result -> {players[0]} gets {abs(p1)} year(s) in jail, {players[1]} gets {abs(p2)} year(s) in jail")

        if s1 == "Cooperate" and s2 == "Cooperate":
            print("     Both stay silent. Light sentence for everyone.")
        elif s1 == "Cooperate" and s2 == "Defect":
            print(f"     {players[0]} trusted but got betrayed. Worst outcome for P1.")
        elif s1 == "Defect" and s2 == "Cooperate":
            print(f"     {players[1]} trusted but got betrayed. Worst outcome for P2.")
        else:
            print("     Both betrayed each other. Bad for both.")

# STEP 5: Summary
def summarise_game(players, strategies, payoff_matrix):
    print("\n GAME SUMMARY")
    print("-" * 55)
    print(f"  Number of players     : {len(players)}")
    print(f"  Strategies per player : {len(strategies)}")
    print(f"  Total outcomes        : {len(payoff_matrix)}")
    print(f"  (= {len(strategies)} strategies ^ {len(players)} players = {len(strategies)**len(players)} combinations)")
    print("=" * 55)

# STEP 6: Run
if __name__ == "__main__":
    display_game(players, strategies, payoff_matrix)
    explain_game(players, strategies, payoff_matrix)
    summarise_game(players, strategies, payoff_matrix)
    print("\n Beginner solver complete!\n")