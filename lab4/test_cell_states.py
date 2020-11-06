import unittest
from unittest.mock import Mock

from cell_states import CellStateA
from cell import Cell

class TestCellStateA(unittest.TestCase):

    def setUp(self):
        self.mockCell = Mock()
        self.mockCell.energy = 1.
        self.mockCell.name = "Mushroom"
        self.mockCell.change_energy = Mock(return_value = None)
        self.mockCell.transition_to = Mock(return_value = "Transition to CellStateE")
        self.mockCell.live = Mock(return_value = "I'm alive")

        self.state = CellStateA()
        self.state.context = self.mockCell

    def test_execute(self):
        self.assertIn("Mushroom cell has 1.0 energy", self.state.execute()[1])
        self.assertEqual(True, self.state.execute()[0])

    def test_change_state(self):
        self.assertEqual("Transition to CellStateE", self.state.change_state())

if __name__ == "__main__":
    unittest.main()
