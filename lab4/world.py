class World:
    """
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """

    def __init__(self, cells) -> None:
        """
        В зависимости от потребностей вашего приложения вы можете предоставить
        Фасаду существующие объекты подсистемы или заставить Фасад создать их
        самостоятельно.
        """

        self._cells = cells or None

    def operation(self) -> str:
        # смена состояний конечного автомата и вывод каждого шага
        pass


def main(world):
    world.operation()


if __name__ == "__main__":
    # В клиентском коде могут быть уже созданы некоторые объекты подсистемы. В
    # этом случае может оказаться целесообразным инициализировать Фасад с этими
    # объектами вместо того, чтобы позволить Фасаду создавать новые экземпляры.



    # строители создают клетки и помещают их в список cells

    world = World(cells)
    main(world)
