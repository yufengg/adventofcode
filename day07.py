import utils as ut

def join(seq, char=" "):
    return char.join(seq)

# wavy tomato bags contain 4 bright orange bags, 4 shiny fuchsia bags, 1 bright gray bag, 1 posh violet bag.
# light red bags contain 1 2 muted yellow bagbright white bag, s.
def parse1(line):
    line = line.split(',')
    output = [join(line[0].split()[:2])]
    # print(output)
    for elem in line:
        output.append(join(elem.split()[-3:-1]))
    return output

def lookup_bag(bag, rmap, outer_set):
    if bag not in rmap:
        print(bag, 'not in map')
        return 0
    total = len(rmap[bag])
    print(bag, 'contained by', total, 'outer bags')
    for color in rmap[bag]:
        outer_set.add(color)
        total += lookup_bag(color, rmap, outer_set)

    print('return', total, 'outerbags')
    return total

def day07p1():
    print('day 07 part 1')
    color_rules = ut.get_file('day07_input.txt', parse1)
    print(color_rules)

    rule_map = {}
    for rule in color_rules:
        outer = rule[0]
        inner = rule[1:]
        for inner_bag in inner:
            rule_map[inner_bag] = rule_map.get(inner_bag, [])
            rule_map[inner_bag].append(outer)
    print(rule_map)

    outer_set = set()
    lookup_bag('shiny gold', rule_map, outer_set)
    print(outer_set)
    return len(outer_set) #31min

print(day07p1())

# wavy tomato bags contain 4 bright orange bags, 4 shiny fuchsia bags, 1 bright gray bag, 1 posh violet bag.
def parse2(line):
    line = line.split(',')
    output = [join(line[0].split()[:2])]
    # print(output)
    for elem in line:
        inner_name = join(elem.split()[-3:-1])
        if inner_name == 'no other':
            inner_count = 0
        else:
            inner_count = int(elem.split()[-4])
        output.append((inner_name, inner_count))
    return output

def count_bags(color, rmap):
    inside_bags = rmap.get(color, [])
    print('outer:', color)
    total = 0
    for (col, ct) in inside_bags:
        print(color, 'contains', ct, col, 'bags')
        total += ct
        total += ct * count_bags(col, rmap)
    print('total returning', total)
    return total

def day07p2():
    print('day 07 part 2')
    color_rules = ut.get_file('day07_input.txt', parse2)
    print(color_rules)

    rule_map = {} # outer: [(inner, ct)] #
    for rule in color_rules:
        outer = rule[0]
        inner = rule[1:]
        for inner_bag in inner:
            rule_map[outer] = rule_map.get(outer, [])
            if inner_bag[0] == 'no other':
                continue
            rule_map[outer].append(inner_bag)
    print(rule_map)

    return count_bags('shiny gold', rule_map)

print(day07p2()) # 52min
