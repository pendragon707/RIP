# A -> A = 0.6
# A -> B = 0.3
# A -> C = 0.1
# B -> A = 0.9
# B -> C = 0.1
# C -> C = 1

from abc import ABC, abstractmethod
from cell import Cell, State
import random

class CellStateA(State):

    """ add energy (eat, breathes)"""
    def execute(self):
#        print("A")
        results = []
        self.context.change_energy(random.normalvariate(0.1, 0.05))

#        print("\n{} cell eat and breaths".format(self.context.name))
#        print("{} cell has {} energy".format(self.context.name, self.context.energy))
        results.append("\n{} cell eat and breaths".format(self.context.name))
        results.append("{} cell has {} energy".format(self.context.name, self.context.energy))
        results.append(self.change_state())

        return True, "\n".join(results)

    def change_state(self):
        results = []
        next_state = random.choices(['A', 'B', 'C'], weights = [1 - self.context.energy ** 2, self.context.energy ** (1/2), (self.context.energy - 1) ** 2])
        if next_state[0] == 'B':
            results.append(self.context.transition_to(CellStateB()))
        elif next_state[0] == 'C':
            results.append(self.context.transition_to(CellStateC()))
        return "\n".join(results)


class CellStateB(State):
    """ duplicates """

    def execute(self):
#        print("B")
        results = []
        self.context.change_energy(-self.context.energy*random.normalvariate(0.5, 0.1))

#        print("\n{} cell duplicates".format(self.context.name))
#        print("{} cell has {} energy".format(self.context.name, self.context.energy))
        results.append("\n{} cell duplicates".format(self.context.name))
        results.append("{} cell has {} energy".format(self.context.name, self.context.energy))
        results.append(self.change_state())

        return True, "\n".join(results)

    def change_state(self):
        results = []
        next_state = random.choices(['A', 'C'], weights = [1 - self.context.energy ** 2, (self.context.energy - 1) ** 2])
        if next_state[0] == 'A':
            results.append(self.context.transition_to(CellStateA()))
        elif next_state[0] == 'C':
            results.append(self.context.transition_to(CellStateC()))
        return "\n".join(results)


class CellStateC(State):
    """ dies """

    def execute(self) -> bool:
#        print("C")
        results = []
#        print("\n{} cell dies".format(self.context.name))
        results.append("\n{} cell dies".format(self.context.name))
        return False, "\n".join(results)

def main():
    cell = Cell(CellStateA(), "Fungal")
    print(cell.live())

if __name__ == "__main__":
    main()
