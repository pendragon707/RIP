import unittest
from unittest.mock import Mock

from cell_builder import Nature, CellBuilder
from world import World
from cell import Cell

class TestWorld(unittest.TestCase):
    def setUp(self):
        self.nature = Nature()
        self.builder = CellBuilder()
        self.world = World(self.nature, self.builder)

    def test_add_four_cells(self):
        self.world.add_four_cells()
        self.assertIsInstance(self.world._cells[0], Cell)
        self.assertEqual(len(self.world._cells), 4)

    def test_operation(self):
        result = self.world.operation()
        self.assertIn("Fungal cell dies", result)

if __name__ == "__main__":
    unittest.main()
