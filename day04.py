import utils as ut

#ecl:hzl byr:1965 hcl:#a97842 iyr:2011 pid:506354451 hgt:172cm eyr:2029
def parse1(line):
    fields = line.split()
    field_dict = dict([f.split(':') for f in fields])
    # print(field_dict)
    return field_dict

def day04p1():
    print('day 04 part 1')
    valid = 0
    passport = {}
    lines = ut.get_file('day04_input.txt', parse1)
    for l in lines:
        if l:
            passport.update(l)
            # make sure all 8 fields are present (but cid is optional)

        else:
            field_count = len(passport.keys())
            if passport.get('cid'):
                field_count -= 1
            if field_count == 7:
                # print('valid:', passport)
                valid += 1
            passport.clear()

    return valid

print(day04p1())

# debug print
def dpr(s):
    # print(s)
    return


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
def valid_rules(d):
    if not (1920 <= int(d['byr']) <= 2002):
        dpr(f'byr on {d}')
        return False

    if not (2010 <= int(d['iyr']) <= 2020):
        dpr(f'iyr on {d}')
        return False

    if not (2020 <= int(d['eyr']) <= 2030):
        dpr(f'eyr on {d}')
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if not (d['hgt'].endswith(('cm','in')) and d['hgt'][:-2].isnumeric()):
        dpr(f'hgt on {d}')
        return False

    if d['hgt'].endswith('cm'):
        if not (150 <= int(d['hgt'][:-2]) <= 193):
            dpr(f'hgt cm on {d}')
            return False

    if d['hgt'].endswith('in'):
        if not (59 <= int(d['hgt'][:-2]) <= 76):
            dpr(f'hgt in on {d}')
            return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = d['hcl']
    if hcl[0] != '#':
        dpr(f'hcl on {d}')
        return False
    if len(hcl[1:]) != 6:
        dpr(f'hcl on {d}')
        return False
    for c in hcl[1:]:
        if c.isnumeric():
            continue
        if not (c.isalpha() and 'a' <= c <= 'f'):
            dpr(f'hcl on {d}')
            return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if d['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        dpr(f'ecl on {d}')
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not (len(d['pid']) == 9 and d['pid'].isnumeric()):
        dpr(f'pid on {d}')
        return False

    return True

def day04p2():
    print('day 04 part 2')
    valid = 0
    passport = {}
    lines = ut.get_file('day04_input.txt', parse1)
    for l in lines:
        if l:
            passport.update(l)
            # make sure all 8 fields are present (but cid is optional)

        else:
            field_count = len(passport.keys())
            if passport.get('cid'):
                field_count -= 1
            if field_count == 7:
                if valid_rules(passport):
                    # print('valid:', passport)
                    valid += 1
            passport.clear()

    return valid


print(day04p2())
