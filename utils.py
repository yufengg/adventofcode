def default_parsing_fn(line):
    return line

def get_file(filename, parsing_fn):
    lines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            lines.append(parsing_fn(line))
    return lines

# import utils as ut
# ut.generate_template(9)
def generate_template(day):
    day = format(day, '02d') # left-pad a zero

    imports = 'import utils as ut\n'

    parse1 = 'def parse1(line):\n\treturn line\n'

    # part1 = "def day4p1():\n\tprint('part 1')\n\tut.get_file('day4_input.txt', parse1)\n\treturn\n"
    part1 = \
f"""def day{day}p1():
    print('day {day} part 1')
    # lines = ut.get_file('day{day}_input.txt', parse1)
    lines = ut.get_file('day{day}_input_small.txt', parse1)
    return

print(day{day}p1())
"""
    parse2 = 'def parse2(line):\n\treturn line\n'

    part2 = \
f"""def day{day}p2():
    print('day {day} part 2')
    # lines = ut.get_file('day{day}_input.txt', parse2)
    lines = ut.get_file('day{day}_input_small.txt', parse2)
    return

print(day{day}p2())
"""
    file_contents = '\n'.join([imports, parse1, part1, parse2, part2])
    with open(f'day{day}.py', 'w') as f:
        f.write(file_contents)

    with open(f'day{day}_input.txt', 'w') as f:
        f.write('')

    with open(f'day{day}_input_small.txt', 'w') as f:
        f.write('')
