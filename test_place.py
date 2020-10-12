"""(Incomplete) Tests for Place class."""
from Place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place("Townsville", "Australia", 12, "v")
    print(default_place)
    assert default_place.name == "Townsville"
    assert default_place.country == "Australia"
    assert default_place.priority == 12
    assert default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 3, False)
    # TODO: Write tests to show this initialisation works


    # TODO: Add more tests, as appropriate, for each method


run_tests()
