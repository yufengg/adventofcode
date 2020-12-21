import utils as ut

def parse1(fn):
    with open(fn) as f:
        tile_strs = f.read().split('\n\n')

    tiles = [] # (tile_num, img_rows)
    for tile_str in tile_strs:
        tile_num, *img_rows = tile_str.split('\n')
        tile_num = int(tile_num.lstrip('Tile ')[:-1]) # 'Tile 1289:' => 1289

        tiles.append((tile_num, img_rows))
    print(len(tiles))
    return tiles

class Tile:
    def __init__(self, tile_num, img_rows):
        self.num = tile_num
        self.img = img_rows
        self.flipped = 'N' # X and Y
        self.rotated = 0 # 0 , 1, 2, 3

    def flip(self, axis): # X or Y?
        if axis == 'X':
            self.img = reversed(self.img)
            self.flipped = 'X' # assuming starting from N
            return

        elif axis == 'Y':
            temp_img = []
            for s in self.img:
                temp_img.append(reversed(s))
            self.img = temp_img
            self.flipped = 'Y'
            return

    def rotate(self, times): # 1-3
        pass

    def get_borders(self):
        top = self.img[0]
        bottom = self.img[-1]
        left = '' # consider replacing with list and join()-ing
        right = ''
        for s in self.img:
            left += s[0]
            right += s[-1]
        return top, bottom, left, right

    def __repr__(self):
        return '\n'.join(self.img)

# class Image: # ??

def day20p1():
    print('day 20 part 1')
    filename = 'day20_input.txt'
    # filename = 'day20_input_small.txt'
    tile_strs = parse1(filename)



    return tile_strs[0]

print(day20p1())

def parse2(line):
	return line

def day20p2():
    print('day 20 part 2')
    # lines = ut.get_file('day20_input.txt', parse2)
    lines = ut.get_file('day20_input_small.txt', parse2)
    return #lines

print(day20p2())
