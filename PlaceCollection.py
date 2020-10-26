from Place import Place
from operator import attrgetter

"""PlaceCollection class with Place class called and attrgetter"""


class PlaceCollection:
    def __init__(self):
        self.file_places = []

    def __str__(self):
        return str([str(place) for place in self.file_places])

    """Load entries from filename called in function, splits up entries into strings and organises them using Place Class"""

    def load_places(self, filename):
        self.filename = filename
        with open(filename) as file:
            for line in file:
                parts = line.strip().split(',')
                place = Place(parts[0], parts[1], parts[2], parts[3])

                if parts[3] == 'v' or parts[3] == True:
                    place.is_visited = True
                else:
                    place.is_visited = False
                self.file_places.append(place)

    """Opens chosen file, wipes new, and appends each line from main list"""

    def save_places(self, filename):
        self.filename = filename
        save_to_file = open(self.filename, 'w')
        for place in self.file_places:
            if place.visited == True:
                place = (f"{place.name}, {place.country}, {str(place.priority)}, v")
            else:
                place = (f"{place.name}, {place.country}, {str(place.priority)}, n")
            save_to_file.write("{} \n".format(place))
        save_to_file.close()
        # new_row = 0
        # for line in range(len(self.file_places)):
        #     save_to_file.write("{} \n".format(self.file_places[new_row]))
        #     new_row += 1
        # save_to_file.close()

    """Adds new entry to main list when called"""

    def add_place(self, place):
        self.file_places.append(place)

    """for each item in main list, add to running count if is.visited == False before returning"""

    def total_unvisited_places(self):
        return len([1 for place in self.file_places if place.is_visited == False])

    """Using imported attrgetter, sort list by object passed through function"""

    def sort(self, object):
        self.object = object
        return self.file_places.sort(key=attrgetter(object))


def test():
    places = PlaceCollection
    print(places)


if __name__ == '__main__':
    test()
