from Place import Place
from operator import attrgetter

class PlaceCollection:
    def __init__(self):
        self.file_places = []

    def __str__(self):
        return str([str(place) for place in self.file_places])



    def load_places(self, filename):
        self.filename = filename
        with open(filename) as file:
            for line in file:
                parts = line.strip().split(',')
                place = Place(parts[0], parts[1], int(parts[2]), parts[3])

                if parts[3] == 'v':
                    place.is_visited = True
                else:
                    place.is_visited = False
                self.file_places.append(place)



    def save_places(self):

        save_to_file = open(self.filename, 'w')
        new_row = 0
        for line in range(len(self.file_places)):
            save_to_file.write("{} \n".format(self.file_places[new_row]))
            new_row += 1
        save_to_file.close()

    def add_place(self, place):
        self.file_places.append(place)


    def total_unvisited_places(self):
        return len([1 for place in self.file_places if place.is_not_visited()])

    def sort(self, object):
        self.object = object
        return self.file_places.sort(key=attrgetter(object))

def test():
    places = PlaceCollection
    print(places)

if __name__ == '__main__':
    test()