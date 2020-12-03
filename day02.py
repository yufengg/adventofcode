print('part 1')

def find_all(a, s):
    count = 0
    for l in s:
        if a == l:
            count += 1
    return count

def day2(filename='day2_input.txt'):
    valid = 0
    with open(filename) as f:
        for line in f:
            rule, passw = line.split(': ')
            passw = passw.strip()
            count, letter = rule.split()
            lower, upper = count.split('-')
            upper = int(upper)
            lower = int(lower)

            # print(line, upper, lower, find_all(letter, passw))

            if lower <= find_all(letter, passw) <= upper:
                # print('valid!')
                valid += 1
    return valid

print(day2('day2_input_short.txt'))
print(day2('day2_input.txt'))

print('part 2')

def parse_file(filename='day2_input.txt'):
    rules = []
    with open(filename) as f:
        for line in f:
            rule, passw = line.split(': ')
            passw = passw.strip()
            count, letter = rule.split()
            lower, upper = count.split('-')
            upper = int(upper)
            lower = int(lower)

            # print(line, upper, lower, find_all(letter, passw))
            rules.append((lower, upper, letter, passw))
    return rules

def day2p2():
    rules = parse_file()
    valid = 0
    for r in rules:
        first, second, letter, passw = r
        if passw[first-1] == letter or passw[second-1] == letter:
            if passw[first-1] == letter and passw[second-1] == letter:
                continue
            else:
                valid += 1

    return valid

print(day2p2())