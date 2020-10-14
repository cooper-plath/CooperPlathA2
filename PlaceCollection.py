from Place import Place

class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, places):
        new_row = 0
        display_file = open('places.csv')
        for line in display_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            new_row += 1
            self.places.append(Place(parts[0], parts[1], parts[2], parts[3]))


    def save_places(self):
        pass

    def add_place(self):
        pass

    def total_unvisited_places(self):
        pass

    def sort_priority(self):
        pass