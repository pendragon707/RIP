#def f(d, key):
#    return (d.get(key) == True)

class Cell():
    """
    Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
    достаточно сложны и требуют обширной конфигурации.

    В отличие от других порождающих паттернов, различные конкретные строители
    могут производить несвязанные продукты. Другими словами, результаты
    различных строителей могут не всегда следовать одному и тому же интерфейсу.
    """

    def __init__(self, name = "") -> None:
        self.name = name
        self.nucleus = False
        self.membrane = False
        self.wall = False
        self.mitochondrion = False
        self.cytoplasm = False
        self.centriole = False

    def set_name(self, name) -> None:
        self.name = name

    def add_nucleus(self) -> None:
        self.nucleus = True

    def add_membrane(self) -> None:
        self.membrane = True

    def add_wall(self) -> None:
        self.wall = True

    def add_wall(self) -> None:
        self.wall = True

    def add_mitochondrion(self) -> None:
        self.mitochondrion = True

    def add_citoplasm(self) -> None:
        self.cytoplasm = True

    def add_centriole(self) -> None:
        self.centriole = True

    def __str__(self) -> None:
    #    list_all_parts = ["Ядро", "Мембрана", "Клеточная стенка", "Митохондрии", "Цитоплазма", "Центриоли"]
     #   list_parts = list(filter(condition, list_all_parts))
        dict_parts = vars(self).copy()
        dict_parts.pop('name', None)
        list_parts = list(filter(lambda key: dict_parts.get(key), list(dict_parts.keys())))
        if not list_parts:
            return "Cell {} contains nothing".format(self.name)
        return "Cell {} contains {}".format(self.name, ', '.join(list_parts))

