from cell import Nature, CellBuilder
from cell_state import Cell
from cell_states import CellStateA, CellStateB, CellStateC

class World:

    def __init__(self, nature: Nature, builder: CellBuilder) -> None:
        self._cells = []
        self._nature = nature or Nature()
        self._builder = builder or CellBuilder()

    def add_four_cells(self) -> None:
        # строители создают клетки и помещают их в список cells
        self._nature.builder = self._builder

        nature.build_animal_cell()
        self._cells.append(builder.cell)

        nature.build_plant_cell()
        self._cells.append(builder.cell)

        nature.build_bacteria_cell()
        self._cells.append(builder.cell)

        nature.build_fungal_cell()
        self._cells.append(builder.cell)

    def operation(self) -> str:
        self.add_four_cells()
        print(*self._cells, sep='\n')
        for cell in self._cells:
            cell.live()

def main(world):
    world.operation()


if __name__ == "__main__":


    nature = Nature()
    builder = CellBuilder()

    world = World(nature, builder)
    main(world)
