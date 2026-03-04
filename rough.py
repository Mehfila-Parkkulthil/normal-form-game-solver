#Defining players, strategies and payoff matrix
players=["P1","P2"]
strategies =["Cooperate","Defect"]
payoff_matrix={
  ("Cooperate","Cooperate") : (-1,-1),
  ("Cooperate","Defect") : (-3,0),
  ("Defect","Cooperate") : (0,-3),
  ("Defect","Defect") : (-2,-2)
}

#function definition 
def display_game(players, strategies,payoff_matrix):
  print("="*50)
  print("   NORMAL FORM GAME - PRISONER'S DILEMMA")
  print("="*50)

#calling function
display_game(players, strategies, payoff_matrix)
print(f"\n{'':20}",end=" ")

#printing header row
for s2 in strategies:
  print(f"{s2:>15}",end=" ")
print()
print("-"*50)

#For rows
for s1 in strategies:
  # print player 1 stragies on the left 
  print(f"{s1:20}",end=" ")
  for s2 in strategies:
    payoff=payoff_matrix[(s1,s2)]
  cell = f"({payoff[0]}, {payoff[1]})"
  print(f"{cell:>15}", end="")
print()
print("-"*50)

def explain_game(players, strategies, payoff_matrix):
  print("\n📖 GAME EXPLANATION")
  print("-" * 50)

    # Print player info
  for i, player in enumerate(players):
  # enumerate() gives you both the index (i) and the value (player)
  # i=0 → "Prisoner 1", i=1 → "Prisoner 2"
    print(f"Player {i+1}: {player}")
    print(f"  Strategies: {', '.join(strategies)}")
        # join() connects list items with a separator
        # ['Cooperate', 'Defect'] → "Cooperate, Defect"

  print("\n📊 All possible outcomes:")
  for (s1, s2), (p1, p2) in payoff_matrix.items():
        # .items() gives you both key and value at the same time
        # (s1, s2) unpacks the key tuple
        # (p1, p2) unpacks the value tuple
    print(f"  {players[0]} plays {s1}, {players[1]} plays {s2}")
    print(f"    → {players[0]} gets {p1} years, {players[1]} gets {p2} years")

# This is the main block
# "if __name__ == '__main__'" means:
# Only run this code if you run THIS file directly
# (not if another file imports it)

if __name__ == "__main__":
    display_game(players, strategies, payoff_matrix)
    explain_game(players, strategies, payoff_matrix)