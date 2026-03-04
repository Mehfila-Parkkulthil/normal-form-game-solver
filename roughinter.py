# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#Players, Strategies, Payoff Matrix
players = ["Prisoner 1", "Prisoner 2"]
strategies = ["Cooperate", "Defect"]

payoff_matrix = {
    ("Cooperate", "Cooperate"): (-1, -1),
    ("Cooperate", "Defect"):    (-3,  0),
    ("Defect",    "Cooperate"): ( 0, -3),
    ("Defect",    "Defect"):    (-2, -2),
}

# Display Payoff Matrix
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
    print("=" * 55)

#Best Response for Player 1
def best_responses_p1(strategies, payoff_matrix, p2_strategy):
    best_payoff = None
    best_moves = []
    for s1 in strategies:
        p1_payoff = payoff_matrix[(s1, p2_strategy)][0]
        if best_payoff is None or p1_payoff > best_payoff:
            best_payoff = p1_payoff
            best_moves = [s1]
        elif p1_payoff == best_payoff:
            best_moves.append(s1)
    return best_moves

# STEP 4: Best Response for Player 2
# def best_responses_p2(strategies, payoff_matrix, p1_strategy):
#     best_payoff = None
#     best_moves = []
#     for s2 in strategies:
#         p2_payoff = payoff_matrix[(p1_strategy, s2)][1]
#         if best_payoff is None or p2_payoff > best_payoff:
#             best_payoff = p2_payoff
#             best_moves = [s2]
#         elif p2_payoff == best_payoff:
#             best_moves.append(s2)
#     return best_moves

# # STEP 5: Find Nash Equilibria
# def find_nash_equilibria(strategies, payoff_matrix):
#     nash_equilibria = []
#     for s1 in strategies:
#         for s2 in strategies:
#             p1_best = best_responses_p1(strategies, payoff_matrix, s2)
#             p2_best = best_responses_p2(strategies, payoff_matrix, s1)
#             if s1 in p1_best and s2 in p2_best:
#                 nash_equilibria.append((s1, s2))
#     return nash_equilibria

# # STEP 6: Display Best Responses
# def display_best_responses(players, strategies, payoff_matrix):
#     print("\n BEST RESPONSE ANALYSIS")
#     print("-" * 55)
#     print(f"\n  {players[0]}'s Best Responses:")
#     for s2 in strategies:
#         br = best_responses_p1(strategies, payoff_matrix, s2)
#         print(f"    If {players[1]} plays '{s2}' -> Best Response: {', '.join(br)}")
#     print(f"\n  {players[1]}'s Best Responses:")
#     for s1 in strategies:
#         br = best_responses_p2(strategies, payoff_matrix, s1)
#         print(f"    If {players[0]} plays '{s1}' -> Best Response: {', '.join(br)}")

# # STEP 7: Display Nash Equilibria
# def display_nash_equilibria(players, strategies, payoff_matrix):
#     nash_equilibria = find_nash_equilibria(strategies, payoff_matrix)
#     print("\n NASH EQUILIBRIUM RESULTS")
#     print("-" * 55)

#     if not nash_equilibria:
#         print("  No pure strategy Nash Equilibrium found.")
#         print("  (This game may only have a mixed strategy NE)")
#     else:
#         print(f"  Found {len(nash_equilibria)} Nash Equilibrium/Equilibria:\n")
#         for (s1, s2) in nash_equilibria:
#             payoff = payoff_matrix[(s1, s2)]
#             print(f"  ** Nash Equilibrium: ({s1}, {s2})")
#             print(f"     Payoffs: {players[0]} = {payoff[0]}, {players[1]} = {payoff[1]}")
#             print(f"     Why?")
#             print(f"       - '{s1}' is {players[0]}'s best response to '{s2}'")
#             print(f"       - '{s2}' is {players[1]}'s best response to '{s1}'")
#             print(f"       - Neither player can improve by switching. Stable!")
#     print("=" * 55)

# # RUN
# if __name__ == "__main__":
#     display_game(players, strategies, payoff_matrix)
#     display_best_responses(players, strategies, payoff_matrix)
#     display_nash_equilibria(players, strategies, payoff_matrix)
#     print("\n Intermediate solver complete! Next: Advanced adds Mixed Strategy NE.\n")