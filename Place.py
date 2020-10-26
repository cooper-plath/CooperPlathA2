
"""Place class: separates each item in place.csv into objects to be called upon"""
class Place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = int(priority)
        self.visited = visited
        self.is_visited = self.is_visited
        self.is_important = self.is_important()
    # Return true if 'visited' object is 'v'
    def is_visited(self):
        return self.visited == 'v' or self.visited == True

    def is_not_visited(self):
        return self.visited == 'n' or self.visited == False

    # Return true if 'priority' object is equal or less than 2
    def is_important(self):
        if self.priority <= 2:
            self.is_important = True
        else:
            self.is_important = False


    def __str__(self):
        # return "{} in {}, priority {}".format(self.name, self.country, self.priority)
        if self.is_visited == True:
            self.visited = "(Visited)"
        else:
            self.visited = ""
        return "{} in {}, priority {} {}".format(self.name, self.country, self.priority, self.visited)


"""Read places.csv and break each entry into name, country, etc using the Place class"""
# new_row = 0
# file_entry = []
# display_file = open('places.csv')
# for line in display_file:
#     line = line.strip()
#     parts = line.split(',')
#     parts[2] = int(parts[2])
#     new_row += 1
#     file_entry.append(Place(parts[0], parts[1], parts[2], parts[3]))






