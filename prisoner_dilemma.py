# ============================================================
# NORMAL FORM GAME SOLVER 
# New: PRISONERS DILEMMA GAME
# ============================================================
#Title
print("="*50)
print(f"{'NORMAL FORM GAME SOLVER - PRISONER\'S DILEMMA':^50}")
print("="*50)

#Defining prisoners, strategies and payoffs
prisoners=["P1","P2"]
strategies=["C","D"]
payoff_matrix ={
  ("C","C"):(-1,-1),
  ("C","D"):(-3,0),
  ("D","C"):(0,-3),
  ("D","D"):(-2,-2)
}

#printing header row
print(f"{"Prisoner 2":>35}")
print(f"{' ':20}",end=" ")

#loop for printing strategies of prisoner 2 and s2 (strategy of prisoner 2)
for s2 in strategies:
  print(f"{s2:<15}",end=" ")
print()

#loop for creating strategies of prisoner 1 and payoffs 
#outerloop
for s1 in strategies:
  print(f"{'Prisoner 1'}",end=" ")
  print(f"{s1:>5}" , end=" ")
  #inner loop
  for s2 in strategies :
    payoff =payoff_matrix[(s1,s2)]
    cell=f"{payoff[0],payoff[1]}"
    print(f"{cell:15}",end=" ")
  print() 

print("-"*50)

#Game Explanation
print("\nGame Explanation")
#loop
for i , prisoner in enumerate(prisoners):
  print(f"Prisoner 1 {i+1}:{prisoner}")
  print(f" Strategies :{' , '.join(strategies)}")

print("\n GAME SUMMARY")
print(f"  Number of players     : {len(prisoners)}")
print(f"  Strategies per player : {len(strategies)}")
print(f"  Total outcomes        : {len(payoff_matrix)}")
print(f"  ({len(strategies)} strategies x {len(prisoners)} players = {len(strategies)**len(prisoners)} combinations)")
print("=" * 55)  

print("Lets play a game : You are player 1 and I am player 2")
comp_choice= "Cooperate"
user_choice =input("What do you choose Defect or Cooperate \n").strip().capitalize()
if comp_choice == "Cooperate" and user_choice == "Cooperate":
  print("     Both stay silent. Light sentence for everyone.")
elif comp_choice == "Cooperate" and user_choice == "Defect":
  print(f"     {prisoners[0]} trusted but got betrayed. Worst outcome for P1.")
elif comp_choice == "Defect" and user_choice == "Cooperate":
 print(f"     {prisoners[1]} trusted but got betrayed. Worst outcome for P2.")
else:
 print("     Both betrayed each other. Bad for both.")