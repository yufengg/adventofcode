print('part 1')

def get_ints(filename='day1_input.txt'):
    ints = []
    with open(filename) as f:
        for line in f:
            ints.append(int(line))
    return ints

def sum_2(ints, total):
    for i in range(len(ints)):
        value = ints[i]
        # print('checking', value)
        if (total - value) in ints[i:]:
            print(value , (total - value))
            return value * (total - value)

def day1p1():
    ints = get_ints('day1_input.txt')
    return sum_2(ints, 2020)

print(day1p1())

print('part 2')

def day1p2(total=2020):
    ints = get_ints()
    for i in range(len(ints)):
        value = ints[i]
        res = sum_2(ints[i:], total - value)
        if res:
            print(value)
            return value * res


print(day1p2(2020))

