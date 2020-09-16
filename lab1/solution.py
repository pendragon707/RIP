import argparse
import math

class Equation():
    pass

class LinEquation(Equation):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def calc_root(self):
        return -(self.b/self.a)

    def solution(self):
        if self.a == self.b == 0:
            print("Корней бесконечно много")
        elif self.a == 0:
            return []
        else:
            return [self.calc_root()]

class QuEquation(Equation):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.discr = -1

    def calc_discr(self):
        self.discr =  self.b ** 2 - 4 * self.a * self.c
        return self.discr

    def calc_root(self, d):
        return (-self.b + d) / (2 * self.a)

    def solution(self):
        if self.a == 0:
            return LinEquation(self.b, self.c).solution()

        self.calc_discr()
        if self.discr < 0:
#            return [self.calc_root(complex(self.discr**0.5))]
            return []
        elif self.discr == 0:
            return [self.calc_root(self.discr)]
        else:
            return [self.calc_root(math.sqrt(self.discr)), self.calc_root(-math.sqrt(self.discr))]

class BiQuEquation(QuEquation):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def calc_discr(self):
        if self.a == 0:
            return QuEquation(self.b, 0, self.c).calc_discr()
        return super().calc_discr()

    def calc_bi_root(self, qu_root):
        if qu_root < 0:
            return []
        elif qu_root == 0:
            return [qu_root]
        elif qu_root > 0:
            root = math.sqrt(qu_root)
            return [root, -root]

    def solution(self):
        if self.a == 0:
            return QuEquation(self.b, 0, self.c).solution()
        qu_roots = super().solution()
        answer = []
        for qu_root in qu_roots:
            answer += self.calc_bi_root(qu_root)
        return answer

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', help = 'first coefficient')
    parser.add_argument('--b', help = 'second coefficient')
    parser.add_argument('--c', help = 'fhird coefficient')
    return parser.parse_args()

def put_coef(args):
    print('Введите 3 коэффициента биквадратного уравнения')
    args.a = input('a = ')
    args.b = input('b = ')
    args.c = input('c = ')

def main():
    print('Подопригорова Н. ИУ5-54')
    args = parse()

    if not (args.a and args.b and args.c):
        put_coef(args)
    while True:
        try:
            args.a = float(args.a)
            args.b = float(args.b)
            args.c = float(args.c)
            break
        except:
            print('Не удаётся привести коэффициенты уравнения к типу float, попробуйте снова')
            put_coef(args)

    eq = BiQuEquation(args.a, args.b, args.c)
    if not (args.a == 0 and args.b == 0):
        print('Дискриминант: {d}'.format(d=eq.calc_discr()))
    answer = eq.solution()
    if answer == []:
        print('Действительных корней нет')
    elif answer is None:
        pass
    else:
        print('Корни: ', answer)

if __name__ == '__main__':
    main()
