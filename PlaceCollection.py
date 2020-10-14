from Place import Place

class PlaceCollection:
    def __init__(self):
        self.file_places = []

    def __str__(self):
        return str([str(place) for place in self.file_places])



    def load_places(self, filename):
        self.filename = filename
        file_places = open(self.filename)
        for line in file_places:
            parts = line.strip().split(',')
            self.file_places.append(Place(parts[0], parts[1], int(parts[2]), parts[3]))
        file_places.close()
        return self.file_places


    def save_places(self):
        pass

    def add_place(self, place):
        self.file_places.append(place)


    def total_unvisited_places(self):
        pass

    def sort_priority(self):
        pass

def test():
    places = PlaceCollection
    print(places)

if __name__ == '__main__':
    test()