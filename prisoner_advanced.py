# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# numpy is used for matrix math and solving linear equations
import numpy as np

# ============================================================
# NORMAL FORM GAME SOLVER - ADVANCED VERSION
# New: Mixed Strategy Nash Equilibrium using numpy
# ============================================================

# STEP 1: Players, Strategies, Payoff Matrix
players = ["Prisoner 1", "Prisoner 2"]
strategies = ["Cooperate", "Defect"]

payoff_matrix = {
    ("Cooperate", "Cooperate"): (-1, -1),
    ("Cooperate", "Defect"):    (-3,  0),
    ("Defect",    "Cooperate"): ( 0, -3),
    ("Defect",    "Defect"):    (-2, -2),
}

# ============================================================
# STEP 2: Build Numpy Matrices from payoff_matrix dictionary
# ============================================================
# numpy lets us treat payoffs as a grid of numbers
# p1_matrix[i][j] = Player 1's payoff when P1 plays i, P2 plays j
# p2_matrix[i][j] = Player 2's payoff when P1 plays i, P2 plays j

def build_matrices(strategies, payoff_matrix):
    n = len(strategies)   # number of strategies = 2

    # np.zeros((n, n)) creates an n×n grid filled with 0.0
    # dtype=float means we store decimal numbers
    p1_matrix = np.zeros((n, n), dtype=float)
    p2_matrix = np.zeros((n, n), dtype=float)

    for i, s1 in enumerate(strategies):       # i = row index
        for j, s2 in enumerate(strategies):   # j = column index
            p1_matrix[i][j] = payoff_matrix[(s1, s2)][0]  # P1's payoff
            p2_matrix[i][j] = payoff_matrix[(s1, s2)][1]  # P2's payoff

    return p1_matrix, p2_matrix

# ============================================================
# STEP 3: Display Payoff Matrix
# ============================================================

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

# ============================================================
# STEP 4: Find Pure Strategy Nash Equilibria (from intermediate)
# ============================================================

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

def best_responses_p2(strategies, payoff_matrix, p1_strategy):
    best_payoff = None
    best_moves = []
    for s2 in strategies:
        p2_payoff = payoff_matrix[(p1_strategy, s2)][1]
        if best_payoff is None or p2_payoff > best_payoff:
            best_payoff = p2_payoff
            best_moves = [s2]
        elif p2_payoff == best_payoff:
            best_moves.append(s2)
    return best_moves

def find_pure_nash(strategies, payoff_matrix):
    nash = []
    for s1 in strategies:
        for s2 in strategies:
            p1_best = best_responses_p1(strategies, payoff_matrix, s2)
            p2_best = best_responses_p2(strategies, payoff_matrix, s1)
            if s1 in p1_best and s2 in p2_best:
                nash.append((s1, s2))
    return nash

# ============================================================
# STEP 5: Find Mixed Strategy Nash Equilibrium
# ============================================================
# For a 2x2 game:
# Let p  = probability P1 plays strategies[0] (e.g. Cooperate)
#     1-p = probability P1 plays strategies[1] (e.g. Defect)
# Let q  = probability P2 plays strategies[0]
#     1-q = probability P2 plays strategies[1]
#
# To find p: make P2 indifferent between their strategies
#   P2's expected payoff from Cooperate = P2's expected payoff from Defect
#   p * p2[0][0] + (1-p) * p2[1][0] = p * p2[0][1] + (1-p) * p2[1][1]
#   Solve for p
#
# To find q: make P1 indifferent between their strategies
#   p1[0][0]*q + p1[0][1]*(1-q) = p1[1][0]*q + p1[1][1]*(1-q)
#   Solve for q

