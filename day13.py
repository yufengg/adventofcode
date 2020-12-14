import utils as ut

def parse1(line):
	return line

def day13p1():
    print('day 13 part 1')
    lines = ut.get_file('day13_input.txt', parse1)
    # lines = ut.get_file('day13_input_small.txt', parse1)

    start_time = int(lines[0])
    schedule = list(map(int, ''.join(lines[1].split('x,')).split(',')))
    departs_in = float('inf')
    bus_id = -1
    for time in schedule:
        new_departs_in = time - start_time % time
        if new_departs_in < departs_in:
            departs_in = new_departs_in
            bus_id = time

    print(departs_in, bus_id)
    return  departs_in * bus_id

# print(day13p1()) #12min

def parse2(line):
	return line

def day13p2():
    print('day 13 part 2')
    lines = ut.get_file('day13_input.txt', parse2)
    # lines = ut.get_file('day13_input_small.txt', parse2)

    offset = 0
    schedule = []
    for val in lines[1].split(','):
        # if val == 'x':
        #     offset += 1
        if val.isnumeric():
            bus_id = int(val)
            schedule.append((bus_id, offset))
        offset+=1
    print(schedule)

    max_sync = 1
    for bus_id, offset in schedule:
        max_sync *= bus_id

    def validate(t, schedule):
        for bus_id, offset in schedule:
            if not ((t+offset) % bus_id == 0):
                return False
        return True

    first_bus = 467 # int(lines[1].split(',')[0])
    t = 100000000000171 # max_sync
    counter = 0
    while True:
    # while t > 0:
        counter += 1
        if counter % 10000000 == 0:
            print(counter, t)
        if validate(t-29, schedule):
            return t
        # t -= first_bus
        t += first_bus

    return schedule

# print(day13p2())

def day13p2v2():
    print('day 13 part 2v2')
    lines = ut.get_file('day13_input.txt', parse2)
    # lines = ut.get_file('day13_input_small.txt', parse2)

    offset = 0
    schedule = []
    for val in lines[1].split(','):
        if val.isnumeric():
            bus_id = int(val)
            schedule.append((bus_id, offset))
        offset += 1
    print(schedule)

    all_buses = [bus_id for bus_id, offset in schedule]

    # find a match with the the first n buses
    # use that match to update the search_offset (=0)
    # update the range operators
    range_top = 1
    range_step = 1
    # prev_bus_id = 1
    search_offset = 0
    for i, (bus_id, offset) in enumerate(schedule):
        range_top *= bus_id
        found = check_match(range_top, range_step, search_offset, schedule[:i+1])
        if found:
            search_offset = found
        print('found', search_offset)
        range_step *= bus_id

    return  search_offset

def check_match(range_top, range_step, search_offset, schedule):
    print('every', range_step, 'offset', search_offset, 'sched', schedule)
    for i in range(0, range_top, range_step):
        if i == 0:
            continue
        t = i + search_offset
        match = [False] * len(schedule)

        bus_id, offset = schedule[-1]
        if (t + offset) % bus_id == 0:
            return t # short version
        # for j, (bus_id, offset) in enumerate(schedule):
        #     if (t + offset) % bus_id == 0:
        #         print('one', t)
        #         match[j] = True
        # if all(match):
        #     return i # return new offset
    return False

print(day13p2v2()) # 3hr 46min
