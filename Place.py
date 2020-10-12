
"""Place class: separates each item in place.csv into objects to be called upon"""
class Place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited
    # Return true if 'visited' object is 'v'
    def is_visited(self):
        return self.visited == 'v'

    # Return true if 'priority' object is equal or less than 2
    def is_important(self):
        return self.priority <= 2

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.country, self.priority, self.visited)

new_row = 0
entry_number = []
display_file = open('places.csv')
for line in display_file:
    line = line.strip()
    parts = line.split(',')
    # name = parts[0]
    # country = parts[1]
    # priority = parts[2]
    # visited = parts[3]
    # print(f"{new_row}. {Place(name, country, priority, visited)}")
    new_row += 1
    entry_number.append(Place(parts[0], parts[1], parts[2], parts[3]))
print(entry_number[0].is_visited())






# display_file = open('places.csv')
# item_number = 1
# for line in display_file:
#     line = line.strip()
#     parts = line.split(',')
#     name = parts[0]
#     country = parts[1]
#     priority = parts[2]
#     visited = parts[3]
#     Place = Place(name, country, priority, visited)



