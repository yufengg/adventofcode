import utils as ut

def parse1(line):
    ins, val = line.split()
    val = int(val)
    return ins, val

def day08p1():
    print('day 08 part 1')
    lines = ut.get_file('day08_input.txt', parse1)
    visited = set() # index of instructions visited

    total = 0
    index = 0
    while index not in visited:
        ins, val = lines[index]
        visited.add(index)
        if ins == 'nop':
            index += 1
        if ins == 'acc':
            total += val
            index += 1
        if ins == 'jmp':
            index += val
    return total


print(day08p1()) # 8:26

def parse2(line):
	return line

# ret True if successful termination, otherwise False
def validate_program(lines):
    visited = set()  # index of instructions visited
    total = 0
    index = 0
    while index not in visited:
        if index > len(lines):
            return False, total

        if index == len(lines):
            return True, total

        ins, val = lines[index]
        visited.add(index)
        if ins == 'nop':
            index += 1
        if ins == 'acc':
            total += val
            index += 1
        if ins == 'jmp':
            index += val

    return False, total

def day08p2():
    print('day 08 part 2')
    # index == len(lines)
    lines = ut.get_file('day08_input.txt', parse1)

    # modify lines to try different nop/jmp swaps
    for i, (ins, val) in enumerate(lines):
        # print(i, ins, val)
        new_input = lines + []
        if ins == 'jmp':
            new_input[i] = ('nop', val)
        if ins == 'nop':
            new_input[i] = ('jmp', val)
        valid, total = validate_program(new_input)
        if valid:
            return total

    return 'WHATTT'

print(day08p2()) #21min
