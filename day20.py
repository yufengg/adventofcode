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
        print('creating tile', tile_num)
        self.num = tile_num
        # self.flipped = False
        self.rotated = 0 # 0 , 1, 2, 3
        self.imgs = []
        self.borders = [] # [(top, bottom, left, right)]
        self.orig_img = []
        for s in img_rows:
            self.orig_img.append(list(s))
        # self.imgs.append(self.orig_img)
        self.get_rotations() #and borders

    def flip(self, image): # X-axis flip
        new_image = list(reversed(image))
        return

    def copy_img(self):
        new_img = []
        for row in self.orig_img:
            new_img.append(row+[])
        return new_img

    def get_rotations(self): # 1-3
        # (x, y) original
        self.imgs.append(self.orig_img)

        # self._get_borders() # on orig_img
        # (y, -x)
        for t in range(3):
            new_img = self.copy_img()
            for i, row in enumerate(self.imgs[-1]):
                for j, val in enumerate(row):
                    new_img[j][-1-i] = val
            # do stuff with new_img as needed
            # get borders, etc
            self.imgs.append(new_img) # rotated

            print(self.num, 'rotation', t)
            self.display(new_img)

        flipped_list = []
        for im in self.imgs:
            # print('flipping')
            # self.display(im)
            flipped_img = list(reversed(im))
            flipped_list.append(flipped_img) # rotate-flipped

        self.imgs = self.imgs + flipped_list

        for im in self.imgs:
            self.borders.append(self._get_borders(im))
        # (-x, -y)
        # (-y, x)
        # self.img = new_img
        return self.imgs

    def _get_borders(self, img):
        top = img[0]
        bottom = img[-1]
        left = [] # consider replacing with list and join()-ing
        right = []
        for s in img:
            left.append(s[0])
            right.append(s[-1])
        return compact(top), compact(bottom), compact(left), compact(right)
        # return top, bottom, left, right

    def __repr__(self):
        return str(self.num) + '\n' + '\n'.join([''.join(s) for s in self.orig_img])

    def display(self, img):
        print('\n'.join([''.join(s) for s in img]))

    def display_list(self, img_list):
        for img in img_list:
            self.display(img)


# class Image:
#     self.edges = [] #exposed edges for docking
    # track positions of tiles, their IDs, their
    # Should tiles have l/r/u/d attributes as docking bays, and we walk the graph?
        # all exposed lrud borders attr that are None, are available
    # keep a handle on the upper-left-most tile?


def compact(l):
    return ''.join(l)

from collections import Counter

def day20p1():
    print('day 20 part 1')
    filename = 'day20_input.txt'
    # filename = 'day20_input_small.txt'
    tile_strs = parse1(filename) # [(id, img_str)]

    tile_lib = {}
    for t in tile_strs:
        tile_lib[t[0]] = Tile(t[0], t[1])

    # start assembling Image class

    # full_img = Image(tile_lib[3079])
    # while not full_img.complete():
    #     full_img.add_tile(tile_lib)
    #

    all_borders = []
    for k,v in tile_lib.items():
        borders = v.borders

        orig_img = borders[0] # orig
        for orig in orig_img:
            orig = int(orig.replace('.', '0').replace('#', '1'), 2)
            all_borders.append(orig)

        flipped_img = borders[4] # flipped
        for flipped in flipped_img:
            flipped = int(flipped.replace('.', '0').replace('#', '1'), 2)
            all_borders.append(flipped)

    border_ct = Counter(all_borders)
    print(border_ct)
    print(len(tile_lib), len(all_borders))

    border_unique = Counter(border_ct.values())
    print(border_unique)
    return # tile_lib[3079]

print(day20p1())

def parse2(line):
	return line

def day20p2():
    print('day 20 part 2')
    # lines = ut.get_file('day20_input.txt', parse2)
    lines = ut.get_file('day20_input_small.txt', parse2)
    return #lines

print(day20p2())
