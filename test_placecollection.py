"""(Incomplete) Tests for PlaceCollection class."""
from PlaceCollection import PlaceCollection
from Place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.file_places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.file_places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)
    # TODO: Add more sorting tests

    place_collection.sort("country")
    print(place_collection)
    # TODO: Test saving places (check CSV file manually to see results)

    place_collection.save_places()
    print(place_collection)
    place_collection.add_place(Place("Townsville", "Australia", 7, True))
    print(f"Updated: {place_collection}")


    # TODO: Add more tests, as appropriate, for each method
    print(place_collection.total_unvisited_places())




run_tests()
