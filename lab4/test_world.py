from pytest_bdd import scenario, given, when, then

from world import World
from cell_builder import Nature, CellBuilder

@scenario('test_world.feature', 'Creating the world')
def F():
    pass

@given("nature and builder")
def create_nature(nature, builder):
    nature = Nature()
    builder = CellBuilder()

@then("The world should be created")
def create_world():
    world = World(nature, builder)
    assert isinstance(world, World)

@when("Create four cells")
def creation_cells():
    world.add_four_cells()
    assert isinstance(world._cells[0], Cell)
    assert len(world._cells) == 4

@then("ok")
def f():
    pass

@when("Cells lives")
def cells_live():
    result = world.operation()

@then("Cells should dies")
def cells_die():
    assert "Fungan dies" in result
