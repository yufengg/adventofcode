import utils as ut
from collections import Counter

def add_tuples(a,b):
    return (a[0] + b[0], a[1] + b[1])
def pr(args):
    # if len(args) > 0 and not (isinstance(args, str)):
    #     " ".join(args)
    # else:
    print(args)
    return

class SeatMap():

    directions1 = ('up', 'down')
    directions2 = ('left', 'right')
    directions = set()
    for d1 in directions1:
        directions.add((d1,))
        for d2 in directions2:
            directions.add((d2,))
            directions.add((d1, d2))
    print(directions)

    direction_mod_map = {
        'up': (-1, 0),
        'down': (+1, 0),
        'left': (0, -1),
        'right': (0, +1)
    }

    direction_coordinates = {}

    for direction_pair in directions:
        for d in direction_pair:
            direction_coordinates[direction_pair] = \
                add_tuples(direction_coordinates.get(direction_pair, (0,0)) , direction_mod_map[d])
    print(direction_coordinates)

    def __init__(self, lines, part = 2):
        self.seats = lines
        self.part = part

    def next_state(self, r, c):
        if self.part == 1:
            return self.next_state_part1(r,c)
        else:
            return self.next_state_part2(r,c)

    # return the counts of L and #
    def look(self, r, c, x, y):
        # pr(['looking',r,c,x,y])
        seen = None
        row, col = r + x, c + y
        while not seen:
            if not (0 <= row < len(self.seats)):
                return '.'
            if not (0 <= col < len(self.seats[0])):
                return '.'
            looking = self.seats[row][col]
            if looking == '.':
                # update coordinates
                row += x
                col += y
                continue
            else:
                seen = True
                return looking # L or #

    def next_state_part2(self,r,c):
        curr = self.seats[r][c]
        if curr == '.':
            return '.'
        # get counts of # and L in line of sights
        empty = 0 # empty is L
        occ = 0 # occ is a #
        for direction_pair in SeatMap.directions:  # ('down', 'right'),
            x,y = SeatMap.direction_coordinates[direction_pair]
            seen = self.look(r,c, x,y)
            if seen == 'L': empty +=1
            if seen == '#': occ +=1

        if curr == '#':
            if occ >= 5:
                return 'L'
            else:
                return '#'
        if curr == 'L':
            if occ == 0:
                return '#'
            else:
                return 'L'




    def next_state_part1(self,r,c):
        region = [-1,0,1]
        curr = self.seats[r][c]
        if curr == '.':
            return '.'
        if curr == 'L': # empty
            for x in region:
                if not (0 <= (r+x) < len(self.seats)):
                    continue
                for y in region:
                    if not (0 <= (c + y) < len(self.seats[0])):
                        continue
                    if x == 0 and y == 0:
                        continue
                    # print('r+x, c+y', r+x, c+y)
                    if self.seats[r+x][c+y] == '#':
                        return 'L'
            return '#'

        if curr == '#': # occ
            occ = 0
            for x in region:
                if not (0 <= (r+x) < len(self.seats)):
                    continue
                for y in region:
                    if not (0 <= (c + y) < len(self.seats[0])):
                        continue
                    if x == 0 and y == 0:
                        continue
                    # print('checking', r+x, c+y, 'value', self.seats[r+x][c+y])
                    if self.seats[r+x][c+y] == '#':
                        occ += 1
                        if occ >= 4:
                            # print('returning L')
                            return 'L'
            return '#'

    def cycle(self, n=1):

        next_seatmap = []
        # make copy of orig and mod in place?
        for x in range(len(self.seats)):
            next_row = []
            for y in range(len(self.seats[0])):
                # print('x,y', x,y)
                next_row.append(self.next_state(x,y))
            next_seatmap.append(next_row)

        self.seats = next_seatmap
        return self

    def get_num_seats(self):
        seat_count = 0
        for row in self.seats:
            for seat in row:
                if seat == '#':
                    seat_count += 1
        return seat_count

    def __repr__(self):
        return '\n'.join([''.join(rows) for rows in self.seats])



def parse1(line):
    row = []
    for char in line:
        row.append(char)
    return row

def day11p1():
    print('day 11 part 1')
    lines = ut.get_file('day11_input.txt', parse1)
    smap = SeatMap(lines, 1)
    prev_seats = smap.get_num_seats()

    while True:
    # for i in range(6):
        smap.cycle()
        # print(smap)
        seats = smap.get_num_seats()
        print(seats)
        if seats == prev_seats:
            return seats
        prev_seats = seats

    # print(smap)

    # for i in range(0,3):
    #     for j in range(0,3):
    #         print(f'{i,j}:', smap.next_state(i, j))
    # return smap.get_num_seats()

# print(day11p1())

def parse2(line):
	return line

def day11p2():
    print('day 11 part 2')
    lines = ut.get_file('day11_input.txt', parse1)
    smap = SeatMap(lines, 2)
    prev_seats = smap.get_num_seats()

    while True:
        # for i in range(6):
        smap.cycle()
        # print(smap)
        seats = smap.get_num_seats()
        print(seats)
        if seats == prev_seats:
            return seats
        prev_seats = seats

print(day11p2())
