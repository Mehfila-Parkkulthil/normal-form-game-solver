# ============================================================
# NORMAL FORM GAME SOLVER 
# New: Best Response Analysis + Pure Strategy Nash Equilibrium
# ============================================================

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
print("\n" + "=" * 60)
print(f"{'NORMAL FORM GAME - PRISONER\'S DILEMMA':^60}")
print("=" * 60)

#adding header rows
print(f"{' Prisoner 2':>50}")
print(f"\n{'':>20}", end="")

#adding player2 strategies(s2)
for s2 in strategies:
    print(f"{s2:>20}", end="")
print()
print("-" * 60)

#outer loop adding payoff 
for s1 in strategies:
    print(f"{'  Prisoner 1':10}",end=" ")
    print(f"  {s1:<10}", end="")
    for s2 in strategies:
        payoff = payoff_matrix[(s1, s2)]
        cell = f"({payoff[0]}, {payoff[1]})"
        print(f"{cell:>16}", end="")
    print()

print("-" * 60)

# Best Response for Player 1 
#s1-strategy of player 1
#s2-strategy of player 2
def best_responses_p1(strategies, payoff_matrix, s2):
    best_payoff = None
    best_moves = []
    for s1 in strategies:
        p1_payoff = payoff_matrix[(s1, s2)][0]
        if best_payoff is None or p1_payoff > best_payoff:
            best_payoff = p1_payoff
            best_moves = [s1]
        elif p1_payoff == best_payoff:
            best_moves.append(s1)
    return best_moves

# Best Response for Player 2
def best_responses_p2(strategies, payoff_matrix, s1):
    best_payoff = None
    best_moves = []
    for s2 in strategies:
        p2_payoff = payoff_matrix[(s1, s2)][1]
        if best_payoff is None or p2_payoff > best_payoff:
            best_payoff = p2_payoff
            best_moves = [s2]
        elif p2_payoff == best_payoff:
            best_moves.append(s2)
    return best_moves

#  Find Nash Equilibria
def find_nash_equilibria(strategies, payoff_matrix):
    nash_equilibria = []
    for s1 in strategies:
        for s2 in strategies:
            p1_best = best_responses_p1(strategies, payoff_matrix, s2)
            p2_best = best_responses_p2(strategies, payoff_matrix, s1)
            if s1 in p1_best and s2 in p2_best:
                nash_equilibria.append((s1, s2))
    return nash_equilibria

#  Display Best Responses
def display_best_responses(players, strategies, payoff_matrix):
    print("\n  BEST RESPONSE ANALYSIS")
    print("-" * 60)
    print(f"\n  {players[0]}'s Best Responses:")
    for s2 in strategies:
        br = best_responses_p1(strategies, payoff_matrix, s2)
        print(f"    If {players[1]} plays '{s2}' -> Best Response: {', '.join(br)}")
    print(f"\n  {players[1]}'s Best Responses:")
    for s1 in strategies:
        br = best_responses_p2(strategies, payoff_matrix, s1)
        print(f"    If {players[0]} plays '{s1}' -> Best Response: {', '.join(br)}")

#  Display Nash Equilibria
def display_nash_equilibria(players, strategies, payoff_matrix):
    nash_equilibria = find_nash_equilibria(strategies, payoff_matrix)
    print("\n NASH EQUILIBRIUM RESULTS")
    print("-" * 60)

    if not nash_equilibria:
        print("  No pure strategy Nash Equilibrium found.")
        print("  (This game may only have a mixed strategy NE)")
    else:
        print(f"  Found {len(nash_equilibria)} Nash Equilibrium/Equilibria:\n")
        for (s1, s2) in nash_equilibria:
            payoff = payoff_matrix[(s1, s2)]
            print(f"     Nash Equilibrium: ({s1}, {s2})")
            print(f"     Payoffs: {players[0]} = {payoff[0]}, {players[1]} = {payoff[1]}")
            print(f"     Why?")
            print(f"       - '{s1}' is {players[0]}'s best response to '{s2}'")
            print(f"       - '{s2}' is {players[1]}'s best response to '{s1}'")
            print(f"       - Neither player can improve by switching. Stable!")
    print("=" * 60)


display_best_responses(players, strategies, payoff_matrix)
display_nash_equilibria(players, strategies, payoff_matrix)