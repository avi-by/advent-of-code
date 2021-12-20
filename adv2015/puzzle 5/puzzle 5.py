"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
"""
counter=0
vowels_letter=['a','e','i','o','u']
naughty_letters=[ 'ab', 'cd', 'pq', 'xy']
with open('input.txt') as input:
    for line in input:
        naughty = False
        vowels = 0
        last_letter = ""
        double_letter = False
        for letter in line:
            if letter == last_letter:
                double_letter = True
            if letter in vowels_letter:
                vowels+=1
            if last_letter+letter in naughty_letters:
                naughty=True
            last_letter=letter
        if not naughty and double_letter and vowels >= 3:
            counter+=1
with open('output part 1.txt','w') as output:
    output.write(f'the answer is: {counter}')
"""
test=['ugknbfddgicrmopn','jchzalrnumimnmhp','haegwjzuvuyypxyu','dvszwmarrgswjxmb']
for line in test:
    naughty = False
    vowels = 0
    last_letter = ""
    double_letter = False
    for letter in line:
        if letter == last_letter:
            double_letter = True
        if letter in vowels_letter:
            vowels += 1
        if last_letter + letter in naughty_letters:
            naughty = True
        last_letter = letter
    if not naughty and double_letter and vowels >= 3:
        print(f'{line} is: not naughty')
    else:
        print(f'{line} is: naughty')
"""

"""
-- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

counter=0
with open('input.txt') as input:
    for line in input:
        last_letter = ""
        two_back_latter = ""
        pair_found = []
        last_pair = ""
        repeat_letter = False
        repeat_pair=False
        for letter in line:
            if two_back_latter == letter:
                repeat_letter = True
            if last_letter + letter in pair_found:
                repeat_pair = True
            pair_found.append(last_pair)
            last_pair = last_letter + letter
            two_back_latter = last_letter
            last_letter = letter
        if repeat_pair and repeat_letter:
            counter+=1
with open('output part 2.txt','w') as output:
    output.write(f'the answer is: {counter}')
"""
tests=['qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy']
for line in tests:
    last_letter = ""
    two_back_latter = ""
    pair_found = []
    last_pair = ""
    repeat_letter = False
    repeat_pair = False
    for letter in line:
        if two_back_latter == letter:
            repeat_letter = True
        if last_letter + letter in pair_found:
            repeat_pair = True
        pair_found.append(last_pair)
        last_pair = last_letter + letter
        two_back_latter = last_letter
        last_letter = letter
    if repeat_pair and repeat_letter:
        print(f'{line} is nice')
    else:
        print(f'{line} is naughty')
"""