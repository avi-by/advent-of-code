"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""
import numpy as np

wires = {}

def l_check(command,wires,flag):
    l= None
    if command[0].isnumeric():
        l = np.int16(command[0])
    elif command[0] in wires:
        l = wires[command[0]]
    else:
        flag = True
    return (l,flag)

def r_and_l_check(command,wires,flag):
    l =None
    r =None
    if command[0].isnumeric():
        l = np.int16(command[0])
    elif command[0] in wires:
        l = wires[command[0]]
    else:
        flag = True
    if command[2].isnumeric():
        r = np.int16(command[0])
    elif command[2] in wires:
        r = wires[command[2]]
    else:
        flag = True
    return (l,r,flag)



with open('input.txt') as input:
    lines =input.readlines()
    flag =True
    while flag:
        flag=False
        for line in lines:
            command = line.split('->')
            wire = command[1].strip()
            command = command[0].split()
            num=None
            if len(command) == 1:
                if command[0].isnumeric():
                    num = np.int16(command[0])
                elif command[0] in wires:
                    num = wires[command[0]]
                else:
                    flag=True
            elif command[0] == "NOT":
                if command[1].isnumeric():
                    num = ~np.int16(command[1])
                elif command[1] in wires:
                    num = ~wires[command[1]]
                else:
                    flag=True
            elif command[1] == "OR":
                l, r, flag = r_and_l_check(command,wires,flag)
                if r is not None and l is not None:
                    num = l | r
            elif command[1] == "AND":
                l, r, flag = r_and_l_check(command,wires,flag)
                if r is not None and l is not None:
                    num = l & r
            elif command[1] =="RSHIFT":
                l, flag = l_check(command,wires,flag)
                if l is not None:
                    num = l >> np.int16(command[2])
            elif command[1] == "LSHIFT":
                l, flag = l_check(command,wires,flag)
                if l is not None:
                    num = l << np.int16(command[2])
            if num is not None and num < 0:
                num += 2 ** 16
            if num is not None:
                wires[wire] = num
with open('output part 1.txt','w') as output:
    output.write(f'the answer is: {wires["a"]}')

"""
--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""

wires={'b':wires['a']}

with open('input.txt') as input:
    lines =input.readlines()
    flag =True
    while flag:
        flag=False
        for line in lines:
            command = line.split('->')
            wire = command[1].strip()
            command = command[0].split()
            num=None
            if len(command) == 1:
                if command[0].isnumeric():
                    num = np.int16(command[0])
                elif command[0] in wires:
                    num = wires[command[0]]
                else:
                    flag=True
            elif command[0] == "NOT":
                if command[1].isnumeric():
                    num = ~np.int16(command[1])
                elif command[1] in wires:
                    num = ~wires[command[1]]
                else:
                    flag=True
            elif command[1] == "OR":
                l, r, flag = r_and_l_check(command,wires,flag)
                if r is not None and l is not None:
                    num = l | r
            elif command[1] == "AND":
                l, r, flag = r_and_l_check(command,wires,flag)
                if r is not None and l is not None:
                    num = l & r
            elif command[1] =="RSHIFT":
                l, flag = l_check(command,wires,flag)
                if l is not None:
                    num = l >> np.int16(command[2])
            elif command[1] == "LSHIFT":
                l, flag = l_check(command,wires,flag)
                if l is not None:
                    num = l << np.int16(command[2])
            if num is not None and num < 0:
                num += 2 ** 16
            if num is not None and wire != "b":
                wires[wire] = num
with open('output part 2.txt','w') as output:
    output.write(f'the answer is: {wires["a"]}')
