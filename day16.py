import utils as ut

def process_rules(line):
    rules = {}
    lines = line.split('\n')
    for l in lines:
        rule_name, num_ranges = l.split(': ')
        first, second = num_ranges.split(' or ')
        first_start, first_end = map(int, first.split('-'))
        second_start, second_end = map(int, second.split('-'))
        assert type(second_end) == int
        # print(rule_name, f'{first_start}-{first_end} or {second_start}-{second_end}')
        rules[rule_name] = [first_start, first_end, second_start, second_end]
    return rules

def process_tix(s):
    tickets = s.split('\n')[1:]
    ticket_list = []
    for t in tickets:
        ticket_values = list(map(int, t.split(',')))
        # print(ticket_values)
        ticket_list.append(ticket_values)
    return ticket_list

def check_valid_ticket(tickets, rules):
    invalid_total = 0
    print('rules', rules)
    for ticket in tickets:
        # print('scanning ticket:', ticket)
        for num in ticket:
            all_rules = dict(zip(rules.keys(), len(rules) * [False]))
            # print(all_rules)
            for name, (a1,a2,b1,b2) in rules.items():
                if (a1 <= num <= a2 or b1 <= num <= b2):
                    all_rules[name] = True
                    # print(num)
                    # invalid_total += num
            if not any(all_rules.values()):
                invalid_total += num
                # print('invalid:', num)

    return invalid_total

def day16p1():
    print('day 16 part 1')
    filename = 'day16_input.txt'
    # filename = 'day16_input_small.txt'

    with open(filename) as f:
        [rules, my_tix, nearby_tix] = f.read().split('\n\n')

    rules = process_rules(rules)
    nearby_tix = process_tix(nearby_tix)

    invalid_total = check_valid_ticket(nearby_tix, rules)

    return invalid_total #rules, my_tix, nearby_tix

print(day16p1()) # 30min

def get_valid_tickets(tickets, rules):
    invalid_total = 0
    print('rules', rules)
    valid_tickets = []
    for ticket in tickets:
        # print('scanning ticket:', ticket)

        for num in ticket:
            all_rules = dict(zip(rules.keys(), len(rules) * [False]))
            # print(all_rules)
            for name, (a1,a2,b1,b2) in rules.items():
                if (a1 <= num <= a2 or b1 <= num <= b2):
                    all_rules[name] = True
                    # print(num)
                    # invalid_total += num
            if not any(all_rules.values()):
                # print('invalid:', num, 'in', ticket)
                break
        else:
            valid_tickets.append(ticket)

    return valid_tickets

"""
for each column (field), find the set(rulenames) that it's valid for.
Find interection() of all values in that column.

Repeat until all sets are == 1:
Find which len(set(s)) ==1 , lock those in.
Then remove() the names of locked rules from all sets.
"""

def sequence_rules(tix, rules):
    rule_sets = []
    for j in range(len(tix[0])):
        all_rules = set(rules.keys())
        for i in range(len(tix)):
            rules_met = set()
            num = tix[i][j]
            for name, (a1,a2,b1,b2) in rules.items():
                if (a1 <= num <= a2 or b1 <= num <= b2):
                    rules_met.add(name)

            # print('num',num, 'matches', rules_met)

            all_rules = all_rules.intersection(rules_met)
            # print(all_rules)

        rule_sets.append(all_rules)

    final_rules = len(tix[0]) * [0]
    rule_sets = eliminate_rules(final_rules, rule_sets)
    print(rule_sets)

    return rule_sets


def eliminate_rules(final_rules, rule_sets):
    # find which are len==1, remove from others
    all_empty = True
    for i, rule_s in enumerate(rule_sets):
        if len(rule_s) == 1:
            found_rule = rule_s.pop()
            final_rules[i] = found_rule
            for r in rule_sets:
                r.discard(found_rule)
        if len(rule_s) > 0:
            all_empty = False
    if not all_empty:
        eliminate_rules(final_rules, rule_sets)

    return final_rules

def find_departure_vals(field_positions, my_tix):
    title, my_tix = my_tix.split('\n')
    my_tix = list(map(int, my_tix.split(',')))
    solution = 1
    for i, field in enumerate(field_positions):
        if field.startswith('departure'):
            solution *= my_tix[i]
    return solution

def day16p2():
    print('day 16 part 2')
    filename = 'day16_input.txt'
    # filename = 'day16_input_small.txt'

    with open(filename) as f:
        [rules, my_tix, nearby_tix] = f.read().split('\n\n')

    rules = process_rules(rules)
    nearby_tix = process_tix(nearby_tix)

    valid_tickets = get_valid_tickets(nearby_tix, rules)

    field_positions = sequence_rules(valid_tickets, rules)

    output = find_departure_vals(field_positions, my_tix)

    return output  # rules, my_tix, nearby_tix

print(day16p2()) #1hr 13min
