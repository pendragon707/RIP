from cell_state import Cell

#from abc import ABC, abstractmethod
#import random
#
#class Cell():
#
#    _state = None
#
#    def __init__(self, state = None, name = "", energy = None) -> None:
#        self.name = name
#        self.nucleus = False
#        self.membrane = False
#        self.wall = False
#        self.mitochondrion = False
#        self.cytoplasm = False
#        self.centriole = False
#
#        if energy is None:
#            self.energy = random.uniform(0, 1)
#        else:
#            self.energy = energy
##        self.transition_to(state)
#
##    def build(self, builder):
##        self.name = builder._cell.name
##        self.nucleus = builder._cell.nucleus
##        self.membrane = builder._cell.membrane
##        self.wall = builder._cell.wall
##        self.mitochondrion = builder._cell.mitochondrion
##        self.cytoplasm = builder._cell.cytoplasm
##        self.centriole = builder._cell.centriole
#
#    def change_energy(self, diff: float):
#        self.energy += diff
#
#    def transition_to(self, state):
#
#        print("{} cell: Transition to {}".format(self.name, type(state).__name__))
#        self._state = state
#        self._state.context = self
#
#    def live(self):
#        while True:
#            print("{} cell has {} energy".format(self.name, self.energy), end = '\n\n')
#            if not self._state.execute(self.name):
#                break
#
#    def __str__(self) -> None:
#        dict_parts = vars(self).copy()
#        dict_parts.pop('name', None)
#        dict_parts.pop('_state', None)
#        list_parts = list(filter(lambda key: dict_parts.get(key), list(dict_parts.keys())))
#        if not list_parts:
#            return "{} cell contains nothing and has {} energy".format(self.name, self.energy)
#        return "{} cell contains {} and has {} energy".format(self.name, ', '.join(list_parts), self.energy)
#
#class State(ABC):
#
#    @property
#    def context(self) -> Cell:
#        return self._context
#
#    @context.setter
#    def context(self, context: Cell) -> None:
#        self._context = context
#
#    def execute(self) -> bool:
#        """ Main body of the state. """
#        pass

class CellBuilder():
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._cell = Cell()

    @property
    def cell(self) -> Cell:
        cell = self._cell
        self.reset()
        return cell

    def set_name(self, name) -> None:
        self._cell.name = name

    def add_nucleus(self) -> None:
        self._cell.nucleus = True

    def add_membrane(self) -> None:
        self._cell.membrane = True

    def add_wall(self) -> None:
        self._cell.wall = True

    def add_mitochondrion(self) -> None:
        self._cell.mitochondrion = True

    def add_citoplasm(self) -> None:
        self._cell.cytoplasm = True

    def add_centriole(self) -> None:
        self._cell.centriole = True

class Nature:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> CellBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CellBuilder) -> None:
        self._builder = builder

    def build_animal_cell(self) -> None:
        self.builder.set_name("Animal")
        self.builder.add_nucleus()
        self.builder.add_membrane()
        self.builder.add_mitochondrion()
        self.builder.add_citoplasm()
        self.builder.add_centriole()

    def build_bacteria_cell(self) -> None:
        self.builder.set_name("Bacterial")
        self.builder.add_membrane()
        self.builder.add_wall()
        self.builder.add_citoplasm()

    def build_plant_cell(self) -> None:
        self.builder.set_name("Plant")
        self.builder.add_nucleus()
        self.builder.add_membrane()
        self.builder.add_wall()
        self.builder.add_mitochondrion()
        self.builder.add_citoplasm()
        self.builder.add_centriole()

    def build_fungal_cell(self) -> None:
        self.builder.set_name("Fungal")
        self.builder.add_nucleus()
        self.builder.add_membrane()
        self.builder.add_wall()
        self.builder.add_mitochondrion()
        self.builder.add_citoplasm()

def main():
    nature = Nature()
    builder = CellBuilder()
    nature.builder = builder

    nature.build_animal_cell()
    print(builder.cell)

    nature.build_plant_cell()
    print(builder.cell)

    nature.build_bacteria_cell()
    print(builder.cell)

    nature.build_fungal_cell()
    print(builder.cell)

if __name__ == "__main__":
    main()
