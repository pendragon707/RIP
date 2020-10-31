# base state = class Cell in cell.py
# или же мы наследуем? давай наследуем и доопределим
#
#
#
# A -> A = 0.6
# A -> B = 0.3
# A -> C = 0.1
# B -> A = 0.9
# B -> C = 0.1
# C -> C = 1

from abc import ABC, abstractmethod
from cell import Cell
import random

# Может, сделать сюда builder или возможность передавать Cell в конструктор
class CellContext(Cell):

    _state = None

    def __init__(self, state, name = "", energy = random.uniform(0, 1)) -> None:
        super().__init__(name)
        self.energy = energy
        self.transition_to(state)

    def change_energy(self, diff: float):
        self.energy += diff

    def transition_to(self, state):

        print("{} cell: Transition to {}".format(self.name, type(state).__name__))
        self._state = state
        self._state.context = self

    def live(self):
        while True:
            print("{} cell has {} energy".format(self.name, self.energy), end = '\n\n')
            if not self._state.execute(self.name):
                break

class State(ABC):

    @property
    def context(self) -> CellContext:
        return self._context

    @context.setter
    def context(self, context: CellContext) -> None:
        self._context = context

    @abstractmethod
    def execute(self) -> bool:
        """ Main body of the state. """
        pass

class CellStateA(State):

    """ add energy (eat, breathes)"""
    def execute(self, name) -> bool:
        print("A")

        self.context.change_energy(random.normalvariate(0.1, 0.05))

        print("{} cell eat and breaths and get energy".format(name))
        self.change_state()

        return True

    def change_state(self) -> None:
        next_state = random.choices(['A', 'B', 'C'], weights = [1 - self.context.energy ** 2, self.context.energy ** (1/2), (self.context.energy - 1) ** 2])
        if next_state[0] == 'B':
            self.context.transition_to(CellStateB())
        elif next_state[0] == 'C':
            self.context.transition_to(CellStateC())


class CellStateB(State):
    """ duplicates """

    def execute(self, name) -> bool:
        print("B")

        self.context.change_energy(-self.context.energy*random.normalvariate(0.5, 0.1))

        print("{} cell duplicates".format(name))
        self.change_state()

        return True

    def change_state(self) -> None:
        next_state = random.choices(['A', 'C'], weights = [1 - self.context.energy ** 2, (self.context.energy - 1) ** 2])
        if next_state[0] == 'A':
            self.context.transition_to(CellStateA())
        elif next_state[0] == 'C':
            self.context.transition_to(CellStateC())


class CellStateC(State):
    """ dies """

    def execute(self, name) -> bool:
        print("C")
        print("{} dies".format(name))
        return False

def main():
    context = CellContext(CellStateA(), "Fungal")
    context.live()

if __name__ == "__main__":
    main()
