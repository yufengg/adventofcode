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

print(day13p1()) #12min

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

print(day13p2())
