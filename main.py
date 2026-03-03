#Two players : Alice and Bob
#Strategies : Study or party
#input the payoff matrices
payoff_matrix=[
  [(8,8),(5,3)],
  [(3,5),(1,1)]
]

#extract number of strategies for each player ie, length of payoff matrix
num_rows=len(payoff_matrix) #alice strategies
num_cols=len(payoff_matrix[0]) #bob strategies

#Best responses for each player
best_responses_Alice=[]
best_responses_Bob=[]

for i in range(num_rows):
  for j in range(num_cols):
    alice_payoff,bob_payoff=payoff_matrix[i][j]
    #to check if this is a best response
    