def find_mixed_nash(strategies, payoff_matrix):
    p1_matrix, p2_matrix = build_matrices(strategies, payoff_matrix)

    # --- Solve for p (P1's mixing probability) ---
    # Rearranging the indifference equation:
    # p * (p2[0][0] - p2[1][0] - p2[0][1] + p2[1][1]) = p2[1][1] - p2[1][0]
    # p = (p2[1][1] - p2[1][0]) / (p2[0][0] - p2[1][0] - p2[0][1] + p2[1][1])

    # denominator for p
    denom_p = (p2_matrix[0][0] - p2_matrix[1][0]
             - p2_matrix[0][1] + p2_matrix[1][1])

    # denominator for q
    denom_q = (p1_matrix[0][0] - p1_matrix[0][1]
             - p1_matrix[1][0] + p1_matrix[1][1])

    # If denominator is 0, no mixed strategy NE exists (strategies already dominate)
    if abs(denom_p) < 1e-10 or abs(denom_q) < 1e-10:
        # 1e-10 is scientific notation for 0.0000000001
        # we use this instead of == 0 to handle floating point rounding errors
        return None

    p = (p2_matrix[1][1] - p2_matrix[1][0]) / denom_p
    q = (p1_matrix[1][1] - p1_matrix[1][0]) / denom_q

    # p and q must be valid probabilities: between 0 and 1
    if not (0 <= p <= 1 and 0 <= q <= 1):
        return None

    return p, q

# ============================================================
# STEP 6: Calculate Expected Payoffs for Mixed Strategy
# ============================================================
# Once we know p and q, we can calculate what each player
# EXPECTS to earn on average over many rounds

def expected_payoffs(p, q, p1_matrix, p2_matrix):
    # P1's expected payoff:
    # = p*q*payoff(C,C) + p*(1-q)*payoff(C,D) + (1-p)*q*payoff(D,C) + (1-p)*(1-q)*payoff(D,D)
    p1_exp = (p * q * p1_matrix[0][0]
            + p * (1-q) * p1_matrix[0][1]
            + (1-p) * q * p1_matrix[1][0]
            + (1-p) * (1-q) * p1_matrix[1][1])

    # P2's expected payoff: same formula but using p2_matrix
    p2_exp = (p * q * p2_matrix[0][0]
            + p * (1-q) * p2_matrix[0][1]
            + (1-p) * q * p2_matrix[1][0]
            + (1-p) * (1-q) * p2_matrix[1][1])

    return p1_exp, p2_exp

# ============================================================
# STEP 7: Display All Results
# ============================================================

def display_all_results(players, strategies, payoff_matrix):
    p1_matrix, p2_matrix = build_matrices(strategies, payoff_matrix)

    # --- Pure Strategy NE ---
    pure_ne = find_pure_nash(strategies, payoff_matrix)
    print("\n PURE STRATEGY NASH EQUILIBRIA")
    print("-" * 55)
    if not pure_ne:
        print("  None found.")
    else:
        for (s1, s2) in pure_ne:
            payoff = payoff_matrix[(s1, s2)]
            print(f"  ** ({s1}, {s2})")
            print(f"     Payoffs: {players[0]}={payoff[0]}, {players[1]}={payoff[1]}")

    # --- Mixed Strategy NE ---
    print("\n MIXED STRATEGY NASH EQUILIBRIUM")
    print("-" * 55)
    result = find_mixed_nash(strategies, payoff_matrix)

    if result is None:
        print("  No mixed strategy NE exists.")
        print("  (One strategy strictly dominates — no reason to mix)")
    else:
        p, q = result
        # round(p, 4) rounds to 4 decimal places for clean display
        print(f"  {players[0]} plays '{strategies[0]}' with probability {round(p, 4)}")
        print(f"  {players[0]} plays '{strategies[1]}' with probability {round(1-p, 4)}")
        print(f"  {players[1]} plays '{strategies[0]}' with probability {round(q, 4)}")
        print(f"  {players[1]} plays '{strategies[1]}' with probability {round(1-q, 4)}")

        p1_exp, p2_exp = expected_payoffs(p, q, p1_matrix, p2_matrix)
        print(f"\n  Expected Payoffs at Mixed NE:")
        print(f"    {players[0]}: {round(p1_exp, 4)} years in jail on average")
        print(f"    {players[1]}: {round(p2_exp, 4)} years in jail on average")

    print("=" * 55)

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    display_game(players, strategies, payoff_matrix)
    display_all_results(players, strategies, payoff_matrix)
    print("\n Advanced solver complete!\n")