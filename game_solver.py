alice_best_responses = {}
bob_best_responses = {}          # ✅ FIXED: moved here, outside the loop

payoff_matrix = [
  [(8,8), (5,3)],
  [(3,5), (1,1)]
]

num_rows = len(payoff_matrix)        # Alice's strategies
num_cols = len(payoff_matrix[0])     # Bob's strategies

# For EACH of Bob's strategies (fix Bob, vary Alice)
for bob_strategy in range(num_cols):
    alice_payoffs = []
    for alice_strategy in range(num_rows):
        alice_payoff, bob_payoff = payoff_matrix[alice_strategy][bob_strategy]
        alice_payoffs.append(alice_payoff)
    max_payoff = max(alice_payoffs)
    best_strategy = alice_payoffs.index(max_payoff)
    alice_best_responses[bob_strategy] = best_strategy

# For EACH of Alice's strategies (fix Alice, vary Bob)
for alice_strategy in range(num_rows):
    bob_payoffs = []
    for bob_strategy in range(num_cols):
        alice_payoff, bob_payoff = payoff_matrix[alice_strategy][bob_strategy]
        bob_payoffs.append(bob_payoff)
    max_payoff = max(bob_payoffs)
    best_strategy = bob_payoffs.index(max_payoff)
    bob_best_responses[alice_strategy] = best_strategy

# Find Nash Equilibrium
for alice_strat in range(num_rows):
    for bob_strat in range(num_cols):
        alice_is_br = (alice_strat == alice_best_responses[bob_strat])
        bob_is_br = (bob_strat == bob_best_responses[alice_strat])
        if alice_is_br and bob_is_br:
            alice_pay, bob_pay = payoff_matrix[alice_strat][bob_strat]
            print(f"✓ NE: (Alice {alice_strat}, Bob {bob_strat}) → ({alice_pay}, {bob_pay})")