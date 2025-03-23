Rock, Paper, Scissors
=====================

First we paste and adapt the Python function definitions as APL functions, keeping as close to the original Python as we can:
`check_play_status` and `rockpaper_py`.

The code offers lots of opportunities to improve it. 
After refactoring in APL, we’ll transfer what we’ve learned back into Python.
(Perhaps it’s easier to think more clearly in APL?)
```apl
  rockpaper_py;f;user_score;computer_score;play;weapons;user_choice;opp_choice
 ⍝ Game of Rock, Paper, Scissors, hewing close to Python solution
 ⍝ https://hackr.io/blog/how-to-create-a-python-rock-paper-scissors-game
 f←##.##.utilities.f

 user_score←0
 computer_score←0

 play←1
 :While play
     'Rock, Paper, Scissors - Shoot!'
     weapons←'RPS'

     :Repeat
         user_choice←1 ⎕C⊃input'Choose your weapon [R]ock, [P]aper, or [S]cissors: '
     :Until user_choice∊weapons
     f'You chose: {user_choice}'

     opp_choice←weapons⊃⍨?≢weapons
     f'I chose: {opp_choice}'

     :If opp_choice=user_choice
         'It’s a Tie!'
     :ElseIf (opp_choice='R')∧user_choice='S'
     :OrIf (opp_choice='S')∧user_choice='P'
     :OrIf (opp_choice='P')∧user_choice='R'
         f'{opp_choice} beats {user_choice}, I win!'
         computer_score+←1
     :Else
         f'{user_choice} beats {opp_choice}, You win!'
         user_score+←1
     :EndIf

     f'Score - You: {user_score}, Computer: {computer_score}'
     play←check_play_status
 :EndWhile

 'Thanks for playing!'
 ```
The main function `rockpaper_py` calls `check_play_status` to set variable `play`, which determines whether to continue the While loop.
But this is deceptive. 

```apl
flag←check_play_status;input;valid_responses;response
 input←{⍞←⍵ ⋄ (≢⍵)↓⍞}
 valid_responses←,¨'yes' 'no' 'y'
 :While 1
     :Trap 6 ⍝ VALUE ERROR
         response←input'Do you wish to play again? (Yes or No): '
         :If ~(⊂⎕C response)∊valid_responses
             {⎕SIGNAL ⍵} 6 ⍝ VALUE ERROR
         :EndIf

         :If (⊂⎕C response)∊,¨'yes' 'y'
             flag←1
             :return
         :Else
            ⍝ os.system('cls' if os.name == 'nt' else 'clear')
             'Thanks for playing!'
             →
         :EndIf
     :Else
        ⍝  except ValueError as err
        ⍝  print(err)
         'Yes or No only'
     :EndTrap
 :EndWhile
```
While `check_play_status` will return `flag` 1 (True) if you answer Yes, it will never return 0 (False).
Instead it exits the program by clearing the execution stack (`→`). 
The While loop in `play_rps_py` is an illusion! 
It were better written as a Repeat with no test so it were at least clear that the path for ending the program is not visible in `rockpaper_py`. 

Most programs at the top level follow a pattern:

1.  set up, e.g. define some constants, open files
1.  do the work
1.  clean up, e.g. erase working files

Crashing out of the program from deep within it is a bad practice.
If this were a program with a clean-up phase, crashing out from a prompt would mean never cleaning up.

The `check_play_status` function _looks_ as if it simply asks a question and returns a flag. 
That would be a better design. Best when a function does a simple job. 
Best too when the logic for terminating a loop is in the same function that runs the loop.

We can raise an eyebrow too at the use of an error trap to handle an invalid response.
Error traps are best reserved for _unforeseen_ program errors.
It can only cause confusion to mix user errors with program errors.
The If/Else construction suffices for handling a user error.

The two prompts can usefully be merged, with Quit as an extra option, and `check_play_status` simply discarded.

What chnges does array thinking suggest?

The two variables `user_choice` and `opp_choice` (why not `computer_choice`?) can become the 2-char string `choices`.
Now `=/choices` replaces `user_choice == opp_choice` and the sequence of tests for pairs condenses to `uwin←(⊂choices)∊'rs' 'sp' 'pr'`.

Similarly, variables `user_score` and `computer_score` can become the pair `scores` (yours and mine) and get incremented in a single expression.

```apl
 rockpaper;f;ans;scores;yours;mine;done;weapons;choices;uwin;wins;loses;winner
 ⍝ APL-literate game of Rock, Paper, Scissors
 f←##.##.utilities.f

 scores←0 0   ⍝ yours, mine
 choices←'  ' ⍝ yours, mine
 weapons←'rps'
 'Rock, Paper, Scissors - Shoot!'

 :Repeat

     :Repeat
         ans←⎕C⊃input'Choose your weapon [R]ock, [P]aper, [S]cissors, or [Q]uit: '
     :Until ans∊'q',weapons

     :If ~done←ans='q'
         (1⊃choices)←ans
         (2⊃choices)←{⍵⊃⍨?≢⍵}weapons

         yours mine←'Rock' 'Paper' 'Scissors'[weapons⍳choices]
         f'You chose: {yours}, I chose: {mine}'

         :If =/choices
             'It’s a Tie!'
         :Else
             uwin←(⊂choices)∊'rs' 'sp' 'pr'
             winner←(uwin+1)⊃'I' 'you'
             wins loses←(~uwin)⌽yours mine
             f'{wins} beats {loses}, and {winner} win!'
             scores+←(~uwin)⌽1 0
         :EndIf

         f'Score - you: {1⊃scores}, me: {2⊃scores}'
     :EndIf

 :Until done

 'Thanks for playing!'
 ```
Refactoring the code like this reveals the core logic more clearly.
Perhaps that helps us write a better version in Python?

```python
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
```

Above, the outer loop manages the replay and keeps the cumulative score.
Forming the string `f'{yc}{mc}'` condenses the multiple tests.