import utils as ut

def parse1(line):
	return line

def day05p1():
    print('day 05 part 1')
    lines = ut.get_file('day05_input.txt', parse1)
    max_seat_id = 0
    for line in lines:
        # s = ''
        # for letter in line[:-3]:
        #     if letter == 'F': s += '0'
        #     if letter == 'B': s += '1'
        # row_num = int(s, 2)
        #
        # s = ''
        # for letter in line[-3:]:
        #     if letter == 'L': s += '0'
        #     if letter == 'R': s += '1'
        # col_num = int(s, 2)
        #
        # max_seat_id = max(max_seat_id, row_num * 8 + col_num)

        mapping = {
            'F': '0',
            'B': '1',
            'L': '0',
            'R': '1'
        }
        for k,v in mapping.items():
            line = line.replace(k,v)

        max_seat_id = max(max_seat_id, int(line, 2))
    return max_seat_id

print(day05p1()) # 7:35

def parse2(line):
	return line

def day05p2():
    print('day 05 part 2')
    lines = ut.get_file('day05_input.txt', parse2)
    max_seat_id = 0
    seat_id_list = []
    for line in lines:
        s = ''
        for letter in line[:-3]:
            if letter == 'F': s += '0'
            if letter == 'B': s += '1'
        row_num = int(s, 2)
        s = ''
        for letter in line[-3:]:
            if letter == 'L': s += '0'
            if letter == 'R': s += '1'
        col_num = int(s, 2)
        seat_id = row_num * 8 + col_num
        seat_id_list.append(seat_id)
        # max_seat_id = max(max_seat_id, row_num * 8 + col_num)
    seat_id_list.sort()

    seat_id = seat_id_list[0]
    for val in seat_id_list:
        if val == seat_id:
            seat_id += 1
        else:
            print(val)
            seat_id = val+1


    return seat_id_list

print(day05p2()) # 12:34 cumulative
