from cell_builder import Nature, CellBuilder
from cell import Cell
from cell_states import CellStateA, CellStateB, CellStateC

class World:

    def __init__(self, nature: Nature, builder: CellBuilder) -> None:
        self._cells = []
        self._nature = nature or Nature()
        self._builder = builder or CellBuilder()

    def add_four_cells(self) -> None:
        # строители создают клетки и помещают их в список cells
        self._nature.builder = self._builder

        self._nature.build_animal_cell()
        self._cells.append(self._builder.cell)

        self._nature.build_plant_cell()
        self._cells.append(self._builder.cell)

        self._nature.build_bacteria_cell()
        self._cells.append(self._builder.cell)

        self._nature.build_fungal_cell()
        self._cells.append(self._builder.cell)

    def operation(self) -> str:
        results = []
        self.add_four_cells()
        for cell in self._cells:
            results.append(cell.__str__())
            results.append(cell.live())
            results.append("\n -------------------------------------- \n")
        return "\n".join(results)

def main(world):
    print(world.operation())


if __name__ == "__main__":
    nature = Nature()
    builder = CellBuilder()

    world = World(nature, builder)
    main(world)
