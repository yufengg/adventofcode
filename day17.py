import utils as ut

def parse1(line):
    active_locs = []
    for i, c in enumerate(line):
        if c == '#':
            active_locs.append(i)

    return active_locs

def get_neighbors(x,y,z):
    deltas = [-1, 0, 1]
    n = []
    for i in deltas:
        for j in deltas:
            for k in deltas:
                if i == 0 and j == 0 and k == 0:
                    continue
                n.append((x+i, y+j, z+k))
    assert len(n) == 26
    return n

def next_state(cube, active_map):
    nei = get_neighbors(*cube)
    active_count = 0
    for n in nei:
        active_count += active_map.get(n, 0)

    # if cube == (3,1,0):
    #     print('3,1,0:', active_count)

    is_active = active_map.get(cube, 0)
    if is_active:
        if active_count == 2 or active_count == 3:
            return 1
        else:
            return 0
    else: # inactive
        if active_count == 3:
            return 1
        else:
            return 0

def disp_map(m):
    # dims = (-1,0,1,2, 3)
    x_range, y_range, z_range = map_dims(m)

    for k in range(*z_range):
        print(f'\nz={k}')
        for i in range(*x_range):
            for j in range(*y_range):
                if m.get((i,j,k), 0):
                    print('#', end='')
                else:
                    print('.', end='')
            print()

def map_dims(m, expand=False):
    x_range = [0, 2]
    y_range = [0, 2]
    z_range = [0, 2]
    # print(m)

    for (x, y, z), active in m.items():
        if active:
            x_range[0] = min(x, x_range[0])
            x_range[1] = max(x, x_range[1])

            y_range[0] = min(y, y_range[0])
            y_range[1] = max(y, y_range[1])

            z_range[0] = min(z, z_range[0])
            z_range[1] = max(z, z_range[1])

    x_range[1] += 1
    y_range[1] += 1
    z_range[1] += 1

    if expand:
        x_range[0] -=1
        x_range[1] +=1
        y_range[0] -= 1
        y_range[1] += 1
        z_range[0] -= 1
        z_range[1] += 1

    return x_range, y_range, z_range

def next_map(old_map):
    new_map = {}

    dims = (-1, 0, 1, 2, 3)
    # inf = float('inf')
    x_range, y_range, z_range = map_dims(old_map, expand=True)

    # print(x_range, y_range, z_range)

    for i in range(*x_range):
        for j in range(*y_range):
            for k in range(*z_range):
                next_val = next_state((i, j, k), old_map)
                if next_val:
                    new_map[i, j, k] = next_val

    # disp_map(new_map)
    return new_map


def day17p1():
    print('day 17 part 1')
    lines = ut.get_file('day17_input.txt', parse1)
    # lines = ut.get_file('day17_input_small.txt', parse1)

    active_map = {}
    for i, row in enumerate(lines):
        for j in row:
            active_map[(i, j, 0)] = 1 # active

    # disp_map(active_map)
    # go through the full space, checking for the next state of each cube
    for _ in range(6):
        active_map = next_map(active_map)

    # for cube, active in active_map.items():
    #     if active:
    #         neighbors = get_neighbors(*cube)
            # print(neighbors,'\n')

    # print(next_state((0,0,0), active_map))

    return sum(active_map.values())

# print(day17p1()) #1hr 9min


def get_neighbors2(x,y,z,w):
    deltas = [-1, 0, 1]
    n = []
    for i in deltas:
        for j in deltas:
            for k in deltas:
                for l in deltas:
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    n.append((x+i, y+j, z+k, w+l))
    assert len(n) == 3**4-1
    return n

def next_state2(cube, active_map):
    nei = get_neighbors2(*cube)
    active_count = 0
    for n in nei:
        active_count += active_map.get(n, 0)

    is_active = active_map.get(cube, 0)
    if is_active:
        if active_count == 2 or active_count == 3:
            return 1
        else:
            return 0
    else: # inactive
        if active_count == 3:
            return 1
        else:
            return 0

def disp_map2(m):
    # dims = (-1,0,1,2, 3)
    x_range, y_range, z_range, w_range = map_dims(m)

    for l in range(*w_range):
        for k in range(*z_range):
            print(f'\nz={k}, w={l}')
            for i in range(*x_range):
                for j in range(*y_range):
                    if m.get((i,j,k,l), 0):
                        print('#', end='')
                    else:
                        print('.', end='')
                print()

def map_dims2(m, expand=False):
    x_range = [0, 2]
    y_range = [0, 2]
    z_range = [0, 2]
    w_range = [0, 2]
    # print(m)

    for (x, y, z, w), active in m.items():
        if active:
            x_range[0] = min(x, x_range[0])
            x_range[1] = max(x, x_range[1])

            y_range[0] = min(y, y_range[0])
            y_range[1] = max(y, y_range[1])

            z_range[0] = min(z, z_range[0])
            z_range[1] = max(z, z_range[1])

            w_range[0] = min(w, w_range[0])
            w_range[1] = max(w, w_range[1])

    x_range[1] += 1
    y_range[1] += 1
    z_range[1] += 1
    w_range[1] += 1

    if expand:
        x_range[0] -=1
        x_range[1] +=1
        y_range[0] -= 1
        y_range[1] += 1
        z_range[0] -= 1
        z_range[1] += 1
        w_range[0] -= 1
        w_range[1] += 1

    return x_range, y_range, z_range, w_range

def next_map2(old_map):
    new_map = {}

    # dims = (-1, 0, 1, 2, 3)
    # inf = float('inf')
    x_range, y_range, z_range, w_range = map_dims2(old_map, expand=True)

    # print(x_range, y_range, z_range, w_range)

    for i in range(*x_range):
        for j in range(*y_range):
            for k in range(*z_range):
                for l in range(*w_range):
                    next_val = next_state2((i, j, k, l), old_map)
                    if next_val:
                        new_map[i, j, k, l] = next_val

    # disp_map(new_map)
    return new_map



def day17p2():
    print('day 17 part 2')
    lines = ut.get_file('day17_input.txt', parse1)
    # lines = ut.get_file('day17_input_small.txt', parse1)

    active_map = {}
    for i, row in enumerate(lines):
        for j in row:
            active_map[(i, j, 0, 0)] = 1  # active

    # go through the full space, checking for the next state of each cube
    for _ in range(6):
        active_map = next_map2(active_map)

    return sum(active_map.values())

print(day17p2()) # 1hr 20min
