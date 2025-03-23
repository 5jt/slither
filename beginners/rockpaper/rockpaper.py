import random

def play_rps():
    print('\nRock, Paper, Scissors - Shoot!')
    weapons = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}

    done = False
    while not done:
        ans = input('Choose your weapon [R]ock, [P]aper, or [S]cissors: ').upper()[0]
        print(ans)
        done = ans in weapons.keys()
        if not done:
            print('Invalid choice! Try again.')

    yc = ans # your choice
    mc  = random.choice(list(weapons.keys())) # my choice
    print(f'You chose: {weapons[yc]} and I chose {weapons[mc]}')

    if yc == mc:
        print('It\'s a Tie!')
        results = [0, 0]
    elif f'{yc}{mc}' in ['RS', 'SP', 'PR']:

        print(f'{weapons[yc]} beats {weapons[mc]}, you win!')
        results = [1, 0]
    else:
        print(f'{weapons[mc]} beats {weapons[yc]}, I win!')
        results = [0, 1]

    return results

if __name__ == '__main__':
    scores = [0, 0] # [your_score, my_score]

    done = False
    while not done:
        res = play_rps()
        scores[0] += res[0]
        scores[1] += res[1]
        print(f'Score - You: {scores[0]}, Me: {scores[1]}')
        done = input('Play again? (Yes or No): ').lower() not in ['yes', 'y']

    print('Thanks for playing!')
