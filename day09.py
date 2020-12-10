import utils as ut

def parse1(line):
	return int(line)

def sum_2(ints, total):
    print(ints)
    for i in range(len(ints)):
        value = ints[i]
        # print('checking', value)
        if (total - value) in ints[i+1:]:
            # print(value , (total - value))
            # return value * (total - value)
            return True
    return False

def day09p1():
    print('day 09 part 1')
    lb = 25 # lookback
    num_list = ut.get_file('day09_input.txt', parse1)
    for i in range(lb, len(num_list)): # start at line 26, aka index 25
        prev = num_list[i-25:i]
        if not (len(prev) == lb):
            return 'BAD PREV LENGTH'
        n = num_list[i]
        print('checking', n)
        if not sum_2(prev, n):
            print(i)
            return n
    print('end is', end)
    return 'WHATTT'

# print(day09p1()) # 25min

def parse2(line):
	return line

def min_max(ls):
    return min(ls), max(ls)

# 32321523
def day09p2():
    print('day 09 part 2')
    lines = ut.get_file('day09_input.txt', parse1)
    find = 32321523
    # for each num
    for i in range(len(lines)):
        # add up all numbers that follow
        temp_total = 0
        for j in range(i, len(lines[i:])):
            temp_total += lines[j]
            # break when the sum > desired_value
            if temp_total > find:
                break
            # if equal, found
            if temp_total == find:
                print(i, j)
                print(lines[i] , lines[j])
                small, big = min_max(lines[i:j+1])
                return small+big

    return 'WHAT'

print(day09p2()) #39min
