import random

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 9): "))
            if 1 <= guess <= 9:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_guessing_game():
    print("Number guessing game")
    number = random.randint(1, 9)
    chances = 0

    while True:
        guess = get_user_guess()
        chances += 1

        if guess == number:
            print(f'CONGRATULATIONS! YOU GUESSED THE NUMBER {number} IN {chances} ATTEMPTS!')
            break
        elif guess < number:
            print(f"Your guess was too low. Guess a number higher than {guess}.")
        else:
            print(f"Your guess was too high. Guess a number lower than {guess}.")

if __name__ == "__main__":
    play_guessing_game()
