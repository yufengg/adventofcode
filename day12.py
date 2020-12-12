import utils as ut

def parse1(line):
    return (line[0], int(line[1:]))
	# return line

# element-wise: a + b*c
def combine(a,b,c=1):
    return [a[0] + b[0]*c, a[1] + b[1]*c]

def day12p1():
    print('day 12 part 1')
    lines = ut.get_file('day12_input.txt', parse1)
    # lines = ut.get_file('day12_input_small.txt', parse1)
    position = [0, 0]
    orientation = 0
    action_map = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }
    angle_map = {
        'L': 1,
        'R': -1
    }

    angle_direction = {
        0 : 'E',
        90 : 'N',
        180 : 'W',
        270 : 'S'
    }
    for direction, dist in lines:
        print(direction, dist)
        if direction == 'F':
            direction = angle_direction[orientation]
        if direction in action_map:
            change = action_map[direction]
            position = combine(position, change, dist)
        if direction in angle_map:
            orientation = (orientation + angle_map[direction] * dist) % 360

    return abs(position[0]) + abs(position[1])
    # return position # , orientation

# print(day12p1())

def parse2(line):
	return line

def elem_mult(a,b):
    return [a[0]*b[0], a[1]*b[1]]

def day12p2():
    print('day 12 part 2')
    lines = ut.get_file('day12_input.txt', parse1)
    # lines = ut.get_file('day12_input_small.txt', parse1)
    way_position = [10, 1]
    way_orientation = 0
    ship_position = [0,0]
    action_map = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }
    angle_map = {
        'L': (-1,1),
        'R': (1,-1)
    }

    angle_direction = {
        0: 'E',
        90: 'N',
        180: 'W',
        270: 'S'
    }
    for direction, dist in lines:
        print(direction, dist)
        if direction == 'F':
        #     direction = angle_direction[way_orientation]
            ship_position = combine(ship_position, way_position, dist)
        if direction in action_map:
            change = action_map[direction]
            way_position = combine(way_position, change, dist)
        if direction in angle_map:
            for i in range(dist // 90):
                way_position = [way_position[1], way_position[0]] # [10,4]
                # [10,4] => [4, -10]
                way_position = elem_mult(way_position, angle_map[direction]) # negate either X or Y
            # way_orientation = (way_orientation + angle_map[direction] * dist) % 360

    print(ship_position, way_position , way_orientation)
    return abs(ship_position[0]) + abs(ship_position[1])

print(day12p2())
