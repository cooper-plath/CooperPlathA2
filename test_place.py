"""(Incomplete) Tests for Place class."""
from Place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place("Townsville", "Australia", 0, "v")
    print(default_place)
    assert default_place.name == "Townsville"
    assert default_place.country == "Australia"
    assert default_place.priority == 0
    assert default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 2, False)
    # TODO: Write tests to show this initialisation works
    print(new_place)
    print(new_place.name)
    print(new_place.country)
    print(new_place.priority)
    print(new_place.visited)

    print(f"Dict: {new_place.__dict__}")




    # TODO: Add more tests, as appropriate, for each method
    print("Is important: {}".format(new_place.is_important()))
    print("Visited? {}".format(new_place.is_visited()))


run_tests()
