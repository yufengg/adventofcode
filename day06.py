import utils as ut

def parse1(line):
	return line

def day06p1():
    print('day 06 part 1')
    # lines = ut.get_file('day06_input.txt', parse1)
    lines = []
    with open('day06_input.txt') as f:
        groups = f.read().split('\n\n')

    total = 0
    for g in groups:
        persons = g.split('\n')
        group_set = set()
        for p in persons:
            for char in p:
                group_set.add(char)
        total += len(group_set)

    return total # 6:13


print(day06p1())

def parse2(line):
	return line

def day06p2():
    print('day 06 part 2')
    # lines = ut.get_file('day06_input.txt', parse1)
    lines = []
    with open('day06_input.txt') as f:
        groups = f.read().split('\n\n')

    total = 0
    for g in groups:
        persons = g.split('\n')
        group_set = set('qwertyuiopasdfghjklzxcvbnm')
        for p in persons:
            # for char in p:
            group_set = group_set.intersection(set(p))
        total += len(group_set)

    return total  # 8:59

print(day06p2())
