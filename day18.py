import utils as ut

def parse1(line):
    print('processing', line)
    return Expr(line).eval()

class Expr:
    def __init__(self, s):
        self.string = s
        if len(self.string) == 1:
            self.l = self.string
            self.r = ''
            self.op = ''
            return

        # print('creating', s)

        self.parse_exp()
        # print(self.__dir__())
        if 'op' not in self.__dir__():
            # drop fully wrapping ()
            if self.string[0] == '(' and self.string[-1] == ')':
                self.string = self.string[1:-1]
                self.parse_exp()

    def parse_exp(self):
        open_parens = 0
        for i, c in enumerate(self.string):
            if c == ' ':
                continue
            if c in '*+' and open_parens == 0:
                self.op = c
                self.l = Expr(self.string[0:i].strip())
                self.r = Expr(self.string[i+1:].strip())
            if c in '(':
                open_parens += 1
                # open_index = i
            if c in ')':
                open_parens -= 1

    def eval(self):
        if self.op == '':
            return int(self.l)

        left = self.l.eval()
        right = self.r.eval()
        if self.op == '*':
            return left * right
        if self.op == '+':
            return left + right

    def __repr__(self):
        if self.op == '':
            return str(self.l)
        return f'{self.l} {self.op} {self.r}'

def day18p1():
    print('day 18 part 1')
    lines = ut.get_file('day18_input.txt', parse1)
    # lines = ut.get_file('day18_input_small.txt', parse1)
    return sum(lines)

# print(day18p1()) #47min

def parse2(line):
    print('2processing', line)
    return Expr2(line).eval()


class Expr2:
    def __init__(self, s):
        self.string = s
        if len(self.string) == 1:
            self.l = self.string
            self.r = ''
            self.op = ''
            return

        # print('creating', s)

        # self.parse_exp()
        # print(self.__dir__())
        while not self.parse_exp(): #'op' not in self.__dir__():
            if self.parse_exp(splitter='+'):
                break
            # drop fully wrapping ()
            if self.string[0] == '(' and self.string[-1] == ')':
                self.string = self.string[1:-1]
                if self.parse_exp():
                    break



    def parse_exp(self, splitter='*'):
        open_parens = 0
        split_success = False
        for i, c in enumerate(self.string):
            if c == ' ':
                continue
            if c == splitter and open_parens == 0:
                self.op = c
                self.l = Expr2(self.string[0:i].strip())
                self.r = Expr2(self.string[i+1:].strip())
                split_success = True
            if c in '(':
                open_parens += 1
                # open_index = i
            if c in ')':
                open_parens -= 1

            assert open_parens >= 0
        return split_success

    def eval(self):
        if self.op == '':
            return int(self.l)

        left = self.l.eval()
        right = self.r.eval()
        if self.op == '*':
            return left * right
        if self.op == '+':
            return left + right

    def __repr__(self):
        if self.op == '':
            return str(self.l)
        return f'{self.l} {self.op} {self.r}'


def day18p2():
    print('day 18 part 2')
    lines = ut.get_file('day18_input.txt', parse2)
    # lines = ut.get_file('day18_input_small.txt', parse2)
    print(lines)
    return sum(lines)


print(day18p2()) #1hr 7min
