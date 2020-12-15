import utils as ut

def parse1(line):
	return line

def day15p1():
    print('day 15 part 1')
    # lines = ut.get_file('day15_input.txt', parse1)
    # init = [0,3,6]
    init = [1,0,15,2,10,13]
    mem = {}
    for i, v in enumerate(init):
        mem[v] = [i+1] # first turn is 1, not 0

    print(mem)
    prev = init[-1]

    limit = 2020
    # limit = 30000000

    for i in range(len(init)+1, limit+1):

        if i % 1000000 == 0:
            print(i)

        occurrences = mem[prev]
        if len(occurrences) == 1:
            spoken = 0
        else:
            spoken = occurrences[-1] - occurrences[-2]

        mem[spoken] = mem.get(spoken, [])
        mem[spoken].append(i)
        prev = spoken

        # print(prev)
        # break

    return prev #17min

print(day15p1()) # 20min for part 2

def parse2(line):
	return line

def day15p2():
    print('day 15 part 2')
    # lines = ut.get_file('day15_input.txt', parse2)
    lines = ut.get_file('day15_input_small.txt', parse2)
    return

print(day15p2())
