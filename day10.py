import utils as ut

def parse1(line):
	return int(line)

def day10p1():
    print('day 10 part 1')
    adapters = ut.get_file('day10_input.txt', parse1)
    adapters.sort()
    print(adapters)

    diff_1 = 0
    diff_3 = 1
    prev = 0 # plug source
    for i in range(len(adapters)):
        diff = adapters[i] - prev
        prev = adapters[i]
        if diff == 1:
            diff_1 += 1
        if diff == 3:
            diff_3 += 1

    return diff_1 * diff_3


# print(day10p1()) # 9:25

def parse2(line):
	return line

class AdapterSeq():
    def __init__(self):
        self.__adapters = [0]

    def append(self, a):
        prev = self.__adapters[-1]
        if 1 <= a - prev <= 3:
            self.__adapters.append(a)
            return True
        else:
            print('invalid append:', a, 'current last val:', self.__adapters[-1])
            return False
        return

    def get_adapters(self):
        return self.__adapters

    def end_seq(self):
        self.append(self.__adapters[-1]+3) # source
        return self.__adapters
    def copy(self):
        new_a = AdapterSeq()
        new_a._AdapterSeq__adapters = self.__adapters + []
        return new_a

# This is the working solution for part 2
total_calls = 0
def count_adapters(adapters, pos, lookup):
    if pos in lookup:
        return lookup[pos]

    global total_calls
    total_calls+=1
    if total_calls % 1000000 == 0:
        print('total calls:', total_calls)

    if (len(adapters)-1) == pos: # last spot
        lookup[pos] = 1
        return 1
    # go through each of the potential 3 values
    # accumulate their total combos
    combos = 0
    base = adapters[pos]
    for i in range(pos+1,pos+4):
        if i >= len(adapters):
            continue
        val = adapters[i]
        if 1 <= val-base <= 3:
            # print(i, val)
            combos += lookup.get(i, count_adapters(adapters, i, lookup))
    lookup[pos] = combos
    # print('return pos', pos, 'is', total)

    return combos

def day10p2_rec():
    print('day 10 part 2 recursive')
    adapters = [0] + ut.get_file('day10_input.txt', parse1)
    adapters.sort()
    adapters.append(max(adapters) + 3)
    adapters = tuple(adapters)
    print(adapters)
    return count_adapters(adapters, 0, {})


print('part 2 rec:', day10p2_rec())
print(total_calls)


# ignore below. Messed it up...
from collections import deque

def day10p2():
    print('day 10 part 2')
    adapters = ut.get_file('day10_input_small.txt', parse1)
    adapters.sort()
    adapters.append(max(adapters)+3)
    # adapters = adapters[:20]
    print(adapters)
    # return count_adapters(adapters)

    stack = deque()
    initial = ([0], adapters)
    stack.append(initial)
    total = 0
    combos = set()
    while len(stack):
        current, adapters = stack.pop()
        if adapters and current[-1] > adapters[0]:
            print('overlap! at total', total)
            print('curr', current)
            print('\tadap', adapters)
            return 'WHAT'
        if total % 1000000 == 0:
            print(total)
            print('curr', current)
            print('\tadap', adapters)

        # print('curr', current)
        # print('\tadap', adapters)

        if len(adapters) == 1:
            new_current = current + []
            new_current.append(adapters[0])
            # print(new_current)
            combos.add(tuple(new_current))
            total += 1
            continue

        end = min(3, len(adapters))
        base = current[-1] # adapters[0]
        for i in range(0, end): # 1 - (3 at most)
            val = adapters[i]
            if 1 <= (val - base) <= 3:
                # copy a new 'current'
                new_current = current+[]
                new_current.append(val)
                new_adapters = adapters[i+1:] + []
                stack.append((new_current, new_adapters))

    return total, len(combos)

# print('part 2:', day10p2())

# ignore below. Tried to do it with powers of 2. Not correct.
from math import pow
import math
def day10p2v2():
    print('day 10 part 2v2')
    adapters = [0] + ut.get_file('day10_input_small.txt', parse1)
    adapters.sort()
    adapters.append(max(adapters)+3)
    # adapters = adapters[:20]
    print(adapters)

    # prev = 0 # plug source
    offset = [1, 2, 3]
    branches = []
    for i in range(len(adapters)-1): # no diffs for the final value
        count = 0
        base = adapters[i]
        for o in offset:
            if i+o >= len(adapters):
                continue
            if 1 <= adapters[i+o] - base <= 3:
                count += 1
        branches.append(count)

    print(branches)

    combos = []
    for i in range(len(adapters)-1): # no diffs for the final value
        # print(adapters[i], branches[i])
        pass

    return

# print('part 2 v2:', day10p2v2())
