import random
import os
import re

def check_play_status():
    valid_responses = ['yes', 'no', 'y']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() in ['yes', 'y']:
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)

def play_rps():
    user_score = 0
    computer_score = 0
    play = True

    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nRock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon [R]ock, [P]aper, or [S]cissors: ')

        if not re.match("^[RrPpSs]$", user_choice):
            print('Invalid choice! Try again.')
            continue

        print(f'You chose: {user_choice.upper()}')
        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)
        print(f'I chose: {opp_choice}')

        if opp_choice == user_choice.upper():
            print('It\'s a Tie!')
        elif (opp_choice == 'R' and user_choice.upper() == 'S') or \
             (opp_choice == 'S' and user_choice.upper() == 'P') or \
             (opp_choice == 'P' and user_choice.upper() == 'R'):
            print(f'{opp_choice} beats {user_choice.upper()}, I win!')
            computer_score += 1
        else:
            print(f'{user_choice.upper()} beats {opp_choice}, You win!')
            user_score += 1

        print(f'Score - You: {user_score}, Computer: {computer_score}')
        play = check_play_status()

if __name__ == '__main__':
    play_rps()