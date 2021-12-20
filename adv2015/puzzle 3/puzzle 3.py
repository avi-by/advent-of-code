"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""
count = 1
pos = [0, 0]
pres = {(0, 0): 1}

with open('input.txt') as input:
    for line in input:
        for letter in line:
            if letter == '^':
                pos[0]+=1
            if letter == "v":
                pos[0]-=1
            if letter == '>':
                pos[1]+=1
            if letter == '<':
                pos[1]-=1
            if tuple(pos) not in pres:
                pres[tuple(pos)] = 0
                count += 1
with open('output part 1.txt','w') as output:
    output.write(f'the answer is: {count}')

    """
    --- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
    """
count = 1
spos = [0, 0]
rpos = [0,0]
pres = {(0, 0): 1}
queue = [spos,rpos]
switcher =1
turn=0
with open('input.txt') as input:
    for line in input:
        for letter in line:
            if letter == '^':
                queue[turn][0]+=1
            if letter == "v":
                queue[turn][0]-=1
            if letter == '>':
                queue[turn][1]+=1
            if letter == '<':
                queue[turn][1]-=1
            if tuple(queue[turn]) not in pres:
                pres[tuple(queue[turn])] = 0
                count += 1
            turn+=switcher
            switcher*=-1
with open('output part 2.txt','w') as output:
    output.write(f'the answer is: {count}')
