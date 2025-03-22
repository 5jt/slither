# https://hackr.io/blog/how-to-create-a-python-number-guessing-game
import random

def confirm(prompt):
    done = False
    while not done:
        response = input(f"{prompt} (Yes/No): ")
        done = response.lower() in ["yes", "y", "no", "n"]
        if not done:
            print("Please respond with 'yes' or 'no'")

    return response.lower() in ["yes", "y"]

def play_game():
    attempts = 0
    rand_num = random.randint(1, 10)

    done = False
    while not done:
        guess = int(input("Pick a number between 1 and 10: "))

        if guess < 1 or guess > 10:
            print("Please guess a number within the given range")
        else:
            attempts += 1

            done = guess == rand_num
            if done:
                print("Nice! You got it! 🎉")
                print(f"It took you {attempts} attempts.")
            else:
                if guess > rand_num:
                    print("It's lower! 📉")
                elif guess < rand_num:
                    print("It's higher! 📈")

    return attempts

if __name__ == "__main__":
    print("Hello, traveler! Welcome to the game of guesses!")
    attempts_list = []

    wanna_play = True
    while wanna_play:
        attempts = play_game()
        attempts_list.append(attempts)
        print(f"The current best score is {min(attempts_list)} attempts.")
        wanna_play = confirm("Would you like to play again?")

    print("Thanks for playing!")