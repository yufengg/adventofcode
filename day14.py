import utils as ut

def parse1(line):
    add, num = line.split(' = ')
    return add, num

def get_and_or(num):
    or_str = ''
    and_str = ''
    for v in num:
        if v == 'X':
            or_str += '0'
            and_str += '1'
        else:
            or_str += v
            and_str += v
    return int(or_str, 2), int(and_str,2)

def day14p1():
    print('day 14 part 1')
    lines = ut.get_file('day14_input.txt', parse1)
    # lines = ut.get_file('day14_input_small.txt', parse1)

    current_mask = ''
    and_mask = ''
    or_mask = ''
    mem = {}
    count = 0
    for add, num in lines:
        if add == 'mask':
            or_mask, and_mask = get_and_or(num)
            # print(or_str, and_str)
        else:
            reg = int(add[4:-1])
            converted = (int(num) | or_mask) & and_mask
            mem[reg] = converted

        # if count == 4:
        #     pass
        #     # break
        # count+=1

        # print(mem)
    return sum(mem.values()) # 28min

print(day14p1())

def parse2(line):
	return line

def decoder(num):
    or_str = ''
    and_str = ''
    X_pos = []
    for i, v in enumerate(num):
        if v == 'X':
            or_str += '0'
            X_pos.append(35-i)
            and_str += '0'
        # elif v == '0':
        #     and_str += v
        else:
            or_str += v
            and_str += '1'


    return int(or_str, 2), int(and_str,2), X_pos

# mem is {}
# reg is base/starting register address value
# X_pos are 2^__ branching additions
# num is value to write to mem[reg+offset] = num
def write_values(mem, reg, X_pos, num):
    # print(len(X_pos))
    if len(X_pos) == 1:
        mem[reg + 2**X_pos[0]] = num
        mem[reg] = num
        return

    write_values(mem, reg, X_pos[1:], num)
    write_values(mem, reg+2**X_pos[0], X_pos[1:], num)


def day14p2():
    print('day 14 part 2')
    lines = ut.get_file('day14_input.txt', parse1)
    # lines = ut.get_file('day14_input_small.txt', parse1)

    current_mask = ''
    and_mask = ''
    or_mask = ''
    mem = {}
    count = 0
    for add, num in lines:
        if add == 'mask':
            or_mask, and_mask, X_pos = decoder(num)
            print(or_mask, and_mask, X_pos)
        else:
            num = int(num)
            reg = int(add[4:-1])
            reg = (reg | or_mask) & and_mask
            write_values(mem, reg, X_pos, num)
            # mem[reg] = num # (with combos)

        # print(mem)
    return sum(mem.values())  # 28min

print(day14p2()) # 1hr 08min
