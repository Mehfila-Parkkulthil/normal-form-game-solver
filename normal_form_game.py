# NORMAL FORM GAME

import random

#defining borders
def print_line(char="-", length=55):
    print("  " + char * length)

#defining headers for game
def print_header(title):
    print_line("=")
    print(f"  {title}")
    print_line("=")

#defining game
def setup_game():
    print_header("GAME THEORY - NASH EQUILIBRIUM FINDER") #calling function

    # Player name
    player_name = input("\n  Enter your name: ").strip() or "Player 1"
    computer_name = "Computer"

    # Strategies
    print("\n  Enter shared strategies (comma separated)")
    print("  Example: Rock, Paper, Scissors")
    raw = input("  Strategies: ").strip()
    strategies = [s.strip() for s in raw.split(",") if s.strip()]

    if len(strategies) < 2:
        print("\n  Need at least 2 strategies. Using defaults: A, B")
        strategies = ["A", "B"]

    print(f"\n  Strategies set: {strategies}")

    # Payoff matrix
    print("\n  Now enter payoffs for each combination.")
    print(f"  Format: your payoff, computer payoff  (e.g. 3, -1)")
    print_line()

    payoff_matrix = {}
    for s1 in strategies:
        for s2 in strategies:
            while True:
                try:
                    raw = input(f"  You play '{s1}', Computer plays '{s2}': ").strip()
                    parts = raw.split(",")
                    p1 = int(parts[0].strip())
                    p2 = int(parts[1].strip())
                    payoff_matrix[(s1, s2)] = (p1, p2)
                    break
                except:
                    print("  Invalid input. Try again e.g. 3, -1")

    return player_name, computer_name, strategies, payoff_matrix


# display payoff matrix
def display_matrix(player_name, computer_name, strategies, payoff_matrix):
    print_header("PAYOFF MATRIX") #calling function
    print(f"  Rows = {player_name}  |  Columns = {computer_name}")
    print(f"  Each cell = (Your payoff, Computer payoff)\n")

    # Header row
    print(f"  {'':20}", end="")
    for s2 in strategies:
        print(f"{s2:>16}", end="")
    print()
    print_line()

    # Data rows
    for s1 in strategies:
        print(f"  {s1:<20}", end="")
        for s2 in strategies:
            p = payoff_matrix[(s1, s2)]
            cell = f"({p[0]}, {p[1]})"
            print(f"{cell:>16}", end="")
        print()
    print_line()

#Best responses
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

#  Nash Equilibuim
def find_nash_equilibria(strategies, payoff_matrix):
    nash = []
    for s1 in strategies:
        for s2 in strategies:
            p1_best = best_responses_p1(strategies, payoff_matrix, s2)
            p2_best = best_responses_p2(strategies, payoff_matrix, s1)
            if s1 in p1_best and s2 in p2_best:
                nash.append((s1, s2))
    return nash

#display analysis
def display_analysis(player_name, computer_name, strategies, payoff_matrix):
    print_header("BEST RESPONSE ANALYSIS")

    print(f"\n  {player_name}'s Best Responses:")
    for s2 in strategies:
        br = best_responses_p1(strategies, payoff_matrix, s2)
        print(f"    If {computer_name} plays '{s2}' -> Best Response: {', '.join(br)}")

    print(f"\n  {computer_name}'s Best Responses:")
    for s1 in strategies:
        br = best_responses_p2(strategies, payoff_matrix, s1)
        print(f"    If {player_name} plays '{s1}' -> Best Response: {', '.join(br)}")

    # Nash
    print_header("NASH EQUILIBRIUM RESULTS")
    nash = find_nash_equilibria(strategies, payoff_matrix)

    if not nash:
        print("  No pure strategy Nash Equilibrium found.")
        print("  This game may only have a mixed strategy NE.")
    else:
        print(f"  Found {len(nash)} Nash Equilibrium/Equilibria:\n")
        for (s1, s2) in nash:
            payoff = payoff_matrix[(s1, s2)]
            print(f"  ** Nash Equilibrium: ({s1}, {s2})")
            print(f"     {player_name} payoff = {payoff[0]}  |  {computer_name} payoff = {payoff[1]}")
            print(f"     Neither player can improve by switching alone.")
            print()
    print_line("=")

#if the user want to play next round
def play_round(player_name, computer_name, strategies, payoff_matrix):
    print_header("PLAY A ROUND")

    # Show options
    print(f"\n  Choose your strategy:")
    for i, s in enumerate(strategies):
        print(f"    {i+1}. {s}")

    # User picks
    while True:
        try:
            choice = int(input("\n  Your choice (number): ").strip())
            if 1 <= choice <= len(strategies):
                user_move = strategies[choice - 1]
                break
            else:
                print(f"  Enter a number between 1 and {len(strategies)}")
        except:
            print("  Invalid input. Enter a number.")

    # Computer picks — uses its best response
    comp_best = best_responses_p2(strategies, payoff_matrix, user_move)
    comp_move = random.choice(comp_best)   # pick randomly if tied

    print(f"\n  You played    : {user_move}")
    print(f"  Computer played: {comp_move}")

    payoff = payoff_matrix[(user_move, comp_move)]
    print(f"\n  Result:")
    print(f"    Your payoff      = {payoff[0]}")
    print(f"    Computer payoff  = {payoff[1]}")

    if payoff[0] > payoff[1]:
        print(f"\n  You came out ahead this round!")
    elif payoff[0] < payoff[1]:
        print(f"\n  Computer came out ahead this round.")
    else:
        print(f"\n  Equal payoffs — a draw!")
    print_line()



player_name, computer_name, strategies, payoff_matrix = setup_game()

while True:
  print("\n  MENU")
  print_line()
  print("  1. View Payoff Matrix")
  print("  2. View Best Responses & Nash Equilibrium")
  print("  3. Play a Round vs Computer")
  print("  4. Quit")
  print_line()

  choice = input("  Your choice: ").strip()

  if choice == "1":
    display_matrix(player_name, computer_name, strategies, payoff_matrix)
  elif choice == "2":
    display_analysis(player_name, computer_name, strategies, payoff_matrix)
  elif choice == "3":
    play_round(player_name, computer_name, strategies, payoff_matrix)
  elif choice == "4":
    print("\n  Thanks for playing. Goodbye!\n")
    break
  else:
    print("  Invalid choice. Pick 1-4.")
