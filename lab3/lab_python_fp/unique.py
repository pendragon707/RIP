class Unique(object):
    # Итератор для удаления дубликатов

    def __init__(self, items, **kwargs):
            self.items = items   # массив или генератор
            self.used_elements = set()
            self.index = 0
            if(kwargs.get('ignore_case')):
                self.indicator = True
            else:
                self.indicator = False

    def __next__(self):
        while(True):
            if(type(self.items) is type(generator(5))):
                current = next(self.items)
            elif(type(self.items) == list):
                if self.index >= len(self.items):
                    raise StopIteration
                current = self.items[self.index]
                self.index = self.index + 1
            else:
                raise TypeError
            if(type(current) == str and self.indicator):
                current = current.lower()
            if current not in self.used_elements:
                self.used_elements.add(current)
                return current

    def __iter__(self):
        return self


def generator(x):
    yield x
