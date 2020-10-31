from abc import ABC, abstractmethod
import random

class State(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    def execute(self, name) -> bool:
        """ Main body of the state. """
        pass

class Cell():

    _state = None

    def __init__(self, state = State(), name = "", energy = None) -> None:
        self.name = name
        self.nucleus = False
        self.membrane = False
        self.wall = False
        self.mitochondrion = False
        self.cytoplasm = False
        self.centriole = False

        if energy is None:
            self.energy = random.uniform(0, 1)
        else:
            self.energy = energy
        self.transition_to(state, suppress_output = True)

    def change_energy(self, diff: float):
        self.energy += diff

    def transition_to(self, state, suppress_output = False):
        if not suppress_output:
            print("{} cell: Transition to {}".format(self.name, type(state).__name__))
        self._state = state
        self._state.context = self

    def live(self):
        while(self._state.execute(self.name)):
            pass

    def __str__(self) -> None:
        dict_parts = vars(self).copy()
        dict_parts.pop('name', None)
        dict_parts.pop('_state', None)
        list_parts = list(filter(lambda key: dict_parts.get(key), list(dict_parts.keys())))
        if not list_parts:
            return "{} cell contains nothing and has {} energy".format(self.name, self.energy)
        return "{} cell contains {} and has {} energy".format(self.name, ', '.join(list_parts), self.energy)

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
