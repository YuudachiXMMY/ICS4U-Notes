import random

# Helper function to simulate one game and check if it is a win
def play_game():
    # Simulate the coin flip (1 for Heads, 0 for Tails)
    coin_flip = random.choice([0, 1])  # 1 for Heads, 0 for Tails
    
    # Simulate the dice rolls (values between 1 and 6)
    die1 = random.randint(1, 6)  # First dice
    die2 = random.randint(1, 6)  # Second dice
    die3 = random.randint(1, 6)  # Third dice
    
    # Check if the game is won
    if (coin_flip == 1 and 
        die1 % 2 == 0 and  # First die is even
        die2 % 2 != 0 and  # Second die is odd
        2 <= die3 <= 4):   # Third die is between 2 and 4 inclusive
        return True
    return False

# Recursive function to simulate multiple games and calculate the probability
def simulate_games(num_games, total_wins=0, total_games=0):
    # Base case: if no more games to simulate, return the probability
    if total_games == num_games:
        probability = (total_wins / total_games) * 100 if total_games > 0 else 0
        print("Experimental Probability of Winning: ", probability)
        return
    
    # Recursive case: simulate one game
    total_games += 1
    if play_game():
        total_wins += 1
    
    # Recursively simulate the next game
    simulate_games(num_games, total_wins, total_games)

# Main function to run the program
def main():
    # Generate a random number of games between 100 and 1000
    num_games = random.randint(100, 1000)
    print("Simulating games...", num_games)
    
    # Call the recursive function to simulate games
    simulate_games(num_games)

main()
