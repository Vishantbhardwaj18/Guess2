import random

def guess_number_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < random_number:
                print("Too low. Try again!")
            elif guess > random_number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# Start the game
guess_number_game()
