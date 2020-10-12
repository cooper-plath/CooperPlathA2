class Place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def is_visited(self):
        return self.visited == "v"

    def is_important(self):
        if self.priority >= 2:
            print(" is important")

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.country, self.priority, self.visited)