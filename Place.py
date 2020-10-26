"""Place class: separates each item in place.csv into objects to be called upon"""


class Place:
    """Initialise place class with attributes that need to be entered to be considered a location"""
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = int(priority)
        self.visited = visited
        self.is_visited = self.is_visited
        self.is_important = self.is_important()

    """Return true if 'visited' object is 'v' or 'True'"""
    def is_visited(self):
        return self.visited == 'v' or self.visited == True
    """Returns true if object = 'n' or False"""
    def is_not_visited(self):
        return self.visited == 'n' or self.visited == False

    """If priority is equal to or less than 2, it's considered important"""
    def is_important(self):
        if self.priority <= 2:
            self.is_important = True
        else:
            self.is_important = False
    """If is_visited == True, print str with attributes with extra string"""
    def __str__(self):
        if self.is_visited == True:
            self.visited = "(Visited)"
        else:
            self.visited = ""
        return "{} in {}, priority {} {}".format(self.name, self.country, self.priority, self.visited)
