import utils as ut

def parse_rule(s):
    s = s.strip()

    if s[0] == '"':
        return s[1]

    rule_list = s.split(' | ')
    output = []
    for r in rule_list:
        # print(r)
        nums = list(map(int, r.split(' ')))
        output.append(tuple(nums))
    return output

def parse1(fn):
    with open(fn) as f:
        rules, msgs = f.read().split('\n\n')

    rules_dict = {}
    for rule in rules.split('\n'):
        rule_num, rule_str = rule.split(': ')
        rules_dict[int(rule_num)] = parse_rule(rule_str)

    msgs = [msg for msg in msgs.split('\n')]

    return rules_dict, msgs

tracker = {8:0, 11:0}

class Rule:
    def __init__(self, rules_dict, rule_num):
        global tracker

        self.rule_num = rule_num
        rule = rules_dict[rule_num]
        if isinstance(rule, str) and rule in 'ab':
            self.value = rule
            self.rule = rule
            return

        self.value = []
        self.rule = rule
        for r in rule:
            # this tuple is an option
            rule_set = []
            for rule_lookup in r:
                if rule_lookup in [8,11]:
                    if tracker[rule_lookup] > 20:
                        continue
                    tracker[rule_lookup] += 1
                rule_set.append(Rule(rules_dict, rule_lookup))
            self.value.append(rule_set)

    def eval(self, msgs): # take arg, slice it down, recurse
        responses = [] # (Bool, str)
        for msg in msgs:
            if isinstance(self.value, str):
                if len(msg) == 0:
                    # responses.append((False, '')) # do nothing if false
                    continue
                # print(msg, self.rule_num)
                if len(msg) >= 1:
                    valid = msg[0] == self.value

                if valid:
                    msg = msg[1:]
                    # print('\t', valid,self.rule_num, msg)  # DEBUG
                    responses.append(msg)
                continue

            result = []
            matched_msgs = []
            # print('checking', self.rule_num, ':', self.rule, msg)  # DEBUG
            orig_msg = msg + ''
            for i, rule_set in enumerate(self.value):
                rmsg = [orig_msg + '']
                rule_set_valid = []
                for v in rule_set:
                    # print('rule text:', v.rule, type(v))
                    valid, rmsg = v.eval(rmsg) # result messages[]
                    rule_set_valid.append(valid)
                    if not valid:
                        # DEBUG
                        # print('ruleset wrong:', self.rule[i], orig_msg, '>', msg)
                        break
                if all(rule_set_valid):
                    # DEBUG
                    # print('ruleset correct:', self.rule[i], orig_msg,'>',msg)  # DEBUG
                    matched_msgs +=  rmsg
                    # return True, msg

                result.append(all(rule_set_valid))

            for m in matched_msgs: # flatten multiples
                responses.append(m)

            # if any(result):
            #     # if len(matched_msgs) > 1:
            #     #     print('extra MATCHES!')
            #     # print('matched msgs', matched_msgs) # HOW MANY?
            #     return True, responses
            # else:
            #     return False, orig_msg
        if len(responses):
            return True, responses
        else:
            return False, []

    def __repr__(self):
        # return str(self.rule_num)
        # print(self.rule_num)
        return self.rule
        if isinstance(self.value, str):
            return self.value

        for v in self.value:
            return str(v)

def day19p1():
    print('day 19 part 1')
    filename = 'day19_input.txt'
    # filename = 'day19_input_small.txt'
    rules_dict, msgs = parse1(filename)
    print(rules_dict)
    base = Rule(rules_dict,0)

    # print(base.value)

    # print(base.eval(['abbbbabbbbaaaababbbbbbaaaababb']))
    # babbbbaabbbbbabbbbbbaabaaabaaa
    #           bbbabbbbbbaabaaabaaa
    count = 0
    for m in msgs:
        # print('** checking',m)
        valid, leftover = base.eval([m])
        if valid and one_is_empty(leftover):
            # print(leftover)
            count += 1
            # print(m)

    print(rules_dict, msgs)
    return count

def one_is_empty(l):
    for elem in l:
        if len(elem) == 0:
            return True
    return False

print(day19p1()) #1hr 20min

def parse2(line):
	return line

def day19p2():
    print('day 19 part 2')
    # lines = ut.get_file('day19_input.txt', parse2)
    lines = ut.get_file('day19_input_small.txt', parse2)
    return

print(day19p2()) # 5hrs ffs
