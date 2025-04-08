The Trilogic Game
=================

Later I came to know it as the Towers of Hanoi problem, but I first encountered it in 196x in as a challenge to Doctor Who set by the Celestial Toymaker. For his amusement, the Toymaker (played by a very menacing Michael Gough) had captured the Doctor and his companions, snatching the Tardis out of time and space. They would be released only if they overcame games and puzzles he set them.

![The Doctor and the Celestial Toymaker](p0122yr7.jpg)

The Doctor’s challenge was ‘The Trilogic Game’. A triangular board had at one corner ten triangles of different sizes, stacked from largest to smallest. Moving only one triangle at a time, the Doctor was to shift the entire stack from one corner of the board to another, never placing a larger triangle on a smaller. 

![The Trilogic Game](toymaker-d.jpg)

He had no more than 1,023 moves. 

![The game in progress](toymker10.jpg)

I was horrified and fascinated. I struggled to solve mate-in-3 chess problems. How could even Doctor Who envisage a thousand-move solution? Unless… was there a system that would save him and his companions?

And there it came to me. If there were a solution for nine triangles, he could move the top nine from A to C, the bottom triangle from A to B, then the top nine from C to B. And the solution for ten triangles could be applied for smaller numbers. I just needed a solution for two triangles. I had stumbled upon induction – or in coding, recursion.

First Python solution
---------------------

Asked for code for the Towers of Hanoi, ChatGPT immediately produced a recursive solution. 
The recursive core is in `move()`.

```python
def move(n, source, target, auxiliary, towers):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Move disk {disk} from {source} to {target}")
        print_towers(towers)
    else:
        move(n - 1, source, auxiliary, target, towers)
        move(1, source, target, auxiliary, towers)
        move(n - 1, auxiliary, target, source, towers)
```

Disks, not triangles. Here we see my childhood logic: if moving one disk, just move it to the target. Otherwise move _n-1_ to the auxiliary, move 1 to the target, move _n-1_  from auxiliary to target.

The rest of the code just sets up the board (`tower_of_hanoi()`), displays the board state (`print_towers()`) and (`main`) asks how high a tower you want. 

APL from Python
---------------
