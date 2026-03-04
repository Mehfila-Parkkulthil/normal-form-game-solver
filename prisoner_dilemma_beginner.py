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
strategies =["C","D"]
payoff_matrix={
  ("C","C") : (-1,-1),
  ("C","D") : (-3,0),
  ("D","C") : (0,-3),
  ("D","D") : (-2,-2)
}

#function definition 
def display_game(players, strategies,payofff_matrix):
  print("="*50)
  print("   NORMAL FORM GAME - PRISONER'S DILEMMA")
  print("="*50)

display_game(players, strategies, payoff_matrix)