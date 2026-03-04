#Prisoner's Dilemma
#If two criminals were caught((i.e, two players)) , they were interrogated separately they got two choices(defect\cooperate).
#And their reward or payoff would be lke 
#                 Prioner 2
#             | C               |     D            |
#Prisone 1  C |    (-1,-1)      |     (-3, 0)      |
#           D |    (0, -3)      |     (-2,-2)      |
# 0 means he will be free.
# -1 means he will lose 1 year of freedom
# -2 means he will lose 2 year of freedom
# -3 means he will lose 3 year of freedom

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
  print("="*90)
  print(f"{' NORMAL FORM GAME - PRISONER\'S DILEMMA':>59}")
  print("="*90)

#calling function
display_game(players, strategies, payoff_matrix)
print(f"{'Prisoner 2':>53}")

print(f"{' ':20}",end=" ")
for s2 in strategies:  #printing header row
   print(f"{s2:>20}",end=" ")
print()
print("-"*90)

#For rows -outer loop
for s1 in strategies:
  print(f"{'Prisoner 1':<13}",end=" ")
  print(f"{s1:14}",end=" ") # print player 1 stragies on the left
  #inner loop for payoffs
  for s2 in strategies:
    payoff=payoff_matrix[(s1,s2)]
    cell = f"({payoff[0]}, {payoff[1]})"
    print(f"{cell:^20}",end=" ") #inner loop ends
  print()#outer loop ends

print("-"*90)
print()

#function definition
def explain_game(players, strategies, payoff_matrix):
  print("\n📖 GAME EXPLANATION")
  print("-" * 50)

# Print player info
for i, player in enumerate(players):
   print(f"Player {i+1}: {player}")
   print(f"  Strategies: {', '.join(strategies)}")

#Printing all possible outcomes
print("\n📊 All possible outcomes:")
for (s1, s2), (p1, p2) in payoff_matrix.items():
  print(f"  {players[0]} plays {s1}, {players[1]} plays {s2}")
  print(f"    → {players[0]} gets {p1} years, {players[1]} gets {p2} years")

